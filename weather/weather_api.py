import requests
from datetime import datetime

# OpenWeatherMap API Key
API_KEY = "7613c6caddbac6c8549b60a388f6b45c"


def get_weather_data(location):
    # Check if the location is numeric (ZIP code)
    if location.isnumeric():
        api_url = f'http://api.openweathermap.org/data/2.5/weather?zip={location},us&appid=7613c6caddbac6c8549b60a388f6b45c&units=metric'
    # Check if the location contains a comma (likely coordinates)
    elif ',' in location:
        try:
            lat, lon = location.split(',')
            api_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=7613c6caddbac6c8549b60a388f6b45c&units=metric'
        except ValueError:
            return None  # Invalid coordinate format
    else:
        # Default case is assuming it's a city name
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=7613c6caddbac6c8549b60a388f6b45c&units=metric'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an error for bad status codes (4xx or 5xx)
        
        # If the request was successful, return the parsed weather data
        if response.status_code == 200:
            weather_data = response.json()

            # Get the timezone offset in seconds and convert to a timezone
            timezone_offset = weather_data['timezone']
            city_time = datetime.utcfromtimestamp(weather_data['dt'] + timezone_offset)
            city_time = city_time.strftime('%Y-%m-%d %H:%M:%S')  # Format the date and time
            
            # Debugging 4: checking Weather_condition to store it in database
            print(weather_data['weather'][0]['description'])



            return {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'condition': weather_data['weather'][0]['description'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
                'date_time': city_time  # Return the local date and time
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        # Log or print the error if necessary
        print(f"Error during API request: {e}")
        return None
