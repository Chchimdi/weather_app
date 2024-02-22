from testfile import weather_zipcode, weather_city 


def fetch_weather(user_input):
    with open('appid.txt', 'r') as file:
        appid = file.readline().strip()

    try:
        if user_input.isdigit():
            return weather_zipcode(user_input, appid)
        else:
            return weather_zipcode(user_input, appid)
    except KeyError:
        print("Not found. Please enter a valid zipcode or city name.")
    except ValueError:
        print("Invalid input. Please try again.")

print("Welcome to Chimdi's Weather App")
user_input = input("Enter city or zipcode: ")
print(fetch_weather(user_input))
