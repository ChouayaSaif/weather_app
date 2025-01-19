from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import UserPreferences, Place
from .views import (
    WeatherDataAPIView,
    ChatbotAPIView,
    PlannedRecommendationsAPIView,
    UserPreferencesAPIView,
    DailyRecommendationsAPIView,
    UpdateUserPreferences,
)
from weather.weather_api import get_weather_data
from weather.daily_recommendations import daily_recommendations
from weather.planned_recommendations import planned_recommendations
from weather.chatbot import ask_chatbot

# testing your Django REST API functions, you can use Django's built-in testing framework along with the unittest module
# Create your tests here.
class WeatherDataAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.factory = RequestFactory()

    def test_get_weather_data(self):
        request = self.factory.get('/api/weather/manouba/')
        request.user = self.user
        response = WeatherDataAPIView.as_view()(request, location='manouba')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('temperature', response.data)

class ChatbotAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.factory = RequestFactory()

    def test_post_chatbot_message(self):
        request = self.factory.post('/api/chatbot/', {'message': 'Hello'}, content_type='application/json')
        request.user = self.user
        response = ChatbotAPIView.as_view()(request, message='Hello')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('response', response.data)

class PlannedRecommendationsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.factory = RequestFactory()

    def test_post_planned_recommendations(self):
        request = self.factory.post('/api/planned-recommendations/', {'location': 'manouba', 'days_ahead': 3}, content_type='application/json')
        request.user = self.user
        response = PlannedRecommendationsAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('planned_recommendations', response.data)

class UserPreferencesAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.factory = RequestFactory()
        self.preferences = UserPreferences.objects.create(user=self.user, default_location='manouba', favorite_locations=['manouba', 'tunis'])

    def test_get_user_preferences(self):
        request = self.factory.get('/api/user-preferences/')
        request.user = self.user
        response = UserPreferencesAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('default_location', response.data)
        self.assertIn('favorite_locations', response.data)

class DailyRecommendationsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.factory = RequestFactory()

    def test_get_daily_recommendations(self):
        request = self.factory.get('/api/daily-recommendations/manouba/')
        request.user = self.user
        response = DailyRecommendationsAPIView.as_view()(request, location_name='manouba')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

class UpdateUserPreferencesAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.factory = RequestFactory()
        self.preferences = UserPreferences.objects.create(user=self.user, default_location='manouba', favorite_locations=['manouba', 'tunis'])

    def test_update_user_preferences(self):
        request = self.factory.put('/api/update-preferences/default_location/tunis/')
        request.user = self.user
        response = UpdateUserPreferences.as_view()(request, field='default_location', value='tunis')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'default_location updated successfully')
        self.preferences.refresh_from_db()
        self.assertEqual(self.preferences.default_location, 'tunis')