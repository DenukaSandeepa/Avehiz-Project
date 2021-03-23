from django import forms
from .models import publishing

class CreateAdForm(forms.ModelForm):
    class Meta:
        model = publishing
        fields = (
        'title',
        'type',
        'brand',
        'model',
        'category',
        'year',
        'transmission',
        'milage',
        'fuel',
        'engine',
        'image1',
        'image2',
        'image3',
        'image4',
        'image5',
        'description',
        'condition',
        'price',
        'tel',
        'city',
        'address',
        )

        
