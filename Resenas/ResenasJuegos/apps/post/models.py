from django.db import models
from django.utils.text import slugify
from django.conf import settings
import uuid
import os

# MODELO CATEGORIAS (RPG, ACCION, AVENTURA, etc.)
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["title"]

    def __str__(self):
        return self.title

<<<<<<< HEAD
# MODELO PLATAFORMAS (PS5, XBOX, PC, etc.)
class Platform(models.Model):
    title = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

=======
>>>>>>> 3384dd51d7d8579605fed650bc8fd9a56ff7f343
# MODELO POSTS
class Post(models.Model):
    #PRIMARY KEY
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #FOREIGN KEYS
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #hay que cambiar el 'auth.User' porque no esta definido en config.
    category = models.ManyToManyField(Category, related_name="post")

    #ATTRIBUTOS
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    @property #CANTIDAD DE COMENTARIOS
    def amaount_comments(self):
        return self.comment.count()
    
    @property #CANTIDAD DE FAVORITOS
    def amount_favorites(self):
        return self.favorite.count()
    
    @property #CALIFICACION PROMEDIO
    def average_score(self):
        all_scores = self.comment.all()
        if all_scores.exists():
            return round(sum(s.score for s in all_scores) / all_scores.count(), 2)
        else: 
            return 0
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()

        super().save(*args, **kwargs)

        if not self.image.exists():
            PostImage.objects.create(post=self, image='post/default/post_default.png')
    
    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1

        return unique_slug


def get_image_path(instance, filename):
    post_id = instance.post.id
    images_count = instance.post.images.count()
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f"post_{post_id}_image_{images_count + 1}{file_extension}"
    
    return os.path.join('post/cover/', new_filename) #Ruta a donde se guardaran las imagenes (en media)

#MODELO POSTS IMAGE
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_path)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Imagen de {self.post.id} ({self.image.name})"
    
