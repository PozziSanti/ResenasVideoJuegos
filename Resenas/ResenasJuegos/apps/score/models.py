from django.db import models
from django.contrib.auth.models import User
from .models import Review
import uuid

#MODELO CALIFICACION
class Score(models.Model):
    #Variable Auxiliar para calcular score
    score_range = [(i, str(i)) for i in range(1, 6)] # Del 1 al 5

    #FOREIGN KEYS
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='score') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #ATRIBUTOS
    score = models.IntegerField(choices=score_range)
    class Meta:
        unique_together = ('review', 'user') 
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'

    def __str__(self):
        return f'{self.user.username} le ha dado {self.score}⭐ a "{self.review.title[:30]}"'