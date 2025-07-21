from django.db import models
from django.contrib.auth.models import User
from .models import Review

#MODELO CALIFICACION
class Score(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='score') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Del 1 al 5
    class Meta:
        unique_together = ('review', 'user') 
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'

    def __str__(self):
        return f'Calificación {self.score} de {self.user.username} para {self.review.title[:30]}'