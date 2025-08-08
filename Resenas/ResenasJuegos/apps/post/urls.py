from django.urls import path
<<<<<<< HEAD
from apps.post.views import IndexView, AboutView, PostDetailView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),  # Pagina sobre nosotros 
=======
from apps.post.views import IndexView, AboutView, TermsView, PostDetailView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),  # Sobre nosotros 
    path('terminos/', TermsView.as_view(), name='terms'),  # Terminos y condiciones 
>>>>>>> 8c85955895b87662a000d50fa1fd91d4093cbcca
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
