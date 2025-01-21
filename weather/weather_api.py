import requests
from datetime import datetime

# OpenWeatherMap API Key
API_KEY = "7613c6caddbac6c8549b60a388f6b45c"

def get_weather_data(location):
    if not location:
        print("Error: location is None or empty")
        return None

    if not isinstance(location, str):
        print(f"Error: Expected a string for location, got {type(location)}")
        return None

    # Determine the API endpoint based on the location format
    if location.isnumeric():
        api_url = f'http://api.openweathermap.org/data/2.5/weather?zip={location},us&appid={API_KEY}&units=metric'
    elif ',' in location:
        try:
            lat, lon = map(str.strip, location.split(','))
            api_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
        except ValueError:
            print("Error: Invalid coordinate format")
            return None
    else:
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        if response.status_code == 200:
            weather_data = response.json()

            # Process the timezone offset
            timezone_offset = weather_data.get('timezone', 0)
            city_time = datetime.utcfromtimestamp(weather_data['dt'] + timezone_offset)
            city_time_formatted = city_time.strftime('%Y-%m-%d %H:%M:%S')

            # Debugging
            print(f'all data: {weather_data}["weather"][0]')
        
            return {
                'city': weather_data.get('name', 'Unknown'),
                'temperature': weather_data['main']['temp'],
                'condition': weather_data['weather'][0]['description'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
                'date_time': city_time_formatted
            }
        else:
            print(f"Error: Received non-200 status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None
