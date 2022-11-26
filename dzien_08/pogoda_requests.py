import sys
import json
import requests
from collections import namedtuple


locations = sys.argv[1:]
if not locations:
    locations = ["Warsaw"]

# from typing import NamedTuple
KEY = "BAEVLKZKT7EZHTJYCRXYSRDCR"
Weather = namedtuple("Weather", ["location", "temperature", "icon", "humidity"])


# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/warsaw?unitGroup=metric&key=BAEVLKZKT7EZHTJYCRXYSRDCR&contentType=json'
def get_location_weather(location):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={KEY}&contentType=json'
    response = requests.get(url)
    # print(response.status_code)
    print(response.content)
    response_json = response.json()
    return Weather(
        location=response_json['resolvedAddress'],
        temperature=response_json["days"][0]["temp"],
        icon=response_json["days"][0]['icon'],
        humidity=response_json["days"][0]['humidity']
    )

def print_weather(weather: Weather):
    print(f"""
Pogoda w {weather.location}
- temperatura: {weather.temperature} 
- wilgotnośc: {weather.humidity}   
    """)

print("xxx", locations)
for location in locations:
    print(location, locations)
    weather = get_location_weather(location)
    print_weather(weather)
