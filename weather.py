#!/usr/bin/python3.6
import requests
from pprint import pprint
import json
import re

city = input("Where are you located? (Ex. Los Angeles, London, Paris)\n")

matches = []
with open('city.list.json', 'r') as city_json:
    json_list = json.load(city_json)
    for i in json_list:
        if re.fullmatch(city.lower(), i['name'].lower()):
            matches.append(i)

r = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?id={}&appid=beb929e6e8c5c36b61aa990cfbd90558'.format(matches[0]['id']))
r_data = r.json()
temp_f = (r_data['main']['temp'] - 273.15) * (9 / 5) + 32
wind_speed = (r_data['wind']['speed']) * (25 / 11)

print(
    f"Current temperature in {r_data['name']} is {round(temp_f, 1)} degrees.")
print(f"Humidity is {r_data['main']['humidity']}%.")
