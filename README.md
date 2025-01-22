# Tunisia Weather API

This is a REST API built with Django that provides weather information, recommendations, and chatbot functionality for regions in Tunisia. 


## Install and usage
This project can be deployed and used in two different ways, depending on your requirements. Below are the instructions for each setup.

### Option 1: Cloud-Based Deployment with Render
1. Pull the pre-built Docker image from DockerHub:
   ```bash
   docker pull saifchouaya/my-django-app:latest
   ```
2. Install the required dependencies:
  ```bash
   pip install -r requirements.txt
   ```
3. Run the Django development server:
  ```bash
   python manage.py runserver
   ```
4. The service will rely on:
  - A connection between the frontend and the cloud database hosted on Snowflake.
  - Hosting on port 8000 using Render. You can access the service through the following link: https://my-django-app-1-6qn8.onrender.com/


### Option 2: Local Deployment with Docker Compose
1. Pull the Docker image for local deployment:
  ```bash
   docker pull saifchouaya/my-weather-app:latest
  ```
2. Run Docker Compose to start the services:
  ```bash
    docker compose up --build
  ```
3. This setup will:
  - Trigger two services:
    - An application service (Django app).
    - A MySQL database service.
  - Connect the services via the app_network network.
4. Access your application locally at:
  ```bash
   http://localhost:8000
  ```
   


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




Choose the setup that best fits your needs and follow the corresponding steps. If you encounter any issues or have questions, refer to the documentation or contact the project maintainer.