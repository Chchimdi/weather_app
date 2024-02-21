import tkinter as tk
from testfile import weather_zipcode, weather_city 


def fetch_weather():
    with open('appid.txt', 'r') as file:
        appid = file.readline().strip()

    user_input = input_field.get()  # Get the input from the input field
    try:
        if user_input.isdigit():
            # Assuming weather_zip is your function to fetch weather by zipcode
            weather_zipcode(user_input, appid)
        else:
            # Assuming weather_city is your function to fetch weather by city name
            weather_city(user_input, appid)
    except KeyError:
        result_label.config(text="Not found. Please enter a valid zipcode or city name.")
    except ValueError:
        result_label.config(text="Invalid input. Please try again.")


# Setting up the GUI
root = tk.Tk()
root.title("Weather Lookup App")

input_field = tk.Entry(root)
input_field.pack()

enter_button = tk.Button(root, text="Enter", command=fetch_weather)
enter_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
