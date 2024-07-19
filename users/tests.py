from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationView(TestCase):
    """
    Класс для тестирования регистрации пользователей.
    """

    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'horoshii',
            'password2': 'horoshii'}

    def test_user_registration_get(self):
        """
        Проверяет отображение страницы регистрации при GET запросе.
        """
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertTemplateNotUsed(response, 'registration')

    def test_user_registration_post_success(self):
        """
        Проверяет успешную регистрацию пользователя.
        Проверяет, что после регистрации пользователь авторизован и его данные сохранены в БД.
        """
        first_name = self.data['first_name']
        self.assertFalse(User.objects.filter(first_name=first_name).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(first_name=first_name).exists())

    def test_user_registration_post_error(self):
        """
        Проверяет ошибку при попытке регистрации пользователя с уже существующим email.
        Проверяет, что при попытке регистрации пользователя с таким email возникает соответствующее сообщение об ошибке.
        """
        User.objects.create(email=self.data['email'])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким Email уже существует.')
