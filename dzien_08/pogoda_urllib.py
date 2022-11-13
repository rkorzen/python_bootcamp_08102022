import sys
import json
import urllib.request
from collections import namedtuple

try:
    location = sys.argv[1]
except IndexError:
    location = "Warsaw"

# from typing import NamedTuple
KEY = "BAEVLKZKT7EZHTJYCRXYSRDCR"
Weather = namedtuple("Weather", ["location", "temperature", "icon", "humidity"])

def get_location_weather(location):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={KEY}&contentType=json'
    with urllib.request.urlopen(url) as f:
        response = json.loads(f.read())
        return Weather(
            location=response['resolvedAddress'],
            temperature=response["days"][0]["temp"],
            icon=response["days"][0]['icon'],
            humidity=response["days"][0]['humidity']
        )

def print_weather(weather: Weather):
    print(f"""
Pogoda w {weather.location}
- temperatura: {weather.temperature} 
- wilgotnośc: {weather.humidity}   
    """)

weather = get_location_weather(location)
print_weather(weather)
