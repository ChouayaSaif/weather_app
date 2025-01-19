from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import WeatherDataAPIView, ChatbotAPIView, PlannedRecommendationsAPIView, UserPreferencesAPIView, DailyRecommendationsAPIView, UpdateUserPreferences


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Version 1.0
    path('api/v1/Weather-Information/<str:location>/', WeatherDataAPIView.as_view(), name='weather-data-api'),
    path('api/v1/Chatbot/<str:message>/', ChatbotAPIView.as_view(), name='chatbot-api'),
    path('api/v1/Planned-Recommendations/<str:location>/<int:days_ahead>/', PlannedRecommendationsAPIView.as_view(), name='planned-recommendations-api'),
    path('api/v1/User-Preferences/preferences/', UserPreferencesAPIView.as_view(), name='user-preferences'),
    path('api/v1/Daily-Recommendations/<str:location_name>/', DailyRecommendationsAPIView.as_view(), name='daily-recommendations'),
    path('api/v1/Update-Preferences/<str:field>/<str:value>/', UpdateUserPreferences.as_view(), name='update-user-preferences'),
]
