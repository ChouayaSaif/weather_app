from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import WeatherDataAPIView, ChatbotAPIView, PlannedRecommendationsAPIView


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/weather/<str:location>/', WeatherDataAPIView.as_view(), name='weather-data-api'),
    path('api/chatbot/', ChatbotAPIView.as_view(), name='chatbot-api'),
    path('api/planned-recommendations/', PlannedRecommendationsAPIView.as_view(), name='planned-recommendations-api'),
]
