from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.post.models import Post
from apps.favorite.models import Favorite

@login_required
def toggle_favorite(request, slug):
    post = get_object_or_404(Post, slug=slug)
    favorite, created = Favorite.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        favorite.delete()
    
    return redirect('post_detail', slug=slug)