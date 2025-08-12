from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import UserProfile

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'alias')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
