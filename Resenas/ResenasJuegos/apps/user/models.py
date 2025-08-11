from django.db import models
from django.contrib.auth.models import AbstractUser
import os
import uuid

def get_avatar_filename(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f"user_{instance.id}_avatar{file_extension}"
    return os.path.join('user/avatar/', new_filename)

class UserProfile(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('user', 'Usuario'),
        ('guest', 'Invitado'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to=get_avatar_filename, default='user/default/avatar_default.avif')
    bio = models.TextField(blank=True, null=True)
    rol = models.CharField(max_length=10, choices=ROLES, default='guest')

    def __str__(self):
        return f'Perfil de {self.user.username} - {self.rol}'