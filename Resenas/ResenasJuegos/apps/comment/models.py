from django.db import models
from django.contrib.auth.models import User
import uuid

#MODELO COMENTARIO
class Comment(models.Model):
    #Variable Auxiliar para calcular score
    score_range = [(i, str(i)) for i in range(1, 6)] # Del 1 al 5

    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    #FOREIGN KEYS
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comment') 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    #ATRIBUTOS
    content = models.TextField()
    score = models.IntegerField(choices=score_range)
    approbed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comentario de {self.user.username}, calificación de {self.score}⭐ en {self.post.title[:30]}'