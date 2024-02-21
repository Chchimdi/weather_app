import requests

def request(URL):
    req = requests.get(url=URL)
    req_result = req.json()
    print(req_result)
    
    condition = req_result['weather'][0]['main']
    description = req_result['weather'][0]['description']
    temp = req_result['main']['temp']
    print(f"Condition: {condition} \nTemp: {temp}'c \nDescription: {description}\n")

def weather_city(city, appid):
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'
    request(URL)

def weather_zipcode(zipcode, appid):
    URL = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&units=metric&appid={appid}'
    request(URL)

def weather_lat_long(lat, lon, appid):
    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}"
    request(URL)

def validate_city():
    while True:
        city = input("Enter City: ").strip()  # .strip() removes leading/trailing whitespace
        if city:  # Check if city input is not empty
            try:
                weather_city(city, appid)
                break  # Break the loop if the city is valid and no KeyError is raised
            except KeyError:
                print("City not found. Please enter a valid city name.")
        else:
            print("Please enter a correct city name.")

def validate_zipcode():
    while True:
        zipcode = input("Enter Zipcode: ").strip()  # .strip() removes leading/trailing whitespace
        if zipcode:  # Check if city input is not empty
            try:
                weather_zipcode(zipcode, appid)
                break  # Break the loop if the city is valid and no KeyError is raised
            except KeyError:
                print("Zipcode not found. Please enter a valid zipcode.")
        else:
            print("Please enter a correct city name.")

def validate_lat_long():
    while True:
        lat = input("Enter latitude: ")
        lon = input("Enter longitude: ")
        if lat and lon:
            try:
                weather_lat_long(lat, lon, appid)
                break
            except KeyError:
                print("Please enter valid latitude and longitude of a place.")

with open('appid.txt', 'r') as file:
    appid = file.readline().strip()

print("Welcome to Chimdi's Weather App")
print("Check the weather of a location.")


def run_app():
    while True:
        print("Select an option:")
        print("1. Enter city")
        print("2. Enter zipcode")
        print("3. Enter latitude and longitude")
        print("4. Quit")

        user_input = input("Enter your option (1-4): ")
        if not user_input.isdigit() or not 1 <= int(user_input) <= 4:
            print("Enter a valid input.")
            continue

        user_input = int(user_input)

        if user_input == 1:
            validate_city()
            continue

        elif user_input == 2:
            validate_zipcode()
            continue

        elif user_input == 3:
            validate_lat_long()
            continue

        elif user_input == 4:
            print("Exiting the app. Thank you!")
            break

run_app()
print("\nThank you for using the Weather App.")
