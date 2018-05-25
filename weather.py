#!/usr/bin/python3.6
import requests
from weatherutil import *
from pprint import pprint
# variables
r = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?id=4339348&appid=beb929e6e8c5c36b61aa990cfbd90558')
r_data = r.json()
temp_f = (r_data['main']['temp'] - 273.15) * (9 / 5) + 32
wind_speed = (r_data['wind']['speed']) * (25 / 11)

def printweather():
    print("Current temperature in %s is %s degrees." %
          (r_data['name'], round(temp_f, 1)))
    print("Humidity is %s%%." % (r_data['main']['humidity']))
    print("Wind is currently blowing %s at %s mph" %
          (deg_to_dir(r_data['wind']['deg']), round(wind_speed, 1)))

printweather()
