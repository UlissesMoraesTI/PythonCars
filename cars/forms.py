from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    year_factory = forms.IntegerField()
    year_model = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    price = forms.FloatField()    
    photo = forms.ImageField()
 
    def save(self):        
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            year_factory = self.cleaned_data['year_factory'],
            year_model = self.cleaned_data['year_model'],
            plate = self.cleaned_data['plate'],
            price = self.cleaned_data['price'],
            photo = self.cleaned_data['photo']
        )
        car.save()
        return car 
