from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
  
       
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + ",PK&appid=f29c602910a4551d2bd9c3cc38450d14&units=metric").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
        # Since units=metric is used, temp is already in Celsius. Removed -273.15
    temp_label1.config(text=str(data["main"]["temp"]) + " °C")
    per_label1.config(text=str(data["main"]["pressure"]) + " hPa")
   
      

win = Tk()  # Fixed: changed from ttk() to Tk()
win.title("tooba's coding")   
win.config(bg='blue')
win.geometry("500x570")

name_label = Label(win, text="tooba's weather app", font=('Times New Roman', 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
List_name = [
    "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad", 
    "Multan", "Peshawar", "Quetta", "Hyderabad", "Sukkur", 
    "Sialkot", "Bahawalpur", "Gujranwala", "Abbottabad", "Larkana", 
    "Mirpur", "Mardan", "Swat", "Mingora", 
    "Muzaffarabad", "Gilgit", "Skardu", "Chitral", "Mansehra", 
    "Haripur", "Dera Ismail Khan", "Bannu", "Kohat", "Nowshera", 
    "Charsadda", "Swabi", "Timergara", "Karak", "Hangu", 
    "Tank", "Daggar", "Buner", "Shangla", "Alpuri", 
    "Battagram", "Kohistan", "Dir", "Malakand", 
    "Sargodha", "Gujrat", "Sahiwal", "Jhang", "Rahim Yar Khan", 
    "Sheikhupura", "Kasur", "Okara", "Wah Cantonment", 
    "Dera Ghazi Khan", "Chiniot", "Kamoke", "Hafizabad", "Sadiqabad", 
    "Burewala", "Khanewal", "Muzaffargarh", "Mandi Bahauddin", "Toba Tek Singh", 
    "Khanpur", "Dadu", "Jacobabad", "Shikarpur", "Tando Adam", 
    "Khairpur", "Ghotki", "Kashmore", "Badin", "Sanghar", "Umerkot"
]

com = ttk.Combobox(win, values=List_name, font=('Times New Roman', 20, 'bold'), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# Weather Climate Labels
w_label = Label(win, text="Weather Climate", font=('Times New Roman', 20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Times New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

# Weather Description Labels
wb_label = Label(win, text="Weather Desc", font=('Times New Roman', 20))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", font=("Times New Roman", 20))
wb_label1.place(x=250, y=330, height=50, width=210)

# Temperature Labels
temp_label = Label(win, text="Temperature", font=("Times New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text='', font=("Times New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

# Pressure Labels
per_label = Label(win, text="Pressure", font=("Times New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)
per_label1 = Label(win, text="", font=("Times New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done", font=('Times New Roman', 20, "bold"), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()