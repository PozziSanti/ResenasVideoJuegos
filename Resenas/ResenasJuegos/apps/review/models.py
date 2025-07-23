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
    date_creation = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_creation']
    
    def average_score(self):
        final_score = self.final_score.all()
        return round(sum(p.score for p in final_score) / len(final_score), 2) if final_score else 0
    
    def __str__(self):
        return f"{self.title} ({self.score})"
