import requests

def request(URL):
    req = requests.get(url=URL)
    req_result = req.json()
    
    condition = req_result['weather'][0]['main']
    description = req_result['weather'][0]['description']
    temp = req_result['main']['temp']
    print(f"Condition: {condition} \nTemp: {temp}'c \nDescription: {description}\n")

def weather_city(city, appid):
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'
    request(URL)

def weather_zip(zipcode, appid):
    URL = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&units=metric&appid={appid}'
    request(URL)

def weather_lat_long(lat, lon, appid):
    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}"
    request(URL)
    
with open('appid.txt', 'r') as file:
    appid = file.readline().strip()
print("Welcome to Chimdi's Weather App")
print("Select any of the options to Check Weather in your desired location: \n 1. city \n 2. zip code \n 3. Longitude and Latitude \n 4. Close app")

def main():
    while True:
        user_input = int(input("Enter your an option between 1-4: "))
        if user_input == 1:
            city = input("Enter city: ")
            weather_city(city, appid)
        elif user_input == 2:
            zipcode = input("Enter zipcode: ")
            weather_zip(zipcode, appid)
        elif user_input == 3:
            lat = input("Enter latitude: ")
            lon = input("Enter longitude: ")
            weather_lat_long(lat, lon, appid)
        elif user_input == 4:
            break
        else:
            print("Enter a valid input")

main()
print("\nDo you want to check the weather again? \n Y for Yes \n Any other character for No")
response = input("Enter option: ")
if response == "Y" or response == "y":
    main()


print("\nThank you for using the Weather App.")
