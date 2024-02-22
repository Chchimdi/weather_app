from testfile import weather_zipcode, weather_city 


def fetch_weather():
    with open('appid.txt', 'r') as file:
        appid = file.readline().strip()

    user_input = input("Enter city or zipcode: ")

    try:
        if user_input.isdigit():
            return weather_zipcode(user_input, appid)
        else:
            return weather_city(user_input, appid)
    except KeyError:
        print("Not found. Please enter a valid zipcode or city name.")
    except ValueError:
        print("Invalid input. Please try again.")

print("Welcome to Chimdi's Weather App")

print(fetch_weather())
