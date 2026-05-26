from django import forms
from cars.models import Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    year_factory = forms.IntegerField()
    year_model = forms.IntegerField()
    price = forms.FloatField()
    plate = forms.CharField(max_length=10)
    photo = forms.ImageField()







    year = forms.IntegerField(label='Year')
    image = forms.ImageField(label='Image')
    make = forms.CharField(label='Make', max_length=100)
    
