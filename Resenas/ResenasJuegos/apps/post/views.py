from django.views.generic import ListView
from apps.post.models import Post 
from django.db.models import Avg, Value
from django.db.models.functions import Coalesce


# Create your views here.

# Filtros post por titulo
class PostTitleFilter(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(title__icontains=q) # busca en el título de los posts
        
        return queryset


# Filtros post por categoría
class PostCategoryFilter (ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.kwargs.get('category') # Obtiene la categoría de los parámetros de la URL

        if category:
            queryset = queryset.filter(title__icontains=category) 
        
        return queryset

# TODO: si se decide poner el filtro de la fecha en el buscador, se lo puede agregar a la vista PostTitleFilter
# Filtros post por fecha de publicación
class PostDateFilter(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get('date')

        if date:
            queryset = queryset.filter(created_at__date=date) # busca el post por fecha de publicación
        
        return queryset

# TODO: se lo puede poner para filtrar por fecha de inicio y fin 
# fecha_inicio = self.request.GET.get('desde')
# fecha_fin = self.request.GET.get('hasta')

# if fecha_inicio and fecha_fin:
#     queryset = queryset.filter(created_at__date__range=[fecha_inicio, fecha_fin])

# filtros por post por estrellas
class PostStarFilter(ListView):
    model = Post
    template_name = 'post/post_list.html' 
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset().annotate(avg_score=Coalesce(Avg('comment__score'), Value(0)))  # Calcula el promedio de las calificaciones de los comentarios
        
        score = self.request.GET.get('score') # valor que viene del formulario de búsqueda

        if score:
            try:
                score = float(score)
                queryset = queryset.filter(avg_score__gte=score) # filtra comentarios que tengan un valor de estrellas mayor o igual al ingresado
            except ValueError:
                pass      # si el valor no es un número válido, no se aplica el filtro
        return queryset