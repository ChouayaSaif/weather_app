# Tunisia Weather API

This is a REST API built with Django that provides weather information, recommendations, and chatbot functionality for regions in Tunisia. 


## Features

- **Weather Data**: Fetch real-time weather data for any Region in Tunisia.
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



## Install and usage
This project can be deployed and used in two different ways, depending on your requirements. Below are the instructions for each setup.

### Prerequisites
- Python 3.8 or higher
- Django 5.1 or compatible version
- Docker and Docker Compose installed
- Snowflake account credentials (for cloud-based deployment)

### Option 1: Cloud-Based Deployment with Render
1. Pull the pre-built Docker image from DockerHub:
  ```bash
   docker pull saifchouaya/my-django-app:latest
  ```
  OR 
  Clone the repository:
  ```bash
   git clone https://github.com/username/tunisia-weather-api.git
   cd weather-app
  ```

2. Create a virtual environment:
  ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
  ```

3. Install the required dependencies:
  ```bash
   pip install -r requirements.txt
  ```
4. Run the Django development server:
  ```bash
   python manage.py runserver
  ```
5. The service will rely on:
   - A connection between the frontend and the cloud database hosted on Snowflake.
   - Hosting on port 8000 using Render. You can access the service through the following link: [https://my-django-app-1-6qn8.onrender.com/](https://my-django-app-1-6qn8.onrender.com/)



### Configuration steps
- Once you have uploaded the application, you need to configure the database and static files.

- Note: The django-snowflake is handled using a package named "django-snowflake". Use the version of django-snowflake that corresponds to your version of Django. For example, to get the latest compatible release for Django 5.1.x:

Configure the Django DATABASES settings similar to this:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django_snowflake',
        'NAME': 'MY_DATABASE',
        'SCHEMA': 'MY_SCHEMA',
        'WAREHOUSE': 'MY_WAREHOUSE',
        'USER': 'my_user',
        'PASSWORD': 'my_password',
        'ACCOUNT': 'my_account',
        # Include 'OPTIONS' if you need to specify any other
        # snowflake.connector.connect() parameters, documented at:
        # https://docs.snowflake.com/en/user-guide/python-connector-api.html#connect
        'OPTIONS': {
            # Examples:
            'role': 'MY_ROLE',
            # To use native Okta authenticators:
            # https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-use#native-sso-okta-only
            'authenticator': 'https://example.okta.com',
            # To use private key authentication:
            'private_key_file': '<path>/rsa_key.p8',
            'private_key_file_pwd': 'my_passphrase',
        },
    },
}
```
Then run these commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

Now Gather all static files into a single location for serving:
```bash
python manage.py collectstatic
```

### Persistent connections
To use persisent connections, set Django's CONN_MAX_AGE and Snowflake Python Connector's client_session_keep_alive:
```python
DATABASES = {
    'default': {
        # ...
        'CONN_MAX_AGE': None,
        'OPTIONS': {
            'client_session_keep_alive': True,
        },
    },
}
```
### Troubleshooting
To troubleshoot issues with connectivity to Snowflake, you can enable Snowflake Connector for Python's logging using Django's LOGGING setting.

This is a minimal addition to Django's default "loggers" configuration that enables the connector's DEBUG logging:
```python
LOGGING = {
    …
    "loggers": {
        …
        "snowflake.connector": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}
```


### Option 2: Local Deployment with Docker Compose
1. Pull the Docker image for local deployment:
  ```bash
   docker pull saifchouaya/my-weather-app:latest
  ```
  OR 
  Clone the repository:
  ```bash
   git clone https://github.com/username/tunisia-weather-api.git
   cd weather-app
  ```
2. Create a virtual environment:
  ```bash
    bashpython -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
  ```
3. Run Docker Compose to start the services:
  ```bash
    docker-compose up --build
  ```
4. This setup will:
  - Trigger two services:
    - An application service (Django app).
    - A MySQL database service.
  - Connect the services via the app_network network.
5. Access your application locally at:
  ```bash
   http://localhost:8000
  ```

### Configuration steps
- Once you have uploaded the application, you need to configure the services availables in the docker-compose file and static files.

Configure the Django DATABASE and application containers settings similar to this:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weather_db_1', 
        'USER': 'user',         
        'PASSWORD': 'saifch',    
        'HOST': 'db',             
        'PORT': '3306',
    }
}
```
Then run these commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

Now Gather all static files into a single location for serving:
```bash
python manage.py collectstatic
```
   
Choose the setup that best fits your needs and follow the corresponding steps. If you encounter any issues or have questions, refer to the documentation or contact the project maintainer.


### Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request. Ensure your changes are well-documented and tested.


### License
This project is licensed under the MIT License. See the `LICENSE` file for details.