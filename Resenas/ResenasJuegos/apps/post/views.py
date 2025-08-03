from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm

# Helper: verificar si el usuario es admin o creador del post
def es_autor_o_admin(user, post):
    return user.is_superuser or post.autor == user

# Verificación de rol

def es_usuario(user):
    return user.groups.filter(name='usuario').exists() or user.is_superuser

def es_invitado(user):
    return not user.is_authenticated

# Lista de posts (público)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

# Ver detalle (público)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

# Crear post (solo usuario o admin)
@login_required
@user_passes_test(es_usuario)
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_create.html', {'form': form})

# Editar post (solo autor o admin)
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not es_autor_o_admin(request.user, post):
        return HttpResponseForbidden("No tenés permiso para editar este post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_update.html', {'form': form, 'post': post})

# Eliminar post (solo autor o admin)
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not es_autor_o_admin(request.user, post):
        return HttpResponseForbidden("No tenés permiso para eliminar este post.")

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post/post_delete.html', {'post': post})