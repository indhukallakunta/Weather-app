import tkinter as tk
import requests

API_KEY = "08a071a5d79eaf3053db1f09a031fd17"

root = tk.Tk()
root.title("Weather App")

window_width = 300
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)

def get_weather():
    city = city_entry.get()
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                temp = data["main"]["temp"]
                condition = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]

                temp_label.config(text=f"Temperature: {temp}°C")
                condition_label.config(text=f"Condition: {condition}")
                humidity_label.config(text=f"Humidity: {humidity}%")
            else:
                temp_label.config(text="Temperature: -")
                condition_label.config(text="City not found")
                humidity_label.config(text="Humidity: -")
        except:
            condition_label.config(text="Error fetching data")
    else:
        condition_label.config(text="Please enter a city")

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=5)

get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack(pady=10)

temp_label = tk.Label(root, text="Temperature: ")
temp_label.pack(pady=2)

condition_label = tk.Label(root, text="Condition: ")
condition_label.pack(pady=2)

humidity_label = tk.Label(root, text="Humidity: ")
humidity_label.pack(pady=2)

root.mainloop()

