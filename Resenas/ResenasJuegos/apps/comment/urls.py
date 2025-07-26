from django.urls import path
from apps.comment.views import add_comment

urlpatterns = [
    path('comentar/<uuid:review_id>/', add_comment, name='comentar_reseña'),
]