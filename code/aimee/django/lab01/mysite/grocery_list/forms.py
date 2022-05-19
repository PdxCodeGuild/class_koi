from django import forms
from django.forms import ModelForm
from .models import GroceryItem

class AddItem(forms.Form):
    add_item = forms.CharField(label='Enter an item...', max_length=50)
    
class GroceryItemForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['description']