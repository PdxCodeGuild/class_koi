from django.forms import ModelForm, TextInput, Textarea, FileInput

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text_content','image_content']
        widgets = {
            'text_content': TextInput(attrs={
                'class': '',
                'placeholder': 'Enter New Boop',
            }),
            'image_content': FileInput(attrs={
                'class': '',
            })
        }