import tkinter as tk
import requests


API_KEY = "your_api_key_here"
BASE_URL = "API_KEY = "http://api.AIzaSyCg98dRVoLqks780Cy0_OJtgJKUkIHjsXQ"


def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = (
                f"📍 City: {city_name}\n"
                f"🌡 Temperature: {temp}°C\n"
                f"☁ Weather: {weather.title()}\n"
                f"💧 Humidity: {humidity}%\n"
                f"🌬 Wind Speed: {wind} m/s"
            )
        else:
            result = f"City not found: {city}"

        result_label.config(text=result)
    except Exception as e:
        result_label.config(text="Error fetching data. Check your internet or API key.")

# --- GUI setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

tk.Label(root, text="Enter City Name:", font=("Helvetica", 14)).pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
