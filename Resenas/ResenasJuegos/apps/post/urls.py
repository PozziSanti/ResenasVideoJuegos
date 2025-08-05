from django.urls import path
from apps.post.views import IndexView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
]
