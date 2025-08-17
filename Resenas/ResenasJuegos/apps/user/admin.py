from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    # Columnas personalizadas para mostrar si pertenece a grupos
    def is_usuario(self, obj):
        return obj.groups.filter(name='usuario').exists()
    is_usuario.short_description = 'Es Usuario'
    is_usuario.boolean = True

    def is_admin_group(self, obj):
        return obj.groups.filter(name='admin').exists()
    is_admin_group.short_description = 'Es Admin'
    is_admin_group.boolean = True

    # Acciones masivas
    def add_to_usuario(self, request, queryset):
        group = Group.objects.get(name='usuario')
        for user in queryset:
            user.groups.add(group)
        self.message_user(request, "Usuarios añadidos al grupo 'usuario'.")
    add_to_usuario.short_description = 'Agregar a Usuario'

    def remove_from_usuario(self, request, queryset):
        group = Group.objects.get(name='usuario')
        for user in queryset:
            user.groups.remove(group)
        self.message_user(request, "Usuarios removidos del grupo 'usuario'.")
    remove_from_usuario.short_description = 'Remover de Usuario'

    def add_to_admins(self, request, queryset):
        group = Group.objects.get(name='admin')
        for user in queryset:
            user.groups.add(group)
        self.message_user(request, "Usuarios añadidos al grupo 'admin'.")
    add_to_admins.short_description = 'Agregar a Admin'

    def remove_from_admins(self, request, queryset):
        group = Group.objects.get(name='admin')
        for user in queryset:
            user.groups.remove(group)
        self.message_user(request, "Usuarios removidos del grupo 'admin'.")
    remove_from_admins.short_description = 'Remover de Admin'

    # Configuración de qué mostrar en la lista de usuarios
    list_display = (
        'username', 'email', 'is_staff', 'is_superuser',
        'is_usuario', 'is_admin_group'
    )

    actions = [
        add_to_usuario,
        remove_from_usuario,
        add_to_admins,
        remove_from_admins,
    ]


admin.site.register(UserProfile, CustomUserAdmin)
