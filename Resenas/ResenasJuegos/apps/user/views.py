from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from .models import UserProfile
from django.contrib.auth import get_user_model
from django.http import HttpResponse


User = get_user_model()

def inicio(request):
    rol = request.session.get('rol', 'invitado')
    return HttpResponse(f"Rol actual: {rol}")
class UserSignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        next_url = self.request.GET.get('next') or self.request.POST.get('next') or '/' # Tomar la URL de origen si existe
        signin_url = f"{reverse('signin')}?next={next_url}"
        return redirect(signin_url)    # redirige al formulario para que lo complete
        
class UserLoginView(LoginView):
    template_name = 'registration/signin.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return self.request.GET.get('next') or reverse_lazy('home') # Si hay una URL de redirección pasada, usarla; si no, ir a home


def logout_view(request):
    logout(request)
    return redirect('home')


#PERMITE EDITAR PERFIL
#TODO=cambiar redireccion de dashboard
@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # lugar de redirección después de guardar el perfil
    else:
        form = RegisterForm(instance=profile)

    return render(request, 'user/user_profile.html', {'form': form})