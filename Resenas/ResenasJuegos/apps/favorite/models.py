from django.db import models
from django.contrib.auth.models import User
from .models import Review


# MODELO FAVORITOS

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='favorite')
    saved_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'review')

    def __str__(self):
        return f'{self.user.username} marcó como favorito {self.review.title}'