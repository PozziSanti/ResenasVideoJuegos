from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category

admin.site.register(Category)

#TODO: Necesitamos crear un superusuario (admin) para probar el modulo categorías.