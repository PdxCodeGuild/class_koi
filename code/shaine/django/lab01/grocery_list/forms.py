from dataclasses import fields
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Add grocery item here...'}))
    class Meta:
        model = Item
        fields = ['content']

class UpdateForm(forms.ModelForm):
    content = forms.CharField(label='')
    class Meta:
        model = Item
        # fields = '__all__'
        fields = ['content', 'complete',]

