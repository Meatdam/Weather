from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Класс для работы с административной панелью для модели "User"
    """
    list_display = ('email', 'is_active', 'is_staff', 'date_joined')
