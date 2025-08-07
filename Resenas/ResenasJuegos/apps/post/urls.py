from django.urls import path
from apps.post.views import IndexView, AboutView, PostDetailView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),  # Pagina sobre nosotros 
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
