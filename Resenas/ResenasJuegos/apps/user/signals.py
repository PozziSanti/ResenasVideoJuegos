from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apps.user.models import UserProfile
from apps.post.models import Post
from apps.comment.models import Comment
from apps.favorite.models import Favorite

@receiver(post_save, sender=UserProfile)
def asignar_grupo_usuario(sender, instance, created, **kwargs):
    """
    Asigna automáticamente el grupo 'usuario' a los nuevos usuarios.
    """
    if created:  # Solo cuando se crea por primera vez
        try:
            grupo_usuario = Group.objects.get(name='usuario')
            instance.groups.add(grupo_usuario)
            print(f"✅ Usuario {instance.username} asignado al grupo 'usuario'")
        except Group.DoesNotExist:
            print("⚠️ El grupo 'usuario' no existe. Ejecuta migrate primero.")


@receiver(post_migrate)
def crear_grupos_y_permisos(sender, **kwargs):
    """
    Crea los grupos 'usuario' y 'admin' con los permisos correspondientes.
    Se ejecuta automáticamente después de migrate.
    """
    # --- Grupo Usuario ---
    usuario_group, _ = Group.objects.get_or_create(name="usuario")

    permisos_usuario = Permission.objects.filter(
        codename__in=[
            # Comentarios
            "add_comment", "change_comment", "delete_comment", "view_comment",
            # Posts
            "view_post",
            # Favoritos
            "add_favorite", "delete_favorite", "view_favorite",
        ]
    )
    usuario_group.permissions.set(permisos_usuario)

    # --- Grupo Admin ---
    admin_group, _ = Group.objects.get_or_create(name="admin")

    permisos_admin = Permission.objects.filter(
        codename__in=[
            # Comentarios
            "add_comment", "change_comment", "delete_comment", "view_comment",
            # Posts
            "add_post", "change_post", "delete_post", "view_post",
            # Favoritos
            "add_favorite", "delete_favorite", "view_favorite",
        ]
    )
    admin_group.permissions.set(permisos_admin)