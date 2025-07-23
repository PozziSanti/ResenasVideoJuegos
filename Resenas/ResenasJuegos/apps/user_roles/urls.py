from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuario/', views.vista_usuario, name='vista_usuario'),
    path('admin/', views.vista_admin, name='vista_admin'),
]