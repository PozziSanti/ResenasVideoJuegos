from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, get_user_model
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from apps.user.forms import LoginForm, RegisterForm, EditForm, ChangePasswordForm
from apps.user.models import UserProfile
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from apps.favorite.models import Favorite


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
        return self.request.GET.get('next') or reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('home')

#PERMITE EDITAR PERFIL
@login_required
def edit_profile(request):
    profile = request.user 
    
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile') 
    else:
        form = EditForm(instance=profile)

    return render(request, 'user/edit_profile.html', {'form': form})

#PERMITE VER PERFIL
@login_required
def profile(request):
    user_profile = request.user
    favorites = Favorite.objects.filter(user=request.user).select_related('post')
    return render(request, 'user/user_profile.html', {'user_profile': user_profile, 'favorites': favorites
})

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user) # Required to keep the user logged in
            return redirect('edit_profile')
    else:
        form = ChangePasswordForm(user)

    return render(request, 'user/change_password.html', {'form': form})