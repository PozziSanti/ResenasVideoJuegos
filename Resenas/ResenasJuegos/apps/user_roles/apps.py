from django.apps import AppConfig


class UserRolesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user_roles'

    def ready(self):
        import apps.user_roles.signals
