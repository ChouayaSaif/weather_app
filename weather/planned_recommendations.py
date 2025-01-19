from .models import Place
from weather.planned_weather_api import get_planned_weather_data

def planned_recommendations(city="Tunis", days_ahead=1):
    weather =  get_planned_weather_data(city, days_ahead)

    # Debugging 11: checking if weather_data has value
    print(f'weather in x days: {weather}')

    if not weather:
        return "No forecast available in next {days_ahead} days."
    
    condition = weather['condition']
    print(f'condition of the weather in x days: {condition}')

    # Generate recommendations based on the weather
    planned_recommendations = Place.objects.filter(weather_type__icontains=weather['condition'])
    recommendations = Place.objects.filter(weather_type__icontains=weather['condition'])


    print(f"planned_R: {planned_recommendations}")
    

    return planned_recommendations