from django.urls import path

from weather.apps import WeatherConfig
from weather.views import index, WeatherDeleteView

app_name = WeatherConfig.name

urlpatterns = [
    path('weather/', index, name='weather'),
    path('delete/<int:pk>/', WeatherDeleteView.as_view(), name='delete_weather'),
]
