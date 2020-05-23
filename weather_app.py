#! /usr/bin/python3

import requests
import sys

#Takes the City Name as Command Line Argument

def weather_city(city):
    api_url = "http://api.weatherapi.com/v1/current.json?key=381d17d37e344cea8ba90809202305&q="
    url = "{}{}".format(api_url,city)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("*Location: {}".format(data["location"]["name"]))
        print("*Temperature (in Celcius): {}".format(data["current"]["temp_c"]))
        print("*Feels Like : {}".format(data["current"]["feelslike_c"]))
        print("*Condition : {}".format(data["current"]["condition"]["text"]))
        print("*Wind Speed : {}Km/h".format(data["current"]["wind_kph"]))
        print("*Humidity : {}".format(data["current"]["humidity"]))
        print()
        print("*Last Updated : {}".format(data["current"]["last_updated"]))
    

user_input = sys.argv[1:]
user_input = " ".join(user_input)

weather_city(user_input)