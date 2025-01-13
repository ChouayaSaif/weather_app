from django.db import models
from django.contrib.auth.models import User


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_location = models.CharField(max_length=255, blank=True, null=True)
    favorite_locations = models.JSONField(default=list)  # Stores a list of favorite locations
    language = models.CharField(max_length=10, choices=[('en', 'English'), ('fr', 'French')], default='en')
    temperature_units = models.CharField(max_length=10, choices=[('Celsius', 'Celsius'), ('Fahrenheit', 'Fahrenheit')], default='Celsius')
    alert_temp_over_35 = models.BooleanField(default=False)
    alert_rain = models.BooleanField(default=False)

    def __str__(self):
        return f"Preferences for {self.user.username}"




class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    weather_type = models.CharField(max_length=50)  # e.g., Sunny, Rainy, Cool
    description = models.TextField()

    def __str__(self):
        return self.name
