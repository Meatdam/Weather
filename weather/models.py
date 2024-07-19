from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class WeatherModel(models.Model):
    """
    Модель для хранения информации о погоде
    """
    city = models.CharField(max_length=100, verbose_name='Город')
    temperature = models.FloatField(verbose_name='Температура', **NULLABLE)
    icon = models.CharField(max_length=20, verbose_name='Иконка погоды', **NULLABLE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Погода'
        verbose_name_plural = 'Погода'
