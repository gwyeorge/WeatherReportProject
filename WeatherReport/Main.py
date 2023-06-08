Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import *
import tkinter as tk
... from geopy.geocoders import Nominatim
... from tkinter import ttk, messagebox
... from timezonefinder import TimezoneFinder
... from datetime import datetime
... import requests
... import pytz
... 
... window = Tk()
... window.title("Weather App")
... window.geometry("900x500+300+200")
... window.resizable(False, False)
... 
... def getWeather():
...     city = textfield.get()
... 
...     geolocator = Nominatim(user_agent="geoapiExercises")
...     location = geolocator.geocode(city)
...     obj = TimezoneFinder()
...     result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
... 
...     home = pytz.timezone(result)
...     local_time = datetime.now(home)
...     current_time = local_time.strftime("%I:%M %p")
...     clock.config(text=current_time)
...     name.config(text='CURRENT WEATHER')
... 
...  #   api = 'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&' + city + 'YOUR API KEY HERE'
... 
...     json_data = requests.get(api).json()
... 
...     print(json_data)
... 
...     if 'weather' in json_data:
...         condition = json_data['weather'][0]['main']
...         description = json_data['weather'][0]['description']
...         temp = int(json_data['main']['temp'] - 273.15)
...         pressure = json_data['main']['pressure']
...         humidity = json_data['main']['humidity']
...         wind = json_data['wind']['speed']

        t.config(text=(temp, '°'))
        c.config(text=(condition, '|', 'FEELS', 'LIKE', temp, '°'))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    else:
        messagebox.showerror("Error", "Failed to retrieve weather information.")


search_image = PhotoImage(file="images/search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(window, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="images/search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

logo_image = PhotoImage(file="images/logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

frame_image = PhotoImage(file="images/box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

name = Label(window, font=('arial', 15, 'bold'))
name.place(x=30, y=100)
clock = Label(window, font=('Helvetica', 20))
clock.place(x=30, y=130)

label1 = Label(window, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(window, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=225, y=400)

label3 = Label(window, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(window, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=400, y=430)

p = Label(font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

window.mainloop()
