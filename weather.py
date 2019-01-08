#!/usr/local/bin/python3.6
import requests
from pprint import pprint
import json
import re
import sys
from progress.counter import Stack

usage = f"usage: {sys.argv[0]} [-c] city1 [city2 ...]\n    -c: display temperature in celcius\n    city1, city2, etc: cities to look up"

if len(sys.argv) < 2:
    print(usage)
    exit()
elif '-c' in sys.argv:
    city_list = sys.argv[2:]
    temp_flag = 'C'
else:
    city_list = sys.argv[1:]
    temp_flag = 'F'

output_data = []


def weather(city):
    matches = []
    with open('city.list.json', 'r') as city_json:
        json_list = json.load(city_json)
        for i in json_list:
            if re.fullmatch(city.lower(), i['name'].lower()):
                matches.append(i)

    if matches:
        r = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?id={}&appid=beb929e6e8c5c36b61aa990cfbd90558'.format(matches[0]['id']))
        r_data = r.json()
        if temp_flag == 'F':
            temp = (r_data['main']['temp'] - 273.15) * (9 / 5) + 32
        else:
            temp = (r_data['main']['temp'] - 273.15)

        output_data.append(
            f"{r_data['name']}:\n  -temperature: {round(temp, 1)}°{temp_flag}")
        output_data.append(f"  -humidity: {r_data['main']['humidity']}%")
    else:
        output_data.append(f'Error: {city} not in lookup table.')


for i in Stack('Fetching ').iter(city_list):
    weather(i)

print('\n')
for i in output_data:
    print(i)
