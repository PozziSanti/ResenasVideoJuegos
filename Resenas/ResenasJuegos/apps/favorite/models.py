from django.db import models
from django.contrib.auth.models import User


# MODELO FAVORITOS
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='favorite')
    saved_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.username} marcó como favorito {self.post.title}'