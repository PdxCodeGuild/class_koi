from django.forms import ModelForm, Textarea, FileInput

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text_content','image_content']
        widgets = {
            'text_content': Textarea(attrs={
                'class': '',
                'placeholder': '',
            }),
            'image_content': FileInput(attrs={
                'class': '',
            })
        }