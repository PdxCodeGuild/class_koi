from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Author, Book

class CheckOutForm(forms.ModelForm):
    user = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Enter User Name'}))
    class Meta:
        model = Book
        fields = ['user']