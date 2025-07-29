from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from apps.clasification.models import Category
from apps.clasification.models import Plataform
from apps.comment.models import Comment
import uuid
import os
   

#MODELO POSTS 
class Review(models.Model): #TODO Modelos incompleto, falta realcionar score #TODO Hay que hacer una view/formulario que nos permita cargar las reseñas
    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    #FOREIGN KEYS
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='review')
    plataform = models.ForeignKey(Plataform, on_delete=models.SET_NULL, null=True, related_name='review')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='review', null=True, blank=True)
    
    #ATRIBUTOS
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    content = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(default=True)
    class Meta:
        ordering = ['-date_creation']
    
    def average_score(self):
        final_score = self.final_score.all()
        return round(sum(p.score for p in final_score) / len(final_score), 2) if final_score else 0
    
    
    @property
    def ammount_comments(self):
        return self.comment.count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1

        while Review.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{counter}"
            counter += 1

        return unique_slug

    def __str__(self):
        return f"{self.title} ({self.score})" 

def get_image_path(instance, filename):
    review_id = instance.review.id
    images_count = ReviewImage.review.images.count()
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f"review_{review_id}_image_{images_count + 1}{file_extension}"
    
    return os.path.join('review/cover/', new_filename)

#MODELO POSTS IMAGE
class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_path)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Imagen de {self.review.title} ({self.image.name})"