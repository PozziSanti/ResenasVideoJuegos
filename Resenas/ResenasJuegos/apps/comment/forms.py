from django import forms
from apps.comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'score']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escribí tu reseña acá...',
                'class': 'w-full border rounded p-2'
            }),
            'score': forms.Select(attrs={
                'class': 'bg-[#130C2A] text-[#f0f1f4] border border-[#241D44] rounded-lg p-5  text-base focus:outline-none focus:ring-2 focus:ring-[#4F46E5] appearance-none',
                'style': 'background-image: none !important; min-height: 40px;'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].choices = [
            (1, '1'),
            (2, '2'), 
            (3, '3'),
            (4, '4'),
            (5, '5')
        ]