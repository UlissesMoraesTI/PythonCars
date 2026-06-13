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

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        # fields = ['model', 'brand', 'year_factory', 'year_model', 'plate', 'price', 'photo']    

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("O preço é obrigatório.")
        if price < 20000:
            raise forms.ValidationError("O preço deve ser maior ou igual a R$ 20.000.")
        return price          
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            raise forms.ValidationError("A foto é obrigatória.")
        return photo          