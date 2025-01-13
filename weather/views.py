from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserPreferences, Place
from weather.weather_api import get_weather_data
from weather.daily_recommendations import daily_recommendations
from weather.planned_recommendations import planned_recommendations
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from weather.chatbot import ask_chatbot
import json

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):

    # Debugging 1: trying to assign the default_location to location_name variable
    try:
        preferences = UserPreferences.objects.get(user=request.user)
        default_location_value = preferences.default_location
        print(default_location_value)
    except UserPreferences.DoesNotExist:
        # Case where preferences do not exist for the user
        default_location_value = None
        print("No preferences found.")

    location_mapping = {
        'manouba': '106982',
        'kairouan': '106968',
        'tunis': '107039',
        'Ariana': '107039',
        'Béja': '106930',
        'BenArous': '106920',
        'Bizerte': '106926',
        'Gabès': '106952',
        'Gafsa': '106954',
        'Jendouba': '106930',
        'Kasserine': '106930',
        'Kebili': '106970',
        'Kef': '106957',
        'Mahdia': '106980',
        'Medenine': '106985',
        'Monastir': '106997',
        'Nabeul': '106926',
        'Sfax': '107019',
        'Sidi_Bouzid': '107024',
        'Siliana': '107026',
        'Sousse': '107029',
        'Tataouine': '107034',
        'Tozeur': '107038',
        'Zaghouan': '107040'
    }

    coordinates_mapping = {
        'manouba': {'lat': 36.8081, 'lon': 10.0863},
        'kairouan': {'lat': 35.6781, 'lon': 10.0963},
        'tunis': {'lat': 36.8065, 'lon': 10.1815},
        'ariana': {'lat': 36.8665, 'lon': 10.1647},
        'béja': {'lat': 36.7256, 'lon': 9.1817},
        'benarous': {'lat': 36.7538, 'lon': 10.2261},
        'bizerte': {'lat': 37.2746, 'lon': 9.8739},
        'gabès': {'lat': 33.8815, 'lon': 10.0982},
        'gafsa': {'lat': 34.425, 'lon': 8.7842},
        'jendouba': {'lat': 36.5011, 'lon': 8.7793},
        'kasserine': {'lat': 35.1673, 'lon': 8.8288},
        'kebili': {'lat': 33.7058, 'lon': 8.969},
        'kef': {'lat': 36.1826, 'lon': 8.7143},
        'mahdia': {'lat': 35.5047, 'lon': 11.0622},
        'medenine': {'lat': 33.3549, 'lon': 10.5055},
        'monastir': {'lat': 35.7643, 'lon': 10.8113},
        'nabeul': {'lat': 36.4561, 'lon': 10.7377},
        'sfax': {'lat': 34.739, 'lon': 10.7603},
        'sidi_bouzid': {'lat': 35.0382, 'lon': 9.4845},
        'siliana': {'lat': 36.0844, 'lon': 9.3708},
        'sousse': {'lat': 35.8256, 'lon': 10.6369},
        'tataouine': {'lat': 32.9295, 'lon': 10.4518},
        'tozeur': {'lat': 33.9197, 'lon': 8.1335},
        'zaghouan': {'lat': 36.4025, 'lon': 10.1451},
    }

    # Widget configuration context
    location_name = request.POST.get('location', default_location_value if preferences else 'manouba').lower()  # Default to user-preferred location
    location_id = location_mapping.get(location_name, "106982")  # Default to 'manouba' if not found
    coordinates = coordinates_mapping.get(location_name, {'lat': 36.8081, 'lon': 10.0863})  # Default to 'manouba' coordinates


    language = "EN"
    unit_system = "METRIC"
    widget_type_1 = "aqiPollutant"
    widget_type_2 = "upcoming"
    widget_type_3 = "summary"
    widget_type_4 = "current6"
    skin = "light"


    

    # Debugging 3: checking if 'Tunis' exists in database
    print(Place.objects.filter(location__iexact="Tunis"))
    # Fetch daily recommendations based on location
    #daily_recommendations = daily_recommendations(location_name)


    # Filling last widget
    # Retrieve user preferences for the logged-in user
    user_preferences = UserPreferences.objects.get(user=request.user)
    
    # Access the favorite locations as a list of strings (no need to use .id since it's a list of strings)
    favorite_locations = user_preferences.favorite_locations  # It's already a list of strings

    # Debuggin 12: printing favorite_locations
    print(favorite_locations)

    # Split the string into individual locations by comma
    locations_list = favorite_locations[0].split(', ')
    print(locations_list)

    # Set variables for each location from the list
    location_name_1 = locations_list[0] if len(locations_list) > 0 else 'kairouan'
    location_name_2 = locations_list[1] if len(locations_list) > 1 else 'kairouan'
    location_name_3 = locations_list[2] if len(locations_list) > 2 else 'kairouan'
    location_name_4 = locations_list[3] if len(locations_list) > 3 else 'kairouan'
    location_name_5 = locations_list[4] if len(locations_list) > 4 else 'kairouan'

    # converting to id rather than names to solve the bug (debugging 13)
    location_id_1 = location_mapping.get(location_name_1, "106982")  # Default to 'manouba' if not found
    location_id_2 = location_mapping.get(location_name_2, "106982")
    location_id_3 = location_mapping.get(location_name_3, "106982")
    location_id_4 = location_mapping.get(location_name_4, "106982")
    location_id_5 = location_mapping.get(location_name_5, "106982")

    # Debugging 13: checking why it return location_id and not location_id_2 though have same value
    print(location_id == location_id_2)
    print(type(location_id))
    print(type(location_id_2))
    print(location_id)
    print(location_id_2)
    print(location_id.lower() == location_id_2.lower()) # --> Solved: i am using location_id rather than location_name
                                                        # I should use location_id to all varibles not names

    # Debugging to render all user preferred locations
    print(f'those are user preferred locations 1: {location_id_1}')
    print(f'those are user preferred locations 2: {location_id_2}')
    print(f'those are user preferred locations 3: {location_id_3}')
    print(f'those are user preferred locations 4: {location_id_4}')
    print(f'those are user preferred locations 5: {location_id_5}')

    print(type(location_id_1))
    # Initialize the context with widget configuration
    context = {
        "location_id": location_id,
        "location_id_1": location_id_1,
        "location_id_2": location_id_2,
        "location_id_3": location_id_3,
        "location_id_4": location_id_4,
        "location_id_5": location_id_5,
        "language": language,
        "unit_system": unit_system,
        "widget_type_1": widget_type_1,
        "widget_type_2": widget_type_2,
        "widget_type_3": widget_type_3,
        "widget_type_4" : widget_type_4,
        "skin": skin,
        "latitude": coordinates['lat'],
        "longitude": coordinates['lon'],
        "default_location": "", 
        "favorite_locations": [],  # Default to an empty list if no favorite locations are set
        "daily_recommendations": daily_recommendations
    }

    # Handle POST requests for both weather data and preferences update
    if request.method == 'POST':

        planned_recs = None
        if request.method == 'POST':
            # Retrieve 'days_ahead' from the POST data
            days_ahead = request.POST.get('days_ahead')
            if days_ahead and location_name:
                planned_recs = planned_recommendations(location_name, days_ahead)  # Make sure it's the function
                print(f"printing planned recommendations: {planned_recs}")
            context['planned_weather_data'] = planned_recs  # Pass the forecast data to the context
        
        if request.method == 'POST':
        # Check if it's an AJAX request (JSON)
            if request.headers.get('Content-Type') == 'application/json':
                user_message = request.body.decode('utf-8')  # Get the raw message from the request body
                print(f"this is user message:{user_message}")
                data = json.loads(user_message)  # Parse the JSON data
                message = data.get('message')  # Extract the message
                print(f"This is message: {message}")
                
                if message:
                    response = ask_chatbot(message)  # Get the chatbot response
                    return JsonResponse({'response': response})  # Send back the response as JSON
                else:
                    return JsonResponse({'response': 'No message provided'}, status=400)
        

        if 'location' in request.POST:
            # Get weather data for the selected location
            location = request.POST.get('location')
            weather_data = daily_recommendations(location)

            context['daily_recommendations'] = daily_recommendations

        elif 'defaultLocation' in request.POST:
            # Update user preferences
            default_location = request.POST.get('defaultLocation')
            favorite_locations = request.POST.getlist('favoriteLocations')  # Get as list
            language = request.POST.get('language')
            temperature_units = request.POST.get('temperatureUnits')
            alert_temp_over_35 = 'alertTempOver35' in request.POST
            alert_rain = 'alertRain' in request.POST

            preferences, created = UserPreferences.objects.get_or_create(user=request.user)
            preferences.default_location = default_location
            preferences.favorite_locations = favorite_locations  # Save favorite locations
            preferences.language = language
            preferences.temperature_units = temperature_units
            preferences.alert_temp_over_35 = alert_temp_over_35
            preferences.alert_rain = alert_rain
            preferences.save()

            context['message'] = 'Preferences updated successfully.'
            context['favorite_locations'] = favorite_locations  # Pass the updated favorite locations

    else:
        # Handle GET request: Display preferences and weather data if available
        preferences = UserPreferences.objects.filter(user=request.user).first()
        if preferences:
            context['preferences'] = preferences
            default_location = preferences.favorite_locations
            context['default_location'] = preferences.default_location 
            location = preferences.default_location
            favorite_locations = preferences.favorite_locations  # Get favorite locations from preferences
            context['favorite_locations'] = favorite_locations  # Add favorite locations to the context
            weather_data = get_weather_data(location)

            context['weather_data'] = weather_data

    return render(request, 'dashboard.html', context)

