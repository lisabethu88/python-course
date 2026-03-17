"""
Assignment 7 - External Libraries and APIs

This program prompts the user for a ZIP code and fetches a 7-day weather forecast
using the Open-Meteo API.

Main features:
- Validates user input to make sure it's a valid ZIP code
- Uses the Open-Meteo Geocoding API to convert the ZIP code into latitude and longitude
- Fetches daily weather data (high/low temperature and precipitation) for 7 days
- USes NumPy arrays for better numerical data handling
- Uses pandas to organize the weather data into a structured DataFrame 
- Formats output with units (°F and inches)
- Displays the final forecast to the console

Libraries used:
- openmeteo_requests: for working with the Open-Meteo API
- requests_cache: to cache API responses
- retry_requests: to automatically retry failed API calls
- pandas: for data organization and display
- NumPy: for numerical data processing
- re: for validating ZIP code input using regular expressions
"""

import openmeteo_requests
import pandas as pd
import numpy as np
import requests_cache
from retry_requests import retry
import re

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

print('----------------------')
print("7-DAY WEATHER FORECAST")
print('----------------------')

# Prompt the user for their zipcode. Keep looping if they don't enter in the correct format
while True:
    
    # prompt user for zipcode
    zip_code = input("Enter in your zipcode: ")

    pattern = r"^\d{5}(-\d{4})?$"

    # Test that the input matches the right pattern
    if not re.match(pattern, zip_code):
        print("Invalid ZIP code format.")
        continue

    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

    geocode_params = {
        "name": zip_code,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    geo_response = retry_session.get(geocode_url, params=geocode_params)
    geo_data = geo_response.json()

    # check if zip code is found in the geo-data api
    if "results" not in geo_data:
        print("ZIP code not found.")
        continue

    # variables that will be sent in the call to the weather API or used later when printing to the console
    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]
    name = geo_data["results"][0]["name"]
    country = geo_data["results"][0]["country"]
    state = geo_data["results"][0]["admin1"]

    break


# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": latitude,
	"longitude": longitude,
    "daily": ["temperature_2m_max", "temperature_2m_min","precipitation_sum"],
    "forecast_days": 7,
	"timezone": "auto",
    "temperature_unit": "fahrenheit",
    "precipitation_unit": "inch",
}
responses = openmeteo.weather_api(url, params=params)

# Process first location
response = responses[0]

# Process daily data as a NumPy array and convert values to integers. 
# The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy().astype(int)
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy().astype(int)
daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy().round(1)

# Generate a list of day names starting from the first date, one per day,
# matching the number of temperature data points
daily_data = {"Day": pd.date_range(
    # Convert the starting time from Unix seconds into a datetime so it's more readable
	start = pd.to_datetime(daily.Time(), unit = "s"), 
    # Set the frequency to 'D' which means generate one date per day
	freq = 'D',
    # Generate as many dates as there are temperature values
    # so the dates line up with the weather data
    periods = len(daily_temperature_2m_max)
).day_name()}

# Format weather data as strings by adding units (° for temperature, "in" for precipitation)
degree_symbol = u'\N{DEGREE SIGN}'
daily_data["High"] = daily_temperature_2m_max.astype(str) + degree_symbol
daily_data["Low"] = daily_temperature_2m_min.astype(str)+ degree_symbol
daily_data["Precipitation"] = daily_precipitation_sum.astype(str) + 'in'

# Create a pandas DataFrame from the daily_data dictionary.
# pandas is a Python library used for data analysis. 
# Here we are using their structures called DataFrames which are similar to tables and
# where data is organized into rows and columns.
daily_dataframe = pd.DataFrame(data = daily_data)

# print the result
print(
    f'\n7-Day Forecast for {name}, {state}, {country}\n',
    daily_dataframe.to_string(index=False)
)