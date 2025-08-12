
from django.views.generic import TemplateView, ListView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from apps.post.models import Post, Category, PostImage
from django.db.models import Avg, Value, FloatField
from django.db.models.functions import Coalesce
from apps.comment.forms import CommentForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import PostForm
# from apps.comment.models import Comment


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

# filtros post por estrellas
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
            queryset = queryset.filter(category__title__iexact=category) 
        
        return queryset

    
    # TODO: sacar, ya que es solo para probar el filtro de categoría
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = self.kwargs.get('category', '')
        return context


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


# filtros post por estrellas
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


# CRUD PARA LOS POSTS

# Detalle de un post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
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



# CRUD PARA LOS POSTS


# Crear un nuevo post
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('home')    # Redirige a la lista de posts después de crear uno

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


# TODO: agregar funcion 403 para que aparezca imagen del michi
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        user = self.request.user
        return user.has_perm('post.add_post') or user.is_superuser # Solo permite acceso a usuarios administradores y superusuarios


# Actualizar un post existente
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = PostForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    template_name = 'post_update.html'
    success_url = reverse_lazy('post_list')    # Redirige a la lista de posts después de crear uno

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.author = self.request.user      # TODO: si se quiere que el autor del post cambie al editar, agregar: post.autor = self.request.user
        post.save()
        return redirect (self.success_url)


# Actualizar un post existente
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    fields = ['titulo', 'contenido', 'categoria', 'imagen']
    template_name = 'post_update.html'
    success_url = reverse_lazy('post_list')    # Redirige a la lista de posts después de crear uno

    template_name = 'post/post_update.html'
    success_url = reverse_lazy('post_list')    # Redirige a la lista de posts después de crear uno

# TODO: agregar funcion 403 para que aparezca imagen del michi
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['request'] = self.request
            return kwargs

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:            # Filtra los post para que solo los autores o superusuarios editen el post
            return Post.objects.all()
        return Post.objects.filter(author=user)

    def form_valid(self, form):
        post = form.save(commit=False)      # TODO: si se quiere que el autor del post cambie al editar, agregar: post.autor = self.request.user
        post.save()
        return super().form_valid(form)    
    
    def test_func(self):
        post = self.get_object()
        user = self.request.user
        return user == post.author or user.is_superuser # Solo permite acceso a usuarios autores y superusuarios


# Listar todos los posts
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return (Post.objects.all()
        .prefetch_related('images')
        .annotate(avg_score=Coalesce
                (Avg('comment__score'),
                 Value(0.0, output_field=FloatField())
                )
            )
        .order_by('-created_at')
        )  # get_queryset se usa para optimizar la consulta y traer las imágenes relacionadas de una sola vez, además de calcular el promedio de puntuaciones


# Eliminar un post existente
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post_list')  # Redirige a la lista de posts después de eliminar uno

# TODO: agregar funcion 403 para que aparezca imagen del michi     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['can_delete'] = user.has_perm('post.delete_post') or user.is_superuser
        return context

    def test_func(self):
        user = self.request.user
        return user.has_perm('post.delete_post') or user.is_superuser # Solo permite acceso a usuarios administradores y superusuarios
