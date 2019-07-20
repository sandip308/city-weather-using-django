from django.shortcuts import render,redirect
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=YOUR API KEY'
    get_city = City.objects.all()
    err = ''
    message = ''
    message_style = ''
    if request.method =="POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            city_count=City.objects.filter(name=new_city).count()
            if city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err = 'City Not Found'
            else:
                err = 'Already Exist, First Delete And Try Again'
        if err:
            message = err
            message_style = 'danger'
        else:
            message = 'City Added Successfully'
            message_style = 'success'
    form = CityForm()
    weather_city = []
    for city in get_city:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temparature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_city.append(city_weather)
    context = {'weather':weather_city,'form':form,'message':message,'message_style':message_style}
    return render(request,'weather/Weather.html',context)


def delete_data(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('index')
