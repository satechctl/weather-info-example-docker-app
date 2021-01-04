#!/usr/bin/env python3

import argparse
import requests
import os
import json

from countryinfo import CountryInfo

OPENWEATHERMAP_API_URL = "https://api.openweathermap.org/data/2.5/weather" 
OPENWEATHERMAP_API_KEY = str(os.environ.get('OPENWEATHERMAP_API_KEY'))

def get_weather_info(city_name):
    # -- prepare request to api.openweathermap.org
    request_url = OPENWEATHERMAP_API_URL + "?q=" + str(city_name.capitalize()) + "&appid=" + OPENWEATHERMAP_API_KEY
    # -- get weather status for a given city
    result = requests.get(request_url)
    # -- return weather status as json
    return result.json()


if __name__ == "__main__":

    # -- parse command line argumets (get city name)
    parser = argparse.ArgumentParser(
        description="Check the weather for the capital city in given country"
    )
    # -- city name as positional argument
    parser.add_argument("country", help="Country name")
    args = parser.parse_args()

    # -- get country capital
    capital_city = CountryInfo(args.country).capital()

    # -- print weather status for a given city
    print(json.dumps(get_weather_info(capital_city), indent=4))
