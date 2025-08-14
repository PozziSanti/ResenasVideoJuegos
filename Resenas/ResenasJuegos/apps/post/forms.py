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
        instance = kwargs.get('instance', None) #SE AGREGO**************
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.all() #SE AGREGO**************
        
        # Solo pasar POST/FIles si existe request
        if request:
            self.images = ImagesFormSet(
                request.POST or None,
                request.FILES or None,
                instance=instance
            )
        else:
            # Para GET
            self.images = ImagesFormSet(instance=instance) #SE MODIFICO**************
        
    def is_valid(self):
        return super().is_valid() and self.images.is_valid()
    
    def save(self, commit=True):
        post = super().save(commit=commit) #SE MODIFICO COMIIT**************
        if commit: #SE AGREGO**************
            self.images.instance = post
            self.images.save()
        return post 
