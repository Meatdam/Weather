from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.common import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    """
    Класс для работы с формой "UserLoginForm"
    Отображение полей при логине пользователя и админ панели если пользователь
    является суперпользователем
    """
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'

    def get_success_url(self):
        return reverse_lazy('weather:weather')


class UserRegistrationCreateView(TitleMixin, CreateView):
    """
    Класс для работы с формой "UserRegistrationForm"
    Отображение полей при регистрации пользователя и админ панели если пользователь
    является суперпользователем
    """
    model = User
    form_class = UserRegistrationForm
    title = 'Регистрация'

    def form_valid(self, form):

        user = form.save()
        user.is_active = True
        user.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:login')


def logaut(request):
    """
    Функция вида logaut
    Отображение полей при регистрации пользователя и админ панели если пользователь
    является суперпользователем
    :return: HttpResponseRedirect(reverse('index'))
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))
