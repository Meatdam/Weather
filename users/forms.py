from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.common import StyleFormMixin
from users.models import User


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    """
    Класс для работы с формой "UserLoginForm"
    """
    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegistrationForm(StyleFormMixin, UserCreationForm):
    """
    Класс для работы с формой "UserRegistrationForm"
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
