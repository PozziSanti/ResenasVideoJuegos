from django.db import models

# Create your models here.

class Category(models.Model): #Crea tabla Category en base de datos
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]

    def __str__(self):
        return self.name