from django.db import models
import uuid

#MODELO CATEGORÍA
class Category(models.Model):
    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    #ATRIBUTOS
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=False)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]

    def __str__(self):
        return self.name


#MODELO PLATAFORMAS   
class Plataform(models.Model): 
    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    #ATRIBUTOS
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ["name"]

    def __str__(self):
        return self.name

