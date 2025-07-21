from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.

# Signup (Registrar nuevo usuario)
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
    })

    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })
   
    

# Home (inicio)
def home(request):
    return render(request, 'home.html')


# Dashboard (panel de tareas)
def dashboard(request):
    return render(request, 'dashboard.html')


# Logout (cerrar sesión)
def goout(request):
    logout(request)
    return redirect('home')


# login (Iniciar sesion)
def signin(request):
    if request.method == 'GET':
         return render(request, 'signin.html', {   # Envía el formulario de "Iniciar sesión"
        'form': AuthenticationForm
        }) 
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos'   # Si se cargan mal los datos, arroja un mensaje de error y vuelve a mandar el formulario
            }) 
        else:
            login(request, user)
            return redirect('dashboard')     # si todo está correcto, redirecciona y guarda la sesion del usuario

       
        