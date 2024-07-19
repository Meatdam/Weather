from rest_framework import serializers

from weather.models import WeatherModel


class WeatherSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habits
    """
    class Meta:
        model = WeatherModel
        fields = '__all__'
