#from dataclasses import dataclass
import datetime
from pprint import pprint

import requests
#from config import open_weather_token
open_weather_token = '2e5e9b911cb312dca1867c57ea705973'

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
          #  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе {city}\nТемпература: {cur_weather}C\nВлажность: {humidity}%\n")


    except Exception as ex:
        print(ex)
        print('Проверьте название города')


def main():
    city = input('Введите город: ')

    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()