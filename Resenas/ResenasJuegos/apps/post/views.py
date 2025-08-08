from django.views.generic import ListView
from apps.post.models import Post 
from django.db.models import Avg, Value
from django.db.models.functions import Coalesce
from django.views.generic import TemplateView, DetailView
from django.shortcuts import redirect
from apps.post.models import Category, Post
from apps.comment.models import Comment
from apps.comment.forms import CommentForm


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


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        print("🟢 VERIFICANDO DATOS EN VISTA:") #TODO:SACAR
        categorias = Category.objects.all()
        print("Categorías encontradas:", list(categorias.values('id', 'title'))) #TODO:SACAR
    
        posts_por_categoria = {}
        for categoria in categorias:
            posts = Post.objects.filter(category=categoria).prefetch_related('images')
            print(f"Posts en {categoria.title}:", list(posts.values('id', 'title'))) #TODO:SACAR
            posts_por_categoria[categoria.title] = posts
    
        context['posts_por_categoria'] = posts_por_categoria
        print("🟢 CONTEXTO FINAL:", context) #TODO:SACAR
        return context

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class TermsView(TemplateView):
    template_name = "pages/terms.html"

class PrivacyPolicyView(TemplateView):
    template_name = 'pages/privacy.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        context['comments'] = post.comment.filter(approbed=True).order_by('-created_at') #carga comentario actual
        context['next_post'] = Post.objects.filter(id__gt=post.id).order_by('id').first() #Agrega todos los comentarios del post actual, ordenados del más nuevo al más viejo
        context['prev_post'] = Post.objects.filter(id__lt=post.id).order_by('-id').first()
        
        #Agrega los botones de navegación (post siguiente y anterior).
        if self.request.user.is_authenticated:
            context['form'] = CommentForm()
        return context #Si el usuario está logueado, le pasa el formulario para comentar

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect('login')

        #Si el usuario no está logueado, lo manda a iniciar sesión
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
        return redirect('post_detail', slug=self.object.slug) #Redirecciona a la misma página para que el comentario se vea en pantalla

