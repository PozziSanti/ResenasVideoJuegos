from django import forms
from .models import Post, PostImage, Category
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
        fields = ['title', 'content', 'category']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.all()
        
        prefix = "images"
        # Solo pasar POST/FIles si existe request
        if request:
            self.images = ImagesFormSet(
                request.POST or None,
                request.FILES or None,
                instance=instance,
                prefix=prefix,
            )
        else:
            # Para GET
            self.images = ImagesFormSet(
                instance=instance,
                prefix=prefix,
            )
        
    def is_valid(self):
        ok_main = super().is_valid()
        ok_imgs = self.images.is_valid()
        return ok_main and ok_imgs
    
    def save(self, commit=True):
        post = super().save(commit=commit)
        self.images.instance = post
        self.images.save()
        return post 
