#!/usr/bin/python3.6
import requests
from pprint import pprint
import json
import re
import sys

usage = "usage: ./weather.py [-c] city1 [city2 ...]\n    -c: display temperature in celcius\n    city1, city2, etc: cities to look up"

if len(sys.argv) < 2:
    print(usage)
    exit()
elif '-c' in sys.argv:
    city_list = sys.argv[2:]
    temp_flag = 'C'
else:
    city_list = sys.argv[1:]
    temp_flag = 'F'


def weather(city):
    matches = []
    with open('city.list.json', 'r') as city_json:
        json_list = json.load(city_json)
        for i in json_list:
            if re.fullmatch(city.lower(), i['name'].lower()):
                matches.append(i)

    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?id={}&appid=beb929e6e8c5c36b61aa990cfbd90558'.format(matches[0]['id']))
    r_data = r.json()
    if temp_flag == 'F':
        temp = (r_data['main']['temp'] - 273.15) * (9 / 5) + 32
    else:
        temp = (r_data['main']['temp'] - 273.15)

    print(
        f"{r_data['name']}:\n  -temperature: {round(temp, 1)}°{temp_flag}")
    print(f"  -humidity: {r_data['main']['humidity']}%")


for i in city_list:
    weather(i)
