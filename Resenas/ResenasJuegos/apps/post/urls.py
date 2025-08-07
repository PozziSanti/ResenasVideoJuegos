from django.urls import path
from apps.post.views import IndexView, AboutView, TermsView, PrivacyView, PostDetailView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),  # Sobre nosotros 
    path('terms/', TermsView.as_view(), name='terms'),  # Terminos y condiciones 
    path('privacy/', PrivacyView.as_view(), name='privacy'),  # Politica de Privacidad
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
