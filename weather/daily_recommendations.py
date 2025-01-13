import requests
from .models import Place
from weather.weather_api import get_weather_data

def daily_recommendations(city="Tunis"):
    weather = get_weather_data(city)

    # Debugging 5: checking whether the weather data is available
    print(weather)
    if not weather:
        return []
    
    # Debuggin 6: converting all weather_type to a format that do not contain spaces
    places = Place.objects.all()
    for place in places:
        place.weather_type = place.weather_type.strip().lower()
    print(places)

    # Debugging 7: Giving a value to weather_type --> it retured now a result
    # recommendations = Place.objects.filter(weather_type__icontains="clear sky")

    # Debugging 8: Comparing value of weather_type = 'clear sky' or not --> False: dismatch btw them
    print(weather=="clear sky")
    print(weather) # Found Bug: weather returns: {'city': 'Tunisia', 'temperature': 11.6, 'condition': 'clear sky', 'humidity': 58, 'wind_speed': 1.73, 'date_time': '2024-12-30 01:52:41'}
                   # or it should return : weather.condition


    # Match weather with places
    recommendations = Place.objects.filter(weather_type__icontains=weather['condition'])

    # Debugging 2: Check if recommendations are returned
    print(recommendations)

    

    return recommendations