from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, get_user_model
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from apps.user.forms import LoginForm, RegisterForm
from apps.user.models import UserProfile
from django.http import HttpResponse


User = get_user_model()

def inicio(request):
    rol = request.session.get('rol', 'invitado')
    return HttpResponse(f"Rol actual: {rol}")

class UserSignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
        
class UserLoginView(LoginView):
    template_name = 'registration/signin.html'
    form_class = LoginForm
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