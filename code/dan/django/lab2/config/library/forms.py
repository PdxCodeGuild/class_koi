from django import forms
from django.forms import ModelForm
import datetime
from .models import Checkinout, Book

class Checkinoutform(ModelForm):
    class Meta:
        model = Checkinout
        fields='__all__'
        
        
class Addbookform(ModelForm):
    class Meta:
        model = Book
        fields='__all__'


     


