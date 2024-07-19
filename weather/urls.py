from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from weather.apps import WeatherConfig
from weather.views import index, WeatherDeleteView, WeatherListAPIView, WeatherRetrieveAPIView

app_name = WeatherConfig.name

urlpatterns = [
    path('weather/', index, name='weather'),
    path('delete/<int:pk>/', WeatherDeleteView.as_view(), name='delete_weather'),
    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API
    path('list/', WeatherListAPIView.as_view(), name='list'),
    path('detail/<int:pk>', WeatherRetrieveAPIView.as_view(), name='detail'),

]
