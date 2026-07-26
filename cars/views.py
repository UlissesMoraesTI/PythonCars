from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import CarModelForm #ModelForm
#from cars.forms import CarForm
from django.views import View


def cars_view(request):
    search = request.GET.get('search')
    
    cars = Car.objects.all().order_by('-model')    
    #cars = Car.objects.filter(brand__name = 'HARLEY')
    #cars  = Car.objects.filter(model__contains = 'ULTRA')     
    if search:
        cars  = Car.objects.filter(model__icontains=search).order_by('-model') 
 
    return render(
        request,
        'cars.html',
        {'cars': cars}

    )
class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('-model')    
        return render(
            request,
            'cars.html',
            {'cars': cars}
        )

def new_car_view(request):
    if request.method == 'POST':
        #new_car_form = CarForm(request.POST, request.FILES)
        new_car_form = CarModelForm(request.POST, request.FILES) #ModelForm
        #print(new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()            
            return redirect('cars_list')            
    else:
       #new_car_form = CarForm()
        new_car_form = CarModelForm() #ModelForm
    return render(request, 'new_car.html', {'new_car_form': new_car_form} )

class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm() #ModelForm
        return render(request, 'new_car.html', {'new_car_form': new_car_form} )
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES) #ModelForm
        if new_car_form.is_valid():
            new_car_form.save()            
            return redirect('cars_list')            
        return render(request, 'new_car.html', {'new_car_form': new_car_form} )