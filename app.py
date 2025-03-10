from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import time

time.sleep(1)
root = Tk()
root.title("Weather App")
root.geometry("800x400+200+100")
root.resizable(False, False)

def getWeather():
    try:
        city = text_field.get().strip()  # Ensure no extra spaces
        if not city:
            messagebox.showerror("Weather App", "Please enter a city!")
            return

        print(f"Fetching weather for: {city}")

        api_key = "API_KEY = fc6b1597d173164e83840e4613fdeb92"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(api_url)
        json_data = response.json()

        print("Status Code:", response.status_code)  # Debugging
        print("Response JSON:", json_data)  # Debugging

        if response.status_code == 403:
            messagebox.showerror("Weather App", f"403 Forbidden")
            return
        
        temp = json_data['main']['temp']
        t.config(text=str(round(temp, 2)))
        c.config(text=json_data['weather'][0]['main'])
        w.config(text=json_data['wind']['speed'])
        h.config(text=json_data['main']['humidity'])
        d.config(text=json_data['weather'][0]['description'])
        p.config(text=json_data['main']['pressure'])

    except Exception as e:
        messagebox.showerror("Weather App", f"An error occurred: {e}")

# Add Search Bar
image_search = PhotoImage(file="images/search_bar.png")
searchbar_image = Label(image=image_search)
searchbar_image.place(x=10, y=10)
text_field = tk.Entry(root, justify="center", width=17, font=("poppins", 18, "bold"), bg="#147886", border=0, fg="white")
text_field.place(x=20, y=20)
text_field.focus()

# Add Search Icon
image_search_icon = PhotoImage(file="images/search_icon.png")
search_icon = Button(image=image_search_icon, borderwidth=0, cursor="hand2", bg="#147886", command=getWeather)
search_icon.place(x=250, y=18)

# Add Weather Logo
image_logo = PhotoImage(file="images/weather_logo.png")
weather_logo = Label(image=image_logo)
weather_logo.place(x=250, y=90)

# Add Information Box
image_box = PhotoImage(file="images/information_box.png")
information_box = Label(image=image_box)
information_box.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Merriweather", 20))
clock.place(x=30, y=130)

# Labels for Information
label1 = Label(root, text="WIND", font=("Merriweather", 15, "bold"), fg="White", bg="#5AC9D9")
label1.place(x=100, y=330)

label2 = Label(root, text="HUMIDITY", font=("Merriweather", 15, "bold"), fg="White", bg="#5AC9D9")
label2.place(x=210, y=330)

label3 = Label(root, text="DESCRIPTION", font=("Merriweather", 15, "bold"), fg="White", bg="#5AC9D9")
label3.place(x=360, y=330)

label4 = Label(root, text="PRESSURE", font=("Merriweather", 15, "bold"), fg="White", bg="#5AC9D9")
label4.place(x=570, y=330)

# Display Weather Data
t = Label(font=("arial", 50, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 20, "bold"))
c.place(x=420, y=230)

w = Label(text="...", font=("arial", 16, "bold"), bg="#5AC9D9")
w.place(x=110, y=360)

h = Label(text="...", font=("arial", 16, "bold"), bg="#5AC9D9")
h.place(x=230, y=360)

d = Label(text="...", font=("arial", 16, "bold"), bg="#5AC9D9")
d.place(x=370, y=360)

p = Label(text="...", font=("arial", 16, "bold"), bg="#5AC9D9")
p.place(x=590, y=360)

root.mainloop()
