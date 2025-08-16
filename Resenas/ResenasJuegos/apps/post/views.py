from django.views.generic import TemplateView, ListView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from apps.post.models import Post, Category, PostImage
from django.db.models import Avg, Value, FloatField
from django.db.models.functions import Coalesce
from apps.comment.forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .forms import PostForm, UpdatePostForm
from apps.comment.models import Comment
from apps.favorite.models import Favorite
from django.views import View
from django.http import JsonResponse
from django.conf import settings

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

class PostAutocomplete(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        results = []
        if q:
            posts = Post.objects.filter(title__icontains=q)[:5]  # límite 5 resultados
            results = list(posts.values_list('title', flat=True))
        return JsonResponse(results, safe=False)

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

    # DA LOS NOMBRES A CADA UNA DE LAS CATEGORIAS DEL SIDEBAR EN LA PAGINA (JUEGOS DE ...)********************************
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = self.kwargs.get('category', '')
        return context


# SE PUEDE REUTILIZAR PARA FILTRO MAS RECIENTES, MAS ANTIGUOS
# class PostDateFilter(ListView):
#     model = Post
#     template_name = 'post/post_list.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         date = self.request.GET.get('date')

#         if date:
#             queryset = queryset.filter(created_at__date=date) # busca el post por fecha de publicación
        
#         return queryset


# Filtros post por estrellas - REUTILIZAR EL IF SCORE PARA FILTRO DE MAYOR PUNTUACION A MENOR PUNTUACION
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

        # Saber si este post ya está en favoritos
        if self.request.user.is_authenticated:
            context['is_favorited'] = Favorite.objects.filter(
                user=self.request.user,
                post=post
            ).exists()
        else:
            context['is_favorited'] = False

        if self.request.user.is_authenticated:
            edit_comment_id = self.request.GET.get('edit_comment_id')
            if edit_comment_id:
                comment_to_edit = get_object_or_404(Comment, pk=edit_comment_id, post=post)
                if comment_to_edit.user == self.request.user:
                    context['edit_comment_form'] = CommentForm(instance=comment_to_edit)
                    context['editing_comment_id'] = comment_to_edit.id
                else:
                    context['edit_comment_form'] = None
                    context['editing_comment_id'] = None
            else:
                context['form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        post = self.object

        if not request.user.is_authenticated:
            return redirect('login') #Si el usuario no está logueado, lo manda a iniciar sesión
        
        #ELIMINAR COMENTARIO
        delete_comment_id = request.POST.get('delete_comment_id')
        if delete_comment_id:
            comment = get_object_or_404(Comment, pk=delete_comment_id, post=post)
            if comment.user == request.user or post.author == request.user:  # Solo el dueño puede eliminar
                comment.delete()
            return redirect('post_detail', slug=post.slug)

        #EDITAR COMENTARIO
        comment_id = request.POST.get('comment_id')
        if comment_id:
            comment = get_object_or_404(Comment, pk=comment_id, post=post)
            if comment.user != request.user:
                return redirect('post_detail', slug=post.slug)

            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('post_detail', slug=post.slug)
            else:
                # Si el form no es válido, recargamos la página con errores
                context = self.get_context_data()
                context['form'] = form
                context['editing'] = comment
                return self.render_to_response(context)
        
        if Comment.objects.filter(user=request.user, post=post).exists():
            context = self.get_context_data()
            context['form'] = CommentForm()
            context['error_message'] = "Ya has dejado una reseña para este post."
            return self.render_to_response(context)
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect('post_detail', slug=self.object.slug)
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


# Crear un nuevo post
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

# TODO: agregar funcion 403 para que aparezca imagen del michi
    def form_valid(self, form):
        form.instance.author = self.request.user
        print("\n=== INICIO DEL PROCESO DE GUARDADO ===")
    
        try:
            print("\n1. Guardando post principal...")
            self.object = form.save(commit=True)
            print(f"✅ Post guardado con ID: {self.object.id}")
            
            print("\n2. Procesando imágenes...")
            form.images.instance = self.object
            is_valid = form.images.is_valid()
            print(f"🔍 Formset válido?: {is_valid}")
            
            if not is_valid:
                print(f"❌ Errores en el formset: {form.images.errors}")
                # Agregar errores del formset al formulario principal
                for error in form.images.errors:
                    form.add_error(None, error)
                return self.form_invalid(form)
            else:
                print("✅ Formset válido, guardando imágenes...")
                form.images.save()
                print(f"📸 Imágenes guardadas correctamente para el post {self.object.id}")
                
        except Exception as e:
            print(f"‼️ ERROR CRÍTICO: {str(e)}")
            form.add_error(None, f"Error al guardar imágenes: {str(e)}")
            return self.form_invalid(form)
        
        print("\n=== PROCESO COMPLETADO CON ÉXITO ===")
        return super().form_valid(form)
    
    def test_func(self):
        user = self.request.user
        return user.has_perm('post.add_post') or user.is_superuser # Solo permite acceso a usuarios administradores y superusuarios


# Actualizar un post existente
class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model=Post
    form_class = UpdatePostForm
    template_name = 'post/post_update.html'

    def get_success_url(self):
        return reverse_lazy ('post_detail', kwargs={'slug': self.object.slug})

#TODO: agregar funcion 403 para que aparezca imagen del michi
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['active_images'] = self.get_object().images.filter(active=True)
            print(kwargs['active_images'])
            return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category_ids'] = [c.id for c in self.object.category.all()]
        return context
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:            # Filtra los post para que solo los autores o superusuarios editen el post
            return Post.objects.all()
        return Post.objects.filter(author=user)

    def form_valid(self, form): # TODO: si se quiere que el autor del post cambie al editar, agregar: post.autor = self.request.user
        post=form.save(commit=False)
        active_images=form.active_images
        keep_any_image_active=False

        if active_images: #Mantener imagen activa
            for image in active_images:
                field_name=f"keep_image_{image.id}"
                if not form.cleaned_data.get(field_name, True):
                    image.active = False
                    image.save 
                else:
                    keep_any_image_active=True
        
        images =self.request.FILES.getlist("images")  #Agregar imagen
        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        
        if not keep_any_image_active and not images:
            PostImage.objects.create(post=post, image=settings.DEFAULT_POST_IMAGE)
        
        post.save()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        user = self.request.user
        return user == post.author or user.is_superuser # Solo permite acceso a usuarios autores y superusuarios


# Listar todos los posts
# class PostListView(ListView):
#     model = Post
#     template_name = 'post/post_list.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         return (Post.objects.all()
#         .prefetch_related('images')
#         # .annotate(avg_score=Coalesce
#         #         (Avg('comment__score'),
#         #          Value(0.0, output_field=FloatField())
#         #         )
#         #     )
#         .order_by('-created_at')
#         )  # get_queryset se usa para optimizar la consulta y traer las imágenes relacionadas de una sola vez, además de calcular el promedio de puntuaciones


# Eliminar un post existente
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home')

# TODO: agregar funcion 403 para que aparezca imagen del michi     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['can_delete'] = user.has_perm('post.delete_post') or user.is_superuser
        return context

    def test_func(self):
        user = self.request.user
        return user.has_perm('post.delete_post') or user.is_superuser # Solo permite acceso a usuarios administradores y superusuario
        



# CRUD PARA LAS CATEGORIAS

# Crear una nueva categoría
class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['title']
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('home')  # Redirige a la lista de categorías después de crear una

    def test_func(self):
        user = self.request.user
        return user.has_perm('post.add_category') or user.is_superuser # Solo permite acceso a usuarios administradores y superusuarios


# Listar todas las categorías
class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

# Editar una categoría existente
class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['title']
    template_name = 'category/category_update.html'
    success_url = reverse_lazy('home')  # Redirige a la lista de categorías después de editar una

    def test_func(self):
        user = self.request.user
        return user.has_perm('post.change_category') or user.is_superuser # Solo permite acceso a usuarios administradores y superusuarios


# Eliminar una categoría existente
class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category/category_delete.html'
    success_url = reverse_lazy('home')  # Redirige a la lista de categorías después de eliminar una

    def test_func(self):
        user = self.request.user
        return user.has_perm('post.delete_category') or user.is_superuser # Solo permite acceso a usuarios administradores y superusuarios 

 

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/post_detail.html'
    
    def get_object(self):
        return get_object_or_404(Comment, id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.object.post
        context["comments"] = (
            self.object.post.comment
            .all()
            .order_by("-created_at")
        )
        return context
        
    def get_success_url(self):
        print('SLUG', self.object.post.slug)
        return reverse_lazy("post_detail", kwargs={"slug": self.object.post.slug})

