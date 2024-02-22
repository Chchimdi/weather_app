import requests

def request(URL):
    req = requests.get(url=URL)
    req_result = req.json()
    
    condition = req_result['weather'][0]['main']
    description = req_result['weather'][0]['description']
    temp = req_result['main']['temp']
    city = req_result['name']
    country = req_result['sys']['country']
    
    return f"City: {city}, Country: {country} \nCondition: {condition} \nTemp: {temp}'c \nDescription: {description}\n"

def weather_city(city, appid):
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'
    return request(URL)

def weather_zipcode(zipcode, appid):
    URL = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&units=metric&appid={appid}'
    return request(URL)

# {'coord': {'lon': -123.2722, 'lat': 44.5904},
#  'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
#  'base': 'stations',
#  'main': {'temp': 10, 'feels_like': 7.03, 'temp_min': 8.99, 'temp_max': 10.93, 'pressure': 1014, 'humidity': 91},
#  'visibility': 10000, 'wind': {'speed': 6.69, 'deg': 170},
#  'clouds': {'all': 100},
#  'dt': 1708542956,
#  'sys': {'type': 2, 'id': 2005452, 'country': 'US', 'sunrise': 1708527886, 'sunset': 1708566543}, 
#  'timezone': -28800, 'id': 0, 'name': 'Corvallis', 'cod': 200}
