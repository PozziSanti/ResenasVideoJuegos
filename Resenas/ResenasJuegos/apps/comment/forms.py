from django import forms
from apps.comment.models import Comment

#CLASE HACER UN COMENTARIO
class CommentForm(forms.ModelForm): #TOMA EL MODELO COMMENT DE REFERENCIA PARA USARLO EN COMMENTFORM
    class Meta:
        model = Comment
        fields = ['content', 'score']
    
    widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
            'score': forms.Select(choices=[(i, f'{i} estrellas') for i in range(1, 6)]),
        }