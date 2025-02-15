from tkinter import *
from tkinter import ttk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from PIL import Image, ImageTk  
import pytz
import requests
import time

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
  try:
    name.config(text = "Current Weather")

    city = textfield.get()


    geolocator = Nominatim(user_agent = "MyWeatherApp123")
    time.sleep(1)
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
    print(result)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    current_date = local_time.strftime("%A, %d %B %Y")
    clock.config(text = current_time)
    date_o.config(text = current_date)


    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=00ff90d1d6009aca348e568fc5085e2c"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]["description"]
    temp = int(json_data['main']['temp' ]-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main'] ['humidity']
    wind = json_data['wind' ] [ 'speed']
    t.config(text = (temp,"°"))
    c.config(text=(condition, "|","FEELS", "LIKE", temp,"°"))

    w.config(text = wind)
    h.config(text = humidity)
    d.config(text = description)
    p.config(text = pressure)

  except Exception as e:
    messagebox.showerror("Weather App", "Invalid Entry!!")



search_image = PhotoImage(file = "E:\\Projects\\Weather App\\search.png")
myimage = Label(image = search_image)
myimage.place(relx=0.5, y=20, anchor="n")



textfield = Entry(root, justify="center", width=17, font=("Poppins", 25, "bold"), 
                  bg="#404040", fg="white", borderwidth=0)
textfield.place(relx=0.5, y=40, anchor="n")
textfield.focus()




Search_icon = PhotoImage(file = "E:\\Projects\\Weather App\\search_icon.png")
myicon = Button(image = Search_icon, borderwidth=0, cursor = "hand2", bg="#404040", command=getWeather)
myicon.place(x = 590, y= 32)


image_path = "E:\\Projects\\Weather App\\logo_new.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((300, 300))  # Set new width & height
logo_image = ImageTk.PhotoImage(resized_image)
logo = Label(root, image=logo_image)
logo.place(relx=0.5, y=90, anchor="n")

box_image = PhotoImage(file="E:\\Projects\\Weather App\\box.png")
box_myimage = Label(image= box_image)
box_myimage.pack(padx = 5, pady = 5, side = BOTTOM
                 )


name = Label(root, font=("arial", 15, "bold"))
name.place(x=100,y=100)
clock=Label(root, font=("Helvetica", 20))
clock.place(x=100,y=130)
date_o = Label(root, font=("arial", 15, "bold"))
date_o.place(x=600,y=100)


wind = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg = "#1ab5ef")
wind.place(x = 120, y = 400)

humidity = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg = "#1ab5ef")
humidity.place(x = 250, y = 400)

desc = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg = "#1ab5ef")
desc.place(x = 430, y = 400)


pressure = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg = "#1ab5ef")
pressure.place(x = 650, y = 400)


t = Label(font = ("arial", 70, "bold"), fg = "#ee666d")
t.place(x = 600, y = 150)
c = Label(font = ("arial", 15, "bold"))
c.place(x = 600, y = 250)

w = Label(text="....", font = ("arial", 20, "bold"), bg = "#1ab5ef")
w.place(x = 120, y = 430)
h = Label(text="....", font = ("arial", 20, "bold"), bg = "#1ab5ef")
h.place(x = 270, y = 430)
d = Label(text="....", font = ("arial", 20, "bold"), bg = "#1ab5ef")
d.place(x = 440, y = 430)
p = Label(text="....", font = ("arial", 20, "bold"), bg = "#1ab5ef")
p.place(x = 670, y = 430)

root.mainloop()
