from django.forms import ModelForm, TextInput

from weather.models import WeatherModel


class CityForm(ModelForm):
    """
    Класс для работы с формой "CityForm"
    """
    class Meta:
        model = WeatherModel
        fields = ('city',)
        widgets = {
            'city': TextInput(attrs={'class': 'form-control',
                                     'city': 'city',
                                     'id': 'city',
                                     'placeholder': 'Введите название города',
                                     })}
