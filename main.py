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


def run_app():
    while True:
        print("Check the weather of a location.")
        print("\nSelect an option:")
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
            city = input("Enter city: ").strip()  # .strip() removes leading/trailing whitespace
            if city:  # Check if city input is not empty
                weather_city(city, appid)
            else:
                print("Please enter a valid city name.")
                continue
        elif user_input == 2:
            zipcode_input = input("Enter zipcode: ")
            try:
                zipcode = int(zipcode_input)  # Convert to integer
                weather_zip(zipcode, appid)
            except ValueError:
                print("Please enter a valid integer for the zipcode.")
                continue
        elif user_input == 3:
            lat_input = input("Enter latitude: ")
            lon_input = input("Enter longitude: ")
            try:
                lat = int(lat_input)  # Convert to integer
                lon = int(lon_input)  # Convert to integer
                weather_lat_long(lat, lon, appid)
            except ValueError:
                print("Please enter valid integers for latitude and longitude.")
                continue
        elif user_input == 4:
            print("Exiting the app. Thank you!")
            break

run_app()
print("\nThank you for using the Weather App.")
