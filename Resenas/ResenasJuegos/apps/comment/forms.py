from django import forms
from apps.comment.models import Comment

#MUESTRA CAMPOS DE COMENTARIO Y PUNTUACION
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 
                  'score'
                ]
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Escribí tu reseña acá...',
                'class': 'w-full border rounded p-2'
            }),
            'score': forms.Select(attrs={'class': 'border rounded p-2'}),
        }
