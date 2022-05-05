from django.forms import ModelForm
from django import forms

from .models import NutritionFacts

class NutritionFactsForm(ModelForm):
    class Meta:
        model = NutritionFacts
        # fields = '__all__' will give you all the non-auto fields (won't include the id)
        fields = '__all__'
        # setting fields to a list or tuple of strings of the field names will ony show those fields
        # fields = ['fat', 'protein', 'name']
        widgets = {
            # these widgets are being used to apply the tailwind classes to the inputs
            'name': forms.TextInput(attrs={
                'class': 'border-black border-2 rounded-md mr-4 my-2'
            }),
            'serving_size': forms.NumberInput(attrs={
                'class': 'border-black border-2 rounded-md mr-4 my-2'
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'border-black border-2 rounded-md mr-4 my-2'
            }),
            'fat': forms.NumberInput(attrs={
                'class': 'border-black border-2 rounded-md mr-4 my-2'
            }),
            'carbs': forms.NumberInput(attrs={
                'class': 'border-black border-2 rounded-md mr-4 my-2'
            }),
            'protein': forms.NumberInput(attrs={
                'class': 'border-black border-2 rounded-md mr-4 my-2'
            }),
            'image': forms.FileInput(attrs={
                'class': 'border-black border-2 rounded-md mr-4 my-2'
            }),
        }