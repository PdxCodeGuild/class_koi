from django import forms
from django.forms import ModelForm

from .models import Author, Book, CheckOut

class CheckOutForm(ModelForm):
    class Meta:
        model = CheckOut
        fields = ['checkout'] 