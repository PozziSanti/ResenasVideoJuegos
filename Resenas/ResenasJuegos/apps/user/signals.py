from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from apps.user.models import UserProfile
from apps.post.models import Post
from apps.comment.models import Comment
from apps.favorite.models import Favorite

@receiver(post_migrate)
def crear_grupos_y_permisos(sender, **kwargs):
    if sender.name != 'apps.user':
        return
    try:
        # Obtener ContentTypes
        post_ct = ContentType.objects.get_for_model(Post)
        comentario_ct = ContentType.objects.get_for_model(Comment)
        favorito_ct = ContentType.objects.get_for_model(Favorite)

        # Obtener permisos por modelo
        permisos_post = Permission.objects.filter(content_type=post_ct)
        permisos_comentario = Permission.objects.filter(content_type=comentario_ct)
        permisos_favorito = Permission.objects.filter(content_type=favorito_ct)

        # Crear grupos
        grupo_usuario, _ = Group.objects.get_or_create(name='usuario')
        grupo_admin, _ = Group.objects.get_or_create(name='admin')

        # Limpiar permisos para mantenerlos actualizados
        grupo_usuario.permissions.clear()
        grupo_admin.permissions.clear()

        # Admin → todos los permisos
        for permiso in list(permisos_post) + list(permisos_comentario) + list(permisos_favorito):
            grupo_admin.permissions.add(permiso)

        # Usuario → solo comentarios y favoritos
        for permiso in list(permisos_comentario) + list(permisos_favorito):
            grupo_usuario.permissions.add(permiso)

        print("✅ Grupos y permisos creados/actualizados correctamente.")

    except Exception as e:
        print(f"⚠️ Error al crear grupos y permisos: {e}")