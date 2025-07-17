from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_roles'

    def ready(self):
        import user_roles.signals  # Importamos señales