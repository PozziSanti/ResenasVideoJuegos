from django import forms
from .models import Post
from .models import Post, PostImage
from django.forms import inlineformset_factory


# Formulario para crear o editar imágenes de un post
ImagesFormSet = inlineformset_factory(
    Post, 
    PostImage, 
    fields=['image'], 
    extra=1, 
    can_delete=True
)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']
        fields = ['title', 'content', 'category'] 

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.images = ImagesFormSet(
            self.request.POST or None,
            self.request.FILES or None,
            instance=self.instance
        )
    def is_valid(self):
        return super().is_valid() and self.images.is_valid()
    
    def save(self, commit=True):
        post = super().save(commit)
        self.images.instance = post
        self.images.save()
        return post 

