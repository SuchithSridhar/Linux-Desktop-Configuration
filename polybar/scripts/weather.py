#!/bin/python

# Procedure
# Surf to https://openweathermap.org/city
# Fill in your CITY
# e.g. Antwerp Belgium
# Check url
# https://openweathermap.org/city/2803138
# you will the city code at the end
# create an account on this website
# create an api key (free)
# LANG included thanks to krive001 on discord


import requests
import datetime
import pickle
import os

CITY = "Halifax"
API_KEY_FILE = "/home/suchi/.pass/weather-api-key"
UNIT_KEY = "C"  # Temperature units
LANG = "en"
TIME_DIFF = 2 * (60 * 60)  # Diff in seconds
LOG_FILE = "/home/suchi/.local/suchi-log/weather-api-log.log"
CACHE_FILE = "/home/suchi/.cache/custom-cache/weather-cache.pickle"
HTTP_CODE_OK = 200
URL = ("https://api.weatherapi.com/v1/current.json?"
       "key={}&q={}&aqi=no")

ICON_MAP = {
    1000: "",
    1003: "",
    1006: "",
    1009: "",
    1030: "",
    1063: "",
    1066: "",
    1069: "",
    1072: "",
    1087: "",
    1114: "",
    1117: "",
    1135: "",
    1147: "",
    1150: "",
    1153: "",
    1168: "",
    1171: "",
    1180: "",
    1183: "",
    1186: "",
    1189: "",
    1192: "",
    1195: "",
    1198: "",
    1201: "",
    1204: "",
    1207: "",
    1210: "",
    1213: "",
    1216: "",
    1219: "",
    1222: "",
    1225: "",
    1237: "",
    1240: "",
    1243: "",
    1246: "",
    1249: "",
    1252: "",
    1255: "",
    1258: "",
    1261: "",
    1264: "",
    1273: "",
    1276: "",
    1279: "",
    1282: ""
}


def get_api():
    with open(API_KEY_FILE) as f:
        data = f.read().strip()
    return data


def get_url():
    return URL.format(get_api(), CITY)


def log():
    time = datetime.datetime.now()
    with open(LOG_FILE, 'a') as f:
        f.write(f"API call at: {time}\n")


def get_weather():

    log()
    REQ = requests.get(get_url())
    value = ''
    error = False
    time = datetime.datetime.now()

    try:
        if REQ.status_code == HTTP_CODE_OK:
            data = REQ.json()
            current = data["current"]["condition"]["text"].capitalize()
            temp = int(float(data["current"]["temp_c"]))
            icon = ICON_MAP.get(data["current"]["condition"]["code"], "")
            value = "{} {}, {} °{}".format(icon, current, temp, UNIT_KEY)

        else:
            value = "Error: HTTP CODE " + str(REQ.status_code)
            error = True

    except (ValueError, IOError):
        value = "Error: Unable print the data"
        error = True

    return {
        'value': value,
        'error': error,
        'time': time
    }


def write_cache(data):
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(data, f)


def check_cache():
    if (os.path.isfile(CACHE_FILE)):
        with open(CACHE_FILE, 'rb') as f:
            data = pickle.load(f)
    else:
        data = {}

    return data


def main():
    now = datetime.datetime.now()
    data = check_cache()
    if (data == {} or
       (now - data['time']).total_seconds() > TIME_DIFF or
       data['error']):

        data = get_weather()
        write_cache(data)

    print(data['value'])


if __name__ == "__main__":
    main()
