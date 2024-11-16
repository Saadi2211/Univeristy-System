import os
import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

# Set API key
api_key = os.getenv("OPEN_WEATHER_API")

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(cities):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    data = []

    for city in cities:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric",  # Use "imperial" for Fahrenheit
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_info = response.json()
            city_name = weather_info["name"]
            temperature = weather_info["main"]["temp"]
            condition = weather_info["weather"][0]["description"]

            data.append(
                {"City": city_name, "Temperature": temperature, "Condition": condition}
            )
        else:
            print(f"Could not retrieve data for {city}")

    return pd.DataFrame(data)