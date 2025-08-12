from django.db import models
from django.contrib.auth.models import AbstractUser
import os
import uuid

<<<<<<< HEAD
#AGREGAR FOTO DE PERFIL Y BIOGAFIA (OPCIONAL)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
=======
def get_avatar_filename(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f"user_{instance.id}_avatar{file_extension}"
    return os.path.join('user/avatar/', new_filename)

class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to=get_avatar_filename, default='user/default/avatar_default.avif')
>>>>>>> 9b01a82081ca73d1e5c0499ad4907b8e72bc6352
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.username}'