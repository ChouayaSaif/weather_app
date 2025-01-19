from rest_framework import serializers
from .models import UserPreferences, Place

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = '__all__'

# Django's response object tries to return an instance of a class (in this case, Place) that cannot be automatically converted to JSON
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
