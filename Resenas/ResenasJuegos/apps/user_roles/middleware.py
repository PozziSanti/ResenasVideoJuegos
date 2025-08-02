from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser

class InvitadoMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            request.rol = 'guest'
        elif hasattr(user, 'perfil'):
            request.rol = user.perfil.rol
        else:
            request.rol = 'guest'
            