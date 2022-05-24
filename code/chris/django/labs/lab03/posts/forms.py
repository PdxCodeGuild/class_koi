from django import forms
from django.forms import ModelForm
from django import forms


from .models import Posts

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control mx-3'
            }),
            'name': 'Chirp',
        }