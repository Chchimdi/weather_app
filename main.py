import requests
import time


def weather(city):
    appid = '44c8b9cfd1b46c5f31e80bb0a67d8c7d'
    city = 'corvallis'
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'

    req = requests.get(url=URL)
    req_result = req.json()
    
    condition = req_result['weather'][0]['main']
    description = req_result['weather'][0]['description']
    temp = req_result['main']['temp']
    print(f"Condition: {condition} \nTemp: {temp}'c \nDescription: {description}\n")


city = input('Please enter city: ')
weather(city)

