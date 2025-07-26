from django.contrib import admin
from django.contrib.auth.models import Group

# Desregistrar el registro por defecto
admin.site.unregister(Group)

# Registrar con configuración personalizada (opcional)
admin.site.register(Group)