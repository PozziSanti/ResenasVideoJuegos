from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, User
from django.contrib.auth.signals import user_logged_in, user_logged_out

# Crear roles automáticamente
@receiver(post_migrate)
def create_roles(sender, **kwargs):
    roles = ['usuario', 'admin', 'invitado']
    for role in roles:
        Group.objects.get_or_create(name=role)

# Asignar 'usuario' cuando se registra
@receiver(post_save, sender=User)
def assign_user_role(sender, instance, created, **kwargs):
    if created:
        user_group = Group.objects.get(name='usuario')
        instance.groups.add(user_group)

# Cuando inicia sesión
@receiver(user_logged_in)
def asignar_usuario(sender, request, user, **kwargs):
    usuario_group = Group.objects.get(name='usuario')
    if not user.groups.filter(name='usuario').exists():
        user.groups.add(usuario_group)

    invitado_group = Group.objects.get(name='invitado')
    user.groups.remove(invitado_group)

    request.session['rol'] = 'usuario'

# Cuando cierra sesión
@receiver(user_logged_out)
def asignar_invitado(sender, request, user, **kwargs):
    request.session['rol'] = 'invitado'