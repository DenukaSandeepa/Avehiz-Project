from django import forms
from .models import publishing
from django.utils.translation import ugettext_lazy as _

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
        'location',
        'location_lat',
        'location_lon',
        )

        widgets = {
        'title':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the Ad title..... e.g- Used Prado for Sale"}),
        'description':forms.Textarea(attrs={"placeholder": "Vehicle description means a description of a vehicle including at a minimum the license information, issuing state, make, model, year, color, body style, and vehicle identification number (VIN)....."}),
        'type':forms.Select(attrs={"class":"form-control"}),
        'brand':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the correct model...... e.g-Toyota"}),
        'model':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the correct model...... e.g-Prado"}),
        'category':forms.Select(attrs={"class":"form-control"}),
        'year':forms.NumberInput(attrs={"class":"form-control","placeholder":"Without spaces or any symbols or latters"}),
        'transmission':forms.Select(attrs={"class":"form-control"}),
        'milage':forms.NumberInput(attrs={"class":"form-control","placeholder":"Without spaces or any symbols or latters"}),
        'fuel':forms.Select(attrs={"class":"form-control"}),
        'engine':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the correct engine details... e.g-V8 4000cc"}),
        'condition':forms.Select(attrs={"class":"form-control"}),
        'price':forms.NumberInput(attrs={"class":"form-control","placeholder":"Without spaces or any symbols or latters"}),
        'tel':forms.TextInput(attrs={"class":"form-control","placeholder":"Without any symbols or latters"}),
        'city':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the nearest city"}),
        'address':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the address"}),
        }

        labels = {
            'title': _('Ad Title'),
            'type': _('Vehicle Type'),
            'brand': _('Vehicle Brand'),
            'model': _('Vehicle Model'),
            'category': _('Vehicle Category'),
            'year': _('Manufacture Year'),
            'transmission': _('Vehicle Transmission Type'),
            'milage': _('Milage of the Vehicle'),
            'fuel': _('Fuel Type'),
            'engine': _('Engine Model and Capacity'),
            'image1': _('Ad Main Image'),
            'image2': _('Ad Image 1'),
            'image3': _('Ad Image 2'),
            'image4': _('Ad Image 3'),
            'image5': _('Ad Image 4'),
            'description': _('Description About the Vehicle'),
            'condition': _('Ad Title'),
            'price': _('Your Price for the Vehicle'),
            'tel': _('Your Telephone Number'),
            'city': _('Nearest City'),
            'address': _('Adress'),
        }
