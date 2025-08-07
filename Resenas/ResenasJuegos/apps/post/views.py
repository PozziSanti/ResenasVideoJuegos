from django.views.generic import TemplateView, DetailView
from django.shortcuts import redirect
from apps.post.models import Category, Post
from apps.comment.models import Comment
from apps.comment.forms import CommentForm


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