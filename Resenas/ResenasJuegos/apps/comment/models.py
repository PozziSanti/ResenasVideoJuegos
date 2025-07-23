from django.db import models
from django.contrib.auth.models import User
from apps.review.models import Review
from apps.score.models import Score
import uuid

#MODELO COMENTARIO
class Comment(models.Model):
    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    #FOREIGN KEYS
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comment') #TODO Definir comentario en review.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE, related_name='comment') #TODO Definir a que va a estar asociado.
    
    #ATRIBUTOS
    content = models.TextField()
    approbed = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.user.username} en {self.review.title[:30]}'