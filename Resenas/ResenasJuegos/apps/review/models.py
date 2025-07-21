from django.db import models
from django.contrib.auth.models import User

#MODELO CATEGORÍA
class Category(models.Model): 
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]

    def __str__(self):
        return self.name

   
#MODELO PLATAFORMAS   
class Plataform(models.Model): 
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ["name"]

    def __str__(self):
        return self.name


#MODELO POSTS 
class Review(models.Model): #TODO Hay que hacer una view/formulario que nos permita cargar las reseñas
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #TODO Hay que decidir si es que cuando un usuario borre su perfil vamos a borrar sus posts también
    #TODO Hay que decidir si vamos a cargar imagenes
    score = models.DecimalField(max_digits=3, decimal_places=1)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    plataform = models.ManyToManyField('Plataform')
    date_creation = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_creation']
    
    def __str__(self):
        return f"{self.title} ({self.score})"
