from django.forms import ModelForm, Textarea, FileInput

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = '__all__' # change to remove author, add request.user to POST in views
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

'''
assign form to variable in views.py (e.g. forms = PostForm())
pass variable through context
call in html as 
{{ variable.as_p }} (as_p method adds <p> tags)
add if request.method == 'POST': to views.py
'''