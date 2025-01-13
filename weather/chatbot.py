# chatbot.py
import os
import requests
import json

# API Key and endpoint
XAI_API_KEY = "xai-I3yN6jKSnG699mFiw3X2S13Hi7ZgqVPfgXiTPDihfen0FvCj489RWNgpmmD7Q68LFo4iFtE9d7xlDPCw"
url = "https://api.x.ai/v1/chat/completions"

# Headers for authentication
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {XAI_API_KEY}",
}

# Initialize conversation history with system message
messages = [
    {"role": "system", "content": "You are a helpful chatbot."}
]


def weather_data(location="Tunisia"):
    API_KEY = "7613c6caddbac6c8549b60a388f6b45c"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        return f"The current temperature in {location} is {temperature}°C with {weather_description}."
    else:
        return "Sorry, I couldn't retrieve weather data at the moment."
    


def ask_chatbot(user_message):
    # Append the user's message to the conversation history
    messages.append({"role": "user", "content": user_message})

    # Check if the user message is about the weather
    if "weather" in user_message.lower():
        weather_info = weather_data("Tunisia")  # You can replace "Tunisia" with dynamic location detection
        return weather_info

    # The data to send in the request to the chatbot
    data = {
        "messages": messages,
        "model": "grok-beta",  # or another model you want to use
        "stream": False,
        "temperature": 0
    }

    # Send the request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response status
    if response.status_code == 200:
        response_json = response.json()
        assistant_message = response_json['choices'][0]['message']['content']
        
        # Append the assistant's message to the conversation history
        messages.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    else:
        return f"Error: {response.status_code}, {response.text}"
