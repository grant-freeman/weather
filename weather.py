#!/usr/local/bin/python3.6
import requests
from pprint import pprint
import json
import re
import sys
from progress.counter import Stack

usage = f"usage: {sys.argv[0]} [-c] city1 [city2 ...]\n    -c: display temperature in celcius\n    city1, city2, etc: cities to look up"
api_key = 'd101ae2101dd53b3bc0b13776b1452ee'

#simple argument parsing
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

#the MEAT
def weather(city):
    matches = []
		#searching through json to find matches in city names
    with open('city.list.json', 'r') as city_json:
        json_list = json.load(city_json)
        for i in json_list:
            if re.fullmatch(city.lower(), i['name'].lower()):
                matches.append(i)
		#sending requests to api to grab data for current weather
    if matches:
        r = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'.format(matches[0]['id'], api_key))
        r_data = r.json()
				#should we be in celcius or freedom units
        if temp_flag == 'F':
            temp = (r_data['main']['temp'] - 273.15) * (9 / 5) + 32
        else:
            temp = (r_data['main']['temp'] - 273.15)
				#formatting output
        output_data.append(
            f"{r_data['name']}:\n  -temperature: {round(temp, 1)}°{temp_flag}")
        output_data.append(f"  -humidity: {r_data['main']['humidity']}%")
    else:
        output_data.append(f'Error: \"{city}\" not in lookup table.')

#pretty loading symbol
for i in Stack('Fetching ').iter(city_list):
    weather(i)

#finally printing output
print('\n')
for i in output_data:
    print(i)
