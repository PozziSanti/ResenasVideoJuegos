from django.urls import path
from apps.favorite import views

urlpatterns = [
    path('toggle/<uuid:review_id>/', views.toggle_favorite, name='toggle_favorite'),
]