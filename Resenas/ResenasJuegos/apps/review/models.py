from django.db import models
from django.contrib.auth.models import User
from apps.clasification.models import Category
from apps.clasification.models import Plataform
import uuid
import os
   
def get_card_image_filename(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f"review_{instance.id}_card_image{file_extension}"

    return os.path.join('review/card_image/', new_filename)

#MODELO POSTS 
class Review(models.Model): #TODO Modelos incompleto, falta slug #TODO Hay que hacer una view/formulario que nos permita cargar las reseñas
    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    #FOREIGN KEYS
    author = models.ForeignKey(User, on_delete=models.CASCADE) #TODO Hay que decidir si es que cuando un usuario borre su perfil vamos a borrar sus posts también
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='review')
    plataform = models.ForeignKey(Plataform, on_delete=models.SET_NULL, null=True, related_name='review')
    
    #ATRIBUTOS
    title = models.CharField(max_length=100)
    content = models.TextField()
    card_image = models.ImageField(upload_to=get_card_image_filename, default='review/default/review_default.png')
    date_creation = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_creation']
    
    def average_score(self):
        final_score = self.final_score.all()
        return round(sum(p.score for p in final_score) / len(final_score), 2) if final_score else 0
    
    def __str__(self):
        return f"{self.title} ({self.score})"
