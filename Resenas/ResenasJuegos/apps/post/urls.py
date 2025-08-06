from django.urls import path
from apps.post.views import IndexView, PostDetailView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
