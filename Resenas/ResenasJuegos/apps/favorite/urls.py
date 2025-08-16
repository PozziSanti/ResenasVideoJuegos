from django.urls import path
from .views import toggle_favorite

urlpatterns = [
    path('<slug:slug>/toggle/', toggle_favorite, name='toggle_favorite'),
]