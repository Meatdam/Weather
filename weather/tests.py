from django.urls import reverse
from rest_framework import status

from users.models import User
from weather.models import WeatherModel
from rest_framework.test import APITestCase


class HabitsTestCase(APITestCase):
    """
    Тестирование создания, изменения и получения привычки
    """
    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.weather = WeatherModel.objects.create(owner=self.user, city="test", temperature="20", icon="test")
        self.client.force_authenticate(user=self.user)

    def test_weather_list(self):
        """
        Тест получения списка привычек
        """
        url = reverse('weather:list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'id': 1,
                               'city': 'test',
                               'temperature': 20.0,
                               'icon': 'test',
                               'owner': 3}]}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_weather_retrieve(self):
        """
        Тест получения одной привычки
        """
        url = reverse('weather:detail', args=(self.weather.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('city', 'temperature'), 'test', '20.0')
