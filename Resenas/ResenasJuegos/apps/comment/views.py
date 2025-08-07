from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from apps.comment.models import Comment

#TODO= REVISAR ROLES
#Solo deja entrar a la función si el usuario está logueado y es staff(administrador). Si no esta logueado, Django lo redirige al login.
@user_passes_test(lambda u: u.is_staff)
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id) # Busca el comentario con ese id en la base de datos. Si no existe, devuelve error 404 automáticamente.
    slug = comment.post.slug
    comment.delete()
    return redirect('post_detail', slug=slug) #Después de borrar, te redirige a la vista de detalle del post al que pertenecía el comentario.