from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Item

class ItemForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Add grocery item here...'}))
    class Meta:
        model = Item
        fields = ['content']


class DateInput(forms.DateInput):
    input_type = 'date'

class UpdateForm(forms.ModelForm):
    content = forms.CharField(label='Update Entry')
    class Meta:
        model = Item
        # fields = '__all__'
        fields = ['content']
        widgets = {
            'date_completed': DateInput(),
        }


class CompleteForm(forms.ModelForm):
    content = forms.CharField(label='')
    class Meta:
        model = Item
        # fields = '__all__'
        fields = ['complete']
        widgets = {
            'date_completed': DateInput(),
        }