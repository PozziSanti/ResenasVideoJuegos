from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def inicio(request):
    rol = request.session.get('rol', 'invitado')
    return HttpResponse(f"Rol actual: {rol}")

@login_required
def vista_usuario(request):
    return HttpResponse("Bienvenido usuario autenticado")

@login_required
def vista_admin(request):
    if request.user.groups.filter(name='admin').exists():
        return HttpResponse("Bienvenido administrador")
    return HttpResponse("No tienes permisos para acceder aquí")
