from django.db import models
from django.contrib.auth.models import User
from .models import Review

#MODELO COMENTARIO
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='') #TODO Definir comentario en review.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    approbed = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.user.username} en {self.review.title[:30]}'