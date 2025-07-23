from django.db import models
from django.contrib.auth.models import User
from .models import Category
from .models import Plataform
import uuid
   
#MODELO POSTS 
class Review(models.Model): #TODO Hay que hacer una view/formulario que nos permita cargar las reseñas
    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    #FOREIGN KEYS
    author = models.ForeignKey(User, on_delete=models.CASCADE) #TODO Hay que decidir si es que cuando un usuario borre su perfil vamos a borrar sus posts también
    category = models.ManyToManyField(Category, on_delete=models.SET_NULL, null=True, related_name='review')
    plataform = models.ManyToManyField(Plataform, on_delete=models.SET_NULL, null=True, related_name='review')
    
    #ATRIBUTOS
    title = models.CharField(max_length=100)
    content = models.TextField()
    #TODO Hay que decidir si vamos a cargar imagenes
    score = models.DecimalField(max_digits=3, decimal_places=1) #TODO Necesito que muestre el promedio de calificaciones.
    date_creation = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_creation']
    
    def __str__(self):
        return f"{self.title} ({self.score})"
