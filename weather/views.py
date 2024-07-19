import os
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from users.common import TitleMixin
from weather.forms import CityForm

from weather.models import WeatherModel


@login_required
def index(request):
    """
    Главная страница приложения
    """

    apy_key = os.getenv('API_KEY')
    if request.method == 'POST':
        result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={request.POST.get('city')}"
                              f"&units=metric&appid={apy_key}").json()
        res = WeatherModel.objects.create(owner=request.user, city=request.POST.get('city'),
                                          temperature=result['main']['temp'], icon=result['weather'][0]['icon'])
        res.save()

    form = CityForm()

    cities = WeatherModel.objects.all()

    context = {
        'all_info': cities,
        'form': form,

    }
    return render(request, 'weather/index.html', context, )


class WeatherDeleteView(DeleteView, TitleMixin):
    """
    Класс для удаления погодных данных города
    """
    model = WeatherModel
    title = 'Удаление города'

    def get_success_url(self):
        return reverse_lazy('weather:weather')
