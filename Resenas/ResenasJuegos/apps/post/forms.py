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


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'allow_comments')

    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        self.active_images = kwargs.pop('active_images', None)
        # self.category = Category.objects.all()

        super(UpdatePostForm, self).__init__(*args, **kwargs)

        if self.active_images:
            for image in self.active_images:
                # keep_image_1, keep_image_2...
                field_name = f"keep_image_{image.id}"
                self.fields[field_name] = forms.BooleanField(
                    required=False, initial=True, label=f"Mantener {image}"
                )

    def save(self, commit=True):
        post = super().save(commit=False)
        image = self.cleaned_data['image']

        if commit:
            post.save()

            if image:
                PostImage.objects.create(post=post, image=image)
            
            if self.active_images:
                for image in self.active_images:
                    if not self.cleaned_data.get(f"keep_image_{image.id}", True):
                        image.delete()
        return post