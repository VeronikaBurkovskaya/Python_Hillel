"""Отримати прогноз погоди для Одеси на наступні 5 днів та записати у файл з ім'ям поточної дати"""
import datetime

import requests
from http.client import HTTPResponse
from pprint import pp
import csv


def get_weather_by_requests(city: str, days: int) -> HTTPResponse:
    params = {'cnt': days, 'q': city, 'units':'metric', 'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    return requests.get('https://api.openweathermap.org/data/2.5/forecast/daily', params=params).json()


def set_date_and_temp(data:dict) ->list:
    result = []
    for i in data['list']:
        new_date = datetime.datetime.fromtimestamp(int(i['dt'])).strftime("%d-%m-%Y")
        temp_day = i['temp']['day']
        temp_night = i['temp']['night']
        result.append([new_date,temp_day,temp_night])
    return result


def set_file_name(city: str, days: int) -> str:
    date_for_file = datetime.datetime.now().strftime("%d-%m-%Y")
    params = [date_for_file, city, str(days), 'days', 'forest.txt']
    result = "-".join(params)
    return result


def write_in_file(city: str, days: int):
    with open(set_file_name(city,days), 'w+') as f:
        csv_writer = csv.writer(f, delimiter=' ')
        csv_writer.writerow('Date Temperature Day and Night')
        csv_writer.writerows(set_date_and_temp(get_weather_by_requests(city,days)))


city = input('Enter your city')
days = int(input('Enter count of Days'))

write_in_file(city,days)


