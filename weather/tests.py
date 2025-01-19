from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from rest_framework.test import APIClient, force_authenticate
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
import json


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

    def test_get_weather_data_invalid_location(self):
        request = self.factory.get('/api/weather/invalid_location/')
        request.user = self.user
        response = WeatherDataAPIView.as_view()(request, location='invalid_location')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)




class ChatbotAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.factory = RequestFactory()

    def test_post_chatbot_message(self):
        # Create a POST request with a JSON payload
        data = {'message': 'Hello'}
        request = self.factory.post(
            '/api/chatbot/',
            data=json.dumps(data),
            content_type='application/json'
        )

        # Authenticate the request with the test user
        force_authenticate(request, user=self.user)

        # Call the view directly, passing the 'message' argument
        response = ChatbotAPIView.as_view()(request, message='Hello')

        # Check the response status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "Hello. It's nice to meet you. Is there something I can help you with or would you like to chat?")




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
    def test_get_user_preferences_not_found(self):
        # Test missing user preferences
        self.preferences.delete()  # Delete the user preferences
        request = self.factory.get('/api/user-preferences/')
        request.user = self.user
        response = UserPreferencesAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)  # Ensure the response contains an error message




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
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        self.factory = RequestFactory()
        self.preferences = UserPreferences.objects.create(user=self.user, default_location='manouba', favorite_locations=['manouba', 'tunis'])

    def test_update_user_preferences_valid_field(self):
        # Test updating a valid field (default_location)
        request = self.factory.put('/api/update-preferences/default_location/tunis/')
        force_authenticate(request, user=self.user)  # Authenticate the request
        response = UpdateUserPreferences.as_view()(request, field='default_location', value='tunis')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'default_location updated successfully')
        self.preferences.refresh_from_db()
        self.assertEqual(self.preferences.default_location, 'tunis')