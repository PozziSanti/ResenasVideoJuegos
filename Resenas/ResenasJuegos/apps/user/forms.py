from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ya existe un usuario con este nombre.")
        return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirm

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

class EditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'alias', 'bio', 'avatar')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'block w-full text-lg text-light bg-transparent border-b-2 border-light-morado focus:outline-none px-3 py-3 placeholder-text-medium'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full text-lg text-light bg-transparent border-b-2 border-light-morado focus:outline-none px-3 py-3 placeholder-text-medium'}),
            'alias': forms.TextInput(attrs={'class': 'block w-full text-lg text-light bg-transparent border-b-2 border-light-morado focus:outline-none px-3 py-3 placeholder-text-medium'}),
            'bio': forms.Textarea(attrs={'class': 'block w-full text-lg text-light bg-transparent border-b-2 border-light-morado focus:outline-none px-3 py-3 placeholder-text-medium', 'rows': 2}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'text-light-morado'})
        }

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label="Contraseña Actual", widget=forms.PasswordInput(attrs={'class': 'block w-full text-lg text-light bg-transparent border-b-2 border-light-morado focus:outline-none px-3 py-3 placeholder-text-medium'}))
    new_password = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput(attrs={'class': 'block w-full text-lg text-light bg-transparent border-b-2 border-light-morado focus:outline-none px-3 py-3 placeholder-text-medium'}))
    new_password_confirm = forms.CharField(label="Confirmar Nueva Contraseña", widget=forms.PasswordInput(attrs={'class': 'block w-full text-lg text-light bg-transparent border-b-2 border-light-morado focus:outline-none px-3 py-3 placeholder-text-medium'}))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_current_password(self):
        current_password = self.cleaned_data.get('current_password')
        if not self.user.check_password(current_password):
            raise forms.ValidationError("La contraseña actual es incorrecta.")
        return current_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        new_password_confirm = cleaned_data.get("new_password_confirm")

        if new_password and new_password_confirm and new_password != new_password_confirm:
            self.add_error('new_password_confirm', "Las nuevas contraseñas no coinciden.")

        if new_password:
            try:
                validate_password(new_password, self.user)
            except ValidationError as e:
                self.add_error('new_password', e.messages)

        return cleaned_data

    def save(self, commit=True):
        new_password = self.cleaned_data['new_password']
        self.user.set_password(new_password)
        if commit:
            self.user.save()
        return self.user