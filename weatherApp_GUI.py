from tabnanny import check
from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from datetime import datetime
import os

w = Tk()
w.geometry('800x400')
w.title("Weather App")
w.resizable(0, 0)

# Define paths to image files
base_dir = '/Users/jaypurdie/Desktop/Menu/'
search_img_path = os.path.join(base_dir, '/Users/jaypurdie/Desktop/Menu/Search.jpg')
no_internet_img_path = os.path.join(base_dir, '/Users/jaypurdie/Desktop/Menu/Nointernet.jpg')
sunny_img_path = os.path.join(base_dir, '/Users/jaypurdie/Desktop/Menu/Sunny.jpg')
cloudy_img_path = os.path.join(base_dir, '/Users/jaypurdie/Desktop/Menu/Cloudy.png')
cloudcold_img_path = os.path.join(base_dir, '/Users/jaypurdie/Desktop/Menu/Cloudcold.jpg')
rain_img_path = os.path.join(base_dir, '/Users/jaypurdie/Desktop/Menu/Rain.jpg')
cold_img_path = os.path.join(base_dir, '/Users/jaypurdie/Desktop/Menu/Cold.png')
def weather_data(query):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?' + query + '&units=metric&appid=6b67799ce53562b530e0d2e46bfcff9a')
    return res.json()

try:
    Frame(w, width=800, height=50, bg='#353535').place(x=0, y=0)
    
    # Search bar
    try:
        imgSearch = ImageTk.PhotoImage(Image.open(search_img_path))
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {search_img_path}")
        w.destroy()
        exit()
    
    def on_entry(e):
        el.delete(0, 'end')
        
    def on_leave(e):
        if el.get() == '':
            el.insert(0, 'Search City')
    
    el = Entry(w, width=21, fg='white', bg='#353535', border=0)
    el.config(font=('Calibri', 12))
    el.bind("<FocusIn>", on_entry)
    el.bind("<FocusOut>", on_leave)
    el.insert(0, 'Search City')
    el.place(x=620, y=15)
    
    # Date Format
    month = datetime.now().strftime('%b')
    today = datetime.today().strftime("%d")
    
    def label(city):
        Frame(w, width=500, height=50, bg="#353535").place(x=0, y=0)
        
        l1 = Label(w, text=str(city), bg="#353535", fg="white")
        l1.config(font=("Calibri", 18))
        l1.place(x=20, y=8)
        
        query = 'q=' + city
        w_data = weather_data(query)
        result = w_data
        
        try:
            check = '{}'.format(result['main']['temp'])
            print(check)
        except KeyError:
            messagebox.showinfo("", "City is not found!")
            return
        
        c = int(float(check))
        description = "{}".format(result['weather'][0]['description'])
        weather = "{}".format(result['weather'][0]['main'])
        
        global imgWeather
        
        if c > 10 and weather in ["Haze", "Clear"]:
            Frame(w, width=800, height=350, bg="#F78954").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open(sunny_img_path))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#F78954"
            fcolor = "white"
        
        elif c > 10 and weather == "Clouds":
            Frame(w, width=800, height=350, bg="#7492B3").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open(cloudy_img_path))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#7492B3"
            fcolor = "white"
        
        elif c <= 10 and weather == "Clouds":
            Frame(w, width=800, height=350, bg="#7492B3").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open(cloudcold_img_path))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#7492B3"
            fcolor = "white"
        
        elif c > 10 and weather == "Rain":
            Frame(w, width=800, height=350, bg="#60789E").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open(rain_img_path))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#60789E"
            fcolor = "white"
        
        elif c <= 10 and weather in ["Fog", "Clear"]:
            Frame(w, width=800, height=350, bg="#white").place(x=0, y=50)
            imgWeather = ImageTk.PhotoImage(Image.open(cold_img_path))
            Label(w, image=imgWeather, border=0).place(x=170, y=130)
            bcolor = "#white"
            fcolor = "black"
        
        else:
            Frame(w, width=800, height=350, bg="#white").place(x=0, y=50)
            label = Label(w, text=weather, border=0, bg='white')
            label.configure(font=("Calibri", 18))
            label.place(x=160, y=130)
            bcolor = "white"
            fcolor = "black"
        
        h = "Humidity: {}".format(result['main']['humidity'])
        p = "Pressure: {}".format(result['main']['pressure'])
        tempMax = "MAX Temp: {}".format(result['main']['temp_max'])
        tempMin = "MIN Temp: {}".format(result['main']['temp_min'])
        wSpeed = "Wind Speed: {} m/s".format(result['wind']['speed'])
        
        l2 = Label(w, text=str(month + " " + today), bg=bcolor, fg=fcolor)
        l2.config(font=("Calibri", 25))
        l2.place(x=330, y=335)
        
        l3 = Label(w, text=str(h) + "%", bg=bcolor, fg=fcolor)
        l3.config(font=("Calibri", 12))
        l3.place(x=510, y=95)
        
        l3 = Label(w, text=str(p) + " hPa", bg=bcolor, fg=fcolor)
        l3.config(font=("Calibri", 12))
        l3.place(x=510, y=135)
        
        l3 = Label(w, text=str(tempMin) + " °C", bg=bcolor, fg=fcolor)
        l3.config(font=("Calibri", 12))
        l3.place(x=510, y=175)
        
        l3 = Label(w, text=str(tempMax) + " °C", bg=bcolor, fg=fcolor)
        l3.config(font=("Calibri", 12))
        l3.place(x=510, y=215)
        
        l3 = Label(w, text=str(wSpeed), bg=bcolor, fg=fcolor)
        l3.config(font=("Calibri", 12))
        l3.place(x=510, y=255)
        
        l3 = Label(w, text=str(c) + " °C", bg=bcolor, fg=fcolor)
        l3.config(font=("Calibri", 42))
        l3.place(x=510, y=150)
    
    label("Los Angeles")
    
    def cmd1():
        b = str(el.get())
        label(str(b))
    
    Button(w, image=imgSearch, command=cmd1, border=0).place(x=750, y=10)

except Exception as e:
    Frame(w, width=800, height=400, bg='white').place(x=0, y=0)
    try:
        imgNoInternet = ImageTk.PhotoImage(Image.open(no_internet_img_path))
        Label(w, image=imgNoInternet, border=0).pack(expand=True)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {no_internet_img_path}")
    print(e)

w.mainloop()
