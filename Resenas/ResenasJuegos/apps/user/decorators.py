from django.http import HttpResponseForbidden

def rol_requerido(roles):
    if isinstance(roles, str):
        roles = [roles]

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or request.user.rol not in roles:
                return HttpResponseForbidden("No tienes permisos para acceder a esta vista.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
