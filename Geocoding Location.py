from tkinter import *
from geopy.geocoders import Nominatim
import folium


# location1 = geolocator.geocode(str(e1.get()))

def get_landmark():
    try:

        geolocator = Nominatim(user_agent="geoapiExercises")
        location1 = geolocator.geocode(str(e1.get()))

        global Loc1_lat, Loc1_lon
        Loc1_lat, Loc1_lon = location1.latitude, location1.longitude

        location1 = (Loc1_lat, Loc1_lon)

        res1 = str((location1))

        result.set(res1)


    except:
        result.set("someting went wrong")


def generate_map():
    m = folium.Map(location=[Loc1_lat, Loc1_lon], zoom_start=15)
    folium.Marker(location=[Loc1_lat, Loc1_lon]).add_to(m)
    m.save('Landmark.html')


# object of tkinter
# with background set to light grey
master = Tk()
master.configure(bg='light grey')
master.title("Geocoding Locations")

# Variable Classes in tkinter
result = StringVar();

# Creating label for each information
# name using widget Label
Label(master, text="Landmark: ", bg="light grey").grid(row=1, sticky=W)

Label(master, text="Result :", bg="light grey").grid(row=3, sticky=W)

# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result, bg="light grey").grid(row=3, column=1, sticky=W)

e1 = Entry(master, width=50)
e1.grid(row=1, column=1)

# creating a button using the widget
b = Button(master, text="Show", command=get_landmark, bg="white")
b.grid(row=1, column=2, columnspan=1, rowspan=1, padx=2.5, pady=2.5, )
b1 = Button(master, text="GenerateMap", command=generate_map, bg="white")
b1.grid(row=1, column=3, columnspan=1, rowspan=1, padx=2.5, pady=2.5, )

mainloop()
