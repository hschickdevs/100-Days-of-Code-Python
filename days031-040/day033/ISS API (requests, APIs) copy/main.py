from tkinter import *
from algorithm import Tracker
from mail_client import send_mail
from haversine import haversine_distance, to_mi

FONT = ("Arial", 18, "normal")

# Main Window Setup
main_window = Tk()
main_window.title("ISS PROXIMITY TRACKER")
main_window.config(padx=50, pady=50, bg="white")
# Main Window Canvas Setup
iss_logo = PhotoImage(file="ISS_logo.png")
canvas = Canvas(width=640, height=419, bg="white", highlightthickness=0)
canvas.create_image((640 / 2), (419 / 2), image=iss_logo)
canvas.grid(row=0, column=0, columnspan=3)
# Main Window Entries:
location_lat_entry = Entry(width=15)
location_lat_entry.insert(0, "Enter Latitude...")
location_lat_entry.grid(row=1, column=0, sticky="e")
location_name_entry = Entry(width=25)
location_name_entry.insert(0, "Location Name...")
location_name_entry.grid(row=1, column=1)
location_lon_entry = Entry(width=15)
location_lon_entry.insert(0, "Enter Longitude...")
location_lon_entry.grid(row=1, column=2, sticky="w")

# secondary window setup:
secondary_window = Tk()
secondary_window.title(location_name_entry.get())
secondary_window.minsize(500, 200)
secondary_window.config(padx=25, pady=25)
# Labels:
longitude_label = Label(master=secondary_window, text="Longitude", bg="white", font=("Arial", 18, "underline"))
longitude_label.grid(row=0, column=1)
latitude_label = Label(master=secondary_window, text="Latitude", bg="white", font=("Arial", 18, "underline"))
latitude_label.grid(row=0, column=2)
# Input information labels:
user_location_label = Label(master=secondary_window, text="User Location:", bg="white", font=FONT)
user_location_label.grid(row=1, column=0, sticky="e")
user_location_lon_label = Label(master=secondary_window, text="0˚", bg="white", font=FONT)
user_location_lon_label.grid(row=1, column=1)
user_location_lat_label = Label(master=secondary_window, text="0˚", bg="white", font=FONT)
user_location_lat_label.grid(row=1, column=2)
# ISS Information Labels
iss_location_label = Label(master=secondary_window, text="ISS Location:", bg="white", font=FONT)
iss_location_label.grid(row=2, column=0, sticky="e")
iss_location_lon_label = Label(master=secondary_window, text="0˚", bg="white", font=FONT)
iss_location_lon_label.grid(row=2, column=1)
iss_location_lat_label = Label(master=secondary_window, text="0˚", bg="white", font=FONT)
iss_location_lat_label.grid(row=2, column=2)
iss_distance_from_user_label = Label(master=secondary_window, text="ISS Distance from User:", bg="white", font=FONT)
iss_distance_from_user_label.grid(row=3, column=0, sticky="e")
iss_distance_in_miles_label = Label(master=secondary_window, text="0 Mi", bg="white", font=FONT)
iss_distance_in_miles_label.grid(row=3, column=1)
iss_distance_in_km_label = Label(master=secondary_window, text="0 Km", bg="white", font=FONT)
iss_distance_in_km_label.grid(row=3, column=2)
# # Checkbutton
# email_checkbutton = Checkbutton(master=secondary_window, text="Email Notifications", font=FONT)
# email_checkbutton.grid(row=4, column=1, columnspan=2)

# Init iss tracker class
iss_tracker = Tracker()


# Function to keep the program checking for the location every 6 seconds:
def get_iss_location(user_lon, user_lat):
    proximity_data = iss_tracker.check_proximity(my_longitude=user_lon, my_latitude=user_lat)
    iss_lat = proximity_data[1]
    iss_lon = proximity_data[2]
    dist_km = haversine_distance(user_lat, user_lon, iss_lat, iss_lon)
    dist_mi = to_mi(dist_km)

    # Update the UI:
    user_location_lon_label.config(text=f"{round(user_lon)}˚")
    user_location_lat_label.config(text=f"{round(user_lat)}˚")
    iss_location_lon_label.config(text=f"{round(iss_lon)}˚")
    iss_location_lat_label.config(text=f"{round(iss_lat)}˚")
    iss_distance_in_km_label.config(text=f"{round(dist_km)} km")
    iss_distance_in_miles_label.config(text=f"{round(dist_mi)} mi")

    # If ISS is nearby and mail notifications are enabled, send email.

    # iss_location_lon_label.config(text=f"{iss}")


def clear_entries():
    # secondary_window.after_cancel()
    location_lat_entry.delete(0, END)
    location_lon_entry.delete(0, END)
    location_name_entry.delete(0, END)
    location_lat_entry.insert(0, "Enter Latitude...")
    location_lon_entry.insert(0, "Enter Longitude...")
    location_name_entry.insert(0, "Location Name...")


# Function to change the user's location.
def set_location():
    secondary_window.title(location_name_entry.get())
    try:
        user_lat = float(location_lat_entry.get())
        user_lon = float(location_lon_entry.get())
    except ValueError:
        print("USER LOCATION VALUE ERROR. Default set to 0,0")
        user_lat = 0
        user_lon = 0
    get_iss_location(user_lon, user_lat)
    # clear_entries() disabled since button changed to update location


# Button to set user location
btn = Button(main_window, text="Update Data", width=22, command=set_location)
btn.grid(row=2, column=1, padx=20, pady=20)

# mainloop, runs infinitely
secondary_window.mainloop()
main_window.mainloop()
