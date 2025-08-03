from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apps.post.models import Post
from apps.comment.models import Comentario
from apps.score.models import Score

# Obtener content types
post_ct = ContentType.objects.get_for_model(Post)
comentario_ct = ContentType.objects.get_for_model(Comentario)
score_ct = ContentType.objects.get_for_model(Score)

# Permisos específicos
permisos_post = Permission.objects.filter(content_type=post_ct)
permisos_comentario = Permission.objects.filter(content_type=comentario_ct)
permisos_score = Permission.objects.filter(content_type=score_ct)

# Grupos
grupo_usuario, _ = Group.objects.get_or_create(name='usuario')
grupo_admin, _ = Group.objects.get_or_create(name='admin')

# Limpiar permisos actuales (opcional si querés empezar de cero)
grupo_usuario.permissions.clear()
grupo_admin.permissions.clear()

# Asignar permisos al grupo admin (todos los permisos)
for permiso in list(permisos_post) + list(permisos_comentario) + list(permisos_score):
    grupo_admin.permissions.add(permiso)

# Asignar solo permisos de comentario y puntuar al grupo usuario
for permiso in list(permisos_comentario) + list(permisos_score):
    grupo_usuario.permissions.add(permiso)

print("✅ Permisos actualizados: admin tiene todo, usuario solo comentar y puntuar.")