from django.contrib import admin

from weather.models import WeatherModel


@admin.register(WeatherModel)
class WeatherModelAdmin(admin.ModelAdmin):
    list_display = ('city', 'owner')
