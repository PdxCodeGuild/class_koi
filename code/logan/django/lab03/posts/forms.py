from django.forms import ModelForm
from django import forms
from.models import Chirp

from django.contrib.auth.models import User

# class LoginForm(ModelForm):
#     """
#     I'm not actually using this, but I made it so it's staying.
#     """
#     class Meta:
#         model = User
#         fields = [ 'username', 'password']

class ChirpForm(ModelForm):
    class Meta:
        model = Chirp
        fields = ['content']
