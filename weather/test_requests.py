# Import your function from requests.py
from weather_api import get_weather_data  

# Test with a sample location
location = "London"
weather_data = get_weather_data(location)

# Print the result to the terminal
if weather_data:
    print(f"Weather data for {location}:")
    print(f"City: {weather_data['city']}")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Condition: {weather_data['condition']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")
else:
    print("Failed to retrieve weather data.")
