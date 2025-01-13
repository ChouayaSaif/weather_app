import requests
from datetime import datetime, timedelta

API_KEY = "7613c6caddbac6c8549b60a388f6b45c"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
GEOCODING_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_coordinates(city_name):
    """
    Get the latitude and longitude for a given city name using the OpenWeatherMap Geocoding API.
    """
    response = requests.get(GEOCODING_URL, params={
        'q': city_name,
        'appid': API_KEY
    })
    
    if response.status_code != 200:
        raise Exception(f"Error fetching location data: {response.status_code}")
    
    data = response.json()
    if 'coord' not in data:
        raise Exception("City not found")
    
    return data['coord']['lat'], data['coord']['lon']

def get_planned_weather_data(city_name, days_ahead):
    # Convert days_ahead to an integer (if it's a string)
    try:
        days_ahead = int(days_ahead)
    except ValueError:
        raise ValueError("Days ahead must be an integer.")
    
    if days_ahead < 1 or days_ahead > 6:
        raise ValueError("Days ahead must be between 1 and 6")
    lat, lon = get_coordinates(city_name)
    
    if lat is None or lon is None:
        raise ValueError(f"Coordinates for {city_name} not found.")

    # Send the request to the OpenWeatherMap API for 5-day forecast
    response = requests.get(
        BASE_URL,
        params={
            'lat': lat,
            'lon': lon,
            'exclude': 'current,minutely,hourly',  # Exclude unnecessary data
            'appid': API_KEY,
            'units': 'metric',  # Use metric for Celsius
        }
    )

    if response.status_code != 200:
        raise Exception(f"Error fetching data from OpenWeatherMap: {response.status_code}")
    
    data = response.json()

    # Debugging: print the entire response to inspect the data
    # print(data)

    # Convert the target day to the correct datetime format
    current_time = datetime.now()
    target_time = current_time + timedelta(days=days_ahead)

    # Find the forecast data for the target day
    for entry in data['list']:
        # Convert the timestamp to datetime object for comparison
        forecast_time = datetime.utcfromtimestamp(entry['dt'])

        # We check if the forecast corresponds to the target date (ignoring time)
        if forecast_time.date() == target_time.date():
            forecast = {
                'date': forecast_time.strftime('%Y-%m-%d'),
                'temperature': entry['main']['temp'],
                'condition': entry['weather'][0]['description'],
                'humidity': entry['main']['humidity'],
                'wind_speed': entry['wind']['speed'],
            }
            return forecast

    # If no forecast found for the target date, return None
    return None         

# Example usage:
city_name = "Tokyo"
forecast = get_planned_weather_data(city_name, 2)  
# Get the weather for 2 days ahead
print(forecast)

# response
# {
#     'date': '2024-12-31',
#     'temperature': 15.6,
#     'weather': 'light rain',
#     'humidity': 78,
#     'wind_speed': 5.2
# }
