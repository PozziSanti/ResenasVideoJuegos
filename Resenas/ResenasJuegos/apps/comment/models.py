from django.db import models
from django.contrib.auth.models import User
from apps.score.models import Score
import uuid

#MODELO COMENTARIO
class Comment(models.Model):
    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    #FOREIGN KEYS
    review = models.ForeignKey('review.Review', on_delete=models.CASCADE, related_name='comment') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE, related_name='comment') 
    
    #ATRIBUTOS
    content = models.TextField()
    approbed = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comentario de {self.user.username} en {self.review.title[:30]}'