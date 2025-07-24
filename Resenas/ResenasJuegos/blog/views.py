from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.

# Signup (Registrar nuevo usuario)
def user_signup(request):
    if request.method == 'GET':
        return render(request, 'user/user_signup.html', {
            'form': UserCreationForm
    })

    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('user_dashboard')
            except IntegrityError:
                return render(request, 'user/user_signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'user/user_signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })
   
    

# Home (inicio)
def user_home(request):
    return render(request, 'user/user_home.html')


# Dashboard (panel de tareas)
def user_dashboard(request):
    return render(request, 'user/user_dashboard.html')


# Logout (cerrar sesión)
def user_goout(request):
    logout(request)
    return redirect('user_home')


# login (Iniciar sesion)
def user_signin(request):
    if request.method == 'GET':
         return render(request, 'user/user_signin.html', {   # Envía el formulario de "Iniciar sesión"
        'form': AuthenticationForm
        }) 
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user/user_signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos'   # Si se cargan mal los datos, arroja un mensaje de error y vuelve a mandar el formulario
            }) 
        else:
            login(request, user)
            return redirect('user_dashboard')  