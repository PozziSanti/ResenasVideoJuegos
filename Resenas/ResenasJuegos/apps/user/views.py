from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView


class UserSignupView(CreateView):
    template_name = 'user/user_signup.html'
    form_class = UserCreationForm
    
    def get_success_url(self):
        return reverse_lazy('home')  

    def form_valid(self, form):
            response = super().form_valid(form)
            login(self.request, self.object)  
            return response
        
        
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
