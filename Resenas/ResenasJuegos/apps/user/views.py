from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import ProfileForm
from .models import UserProfile


class UserSignupView(CreateView):
    template_name = 'user/user_signup.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        UserProfile.objects.create(user=user)  # crea perfil en blanco automáticamente
        return redirect('edit_profile')    # redirige al formulario para que lo complete

    def get_success_url(self):
        return reverse('edit_profile')
        
        
class UserLoginView(LoginView):
    template_name = 'user/user_signin.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('home')


#class HomeView(TemplateView):
#    template_name = 'user/user_home.html'


class DashboardView(TemplateView):
    template_name = 'user/user_dashboard.html'



@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # lugar de redirección después de guardar el perfil
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'user/user_profile.html', {'form': form})
