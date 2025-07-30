from django import forms
from apps.comment.models import Comment

#CLASE HACER UN COMENTARIO
class CommentForm(forms.ModelForm): #TOMA EL MODELO COMMENT DE REFERENCIA PARA USARLO EN COMMENTFORM
    class Meta:
        model = Comment
        fields = ['content']
    
    widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
        }