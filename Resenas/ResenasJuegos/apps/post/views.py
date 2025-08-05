from django.views.generic import TemplateView
from apps.post.models import Category, Post

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categorias = Category.objects.all()
        posts_por_categoria = {}

        for categoria in categorias:
            posts = Post.objects.filter(category__in=[categoria]).prefetch_related('images')
            posts_por_categoria[categoria.title] = posts

        context['posts_por_categoria'] = posts_por_categoria

        print("DEBUG - Categorías encontradas:")
        for cat, posts in posts_por_categoria.items():
            print(f"  {cat} → {posts.count()} posts")

        return context

