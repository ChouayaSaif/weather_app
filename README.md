# Tunisia Weather API

This is a REST API built with Django that provides weather information, recommendations, and chatbot functionality for various locations in Tunisia.

## Features

- **Weather Data**: Fetch real-time weather data for any location in Tunisia.
- **Daily Recommendations**: Get daily recommendations based on the current weather conditions.
- **Planned Recommendations**: Get weather-based recommendations for future dates.
- **Chatbot**: Interact with a chatbot to get weather-related information.
- **User Preferences**: Manage user preferences such as default location, favorite locations, and alert settings.

## API Endpoints

### Weather Information
- **GET** `/api/v1/Weather-Information/<str:location>/`
  - Fetch weather data for a specific location in Tunisia.

### Chatbot
- **POST** `/api/v1/Chatbot/<str:message>/`
  - Interact with the chatbot to get weather-related information.

### Planned Recommendations
- **POST** `/api/v1/Planned-Recommendations/`
  - Get weather-based recommendations for future dates.

### User Preferences
- **GET** `/api/v1/User-Preferences/preferences/`
  - Retrieve user preferences including default location and favorite locations.

### Daily Recommendations
- **GET** `/api/v1/Daily-Recommendations/<str:location_name>/`
  - Get daily recommendations based on the current weather conditions for a specific location.

### Update User Preferences
- **PUT** `/api/v1/Update-Preferences/<str:field>/<str:value>/`
  - Update a specific field in the user preferences.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/tunisia-weather-api.git
   cd tunisia-weather-api