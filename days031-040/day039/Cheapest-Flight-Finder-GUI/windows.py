import tkinter.ttk
from tkinter import *
from tkinter import messagebox
import webbrowser
from datetime import datetime


# https://www.tutorialspoint.com/how-to-create-a-hyperlink-with-a-label-in-tkinter

class MainMenu(Tk):
    def __init__(self, search_func):
        super().__init__()
        self.title("Cheapest Flights Finder")
        self.config(padx=10, pady=15)

        # Logo Image:
        self.logo = PhotoImage(file="image_assets/menu_icon.png")
        self.canvas = Canvas(master=self, width=320, height=320)
        self.canvas.create_image((160, 160), image=self.logo)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Entries
        self.departure_city_entry = PlaceholderEntry(self, "Departure City...")
        self.departure_city_entry.grid(row=2, column=0, pady=2.5, columnspan=2)
        self.arrival_city_entry = PlaceholderEntry(self, "Arrival City...")
        self.arrival_city_entry.grid(row=3, column=0, pady=2.5, columnspan=2)
        self.from_date_entry = PlaceholderEntry(self, "From (dd/mm/yyyy)...")
        self.from_date_entry.grid(row=4, column=0, pady=2.5, columnspan=2)
        self.to_date_entry = PlaceholderEntry(self, "To (dd/mm/yyyy)...")
        self.to_date_entry.grid(row=5, column=0, pady=2.5, columnspan=2)
        self.email_entry = PlaceholderEntry(self, "Enter Email...")
        self.email_entry.grid(row=10, column=0, pady=2.5, columnspan=2)
        self.nights_in_dest_entry = PlaceholderEntry(self, "Nights in Destination...")
        self.nights_in_dest_entry.grid(row=6, column=0, pady=2.5, columnspan=2)

        # Search button
        self.search_button = Button(master=self, width=21, text="Search Flights", bg="#53A1DB", command=search_func)
        self.search_button.grid(row=8, column=0, pady=5, columnspan=2)

        # Checkboxes
        self.airports = IntVar()
        self.airports_checkbutton = Checkbutton(text="Use Airport Codes", variable=self.airports)
        self.airports_checkbutton.grid(row=1, column=0, columnspan=2, pady=2.5)
        self.emails_on = IntVar()
        self.emails_checkbutton = Checkbutton(text="Receive Emailed Report", variable=self.emails_on)
        self.emails_checkbutton.grid(row=11, column=0, columnspan=2, pady=2.5)
        self.layovers_on = IntVar()
        self.layovers_checkbutton = Checkbutton(text="Allow Layovers", variable=self.layovers_on)
        self.layovers_checkbutton.grid(row=7, column=1, pady=2.5, sticky="w")
        self.roundtrip_on = IntVar()
        self.roundtrip_checkbutton = Checkbutton(text="Roundtrip", variable=self.roundtrip_on)
        self.roundtrip_checkbutton.grid(row=7, column=0, pady=2.5, sticky="e")

        # Instructions Label:
        self.instructions = Label(master=self,
                                  text="Note: For comp searches, separate each city name, departure, and arrival date with a comma and no spaces.",
                                  wraplength=190,
                                  justify="left")
        self.instructions.grid(row=9, column=0, pady=2.5, columnspan=2)

    #     # Listbox Selector
    #     self.listbox_selection = StringVar()
    #     self.flight_types_listbox = Listbox(height=2)
    #     flight_types = ["Direct", "Multicity"]
    #     for item in flight_types:
    #         self.flight_types_listbox.insert(flight_types.index(item), item)
    #     self.flight_types_listbox.select_set(0)
    #     self.listbox_selection = self.flight_types_listbox.get(self.flight_types_listbox.curselection())
    #     self.flight_types_listbox.bind("<<ListboxSelect>>", self.listbox_used)
    #     self.flight_types_listbox.grid(row=6, column=0, pady=2.5, columnspan=2)
    #
    # def listbox_used(self, event):
    #     self.listbox_selection = self.flight_types_listbox.get(self.flight_types_listbox.curselection())

    def get_tk_entries(self):
        departures_list = self.departure_city_entry.get().split(",")
        arrivals_list = self.arrival_city_entry.get().split(",")
        from_dates_list = self.from_date_entry.get().split(",")
        to_dates_list = self.to_date_entry.get().split(",")
        emails = self.emails_on.get()
        layovers = self.layovers_on.get()
        roundtrip = self.roundtrip_on.get()
        airport_codes = self.airports.get()

        try:
            nights_in_destination = int(self.nights_in_dest_entry.get())
        except ValueError:
            nights_in_destination = 0

        flights_information = {
            "departure_cities": departures_list,
            "arrival_cities": arrivals_list,
            "from_dates": from_dates_list,
            "to_dates": to_dates_list,
        }

        if "@" in self.email_entry.get():
            to_email = self.email_entry.get()
            if emails > 0:
                emails = True
            else:
                emails = False
        else:
            to_email = ""
            emails = False
            self.emails_on = IntVar()

        if layovers > 0:
            layovers = True
        else:
            layovers = False

        if roundtrip > 0:
            trip_type = "round"
        else:
            trip_type = "oneway"

        if airport_codes > 0:
            airport_codes = True
        else:
            airport_codes = False

        tk_data = {
            "airport_codes": airport_codes,
            "flights_information": flights_information,
            # "max_price": max_ticket_price,
            "emails": emails,
            "layovers": layovers,
            "trip_type": trip_type,
            "to_email": to_email,
            "nights_in_destination": nights_in_destination
        }

        return tk_data


class PlaceholderEntry(Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.placeholder = placeholder

        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, e):
        self.delete("0", "end")

    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)


now = datetime.now()


class DirectReportToplevel(Tk):
    def __init__(self, data: dict):
        super().__init__()
        self.title(f"{now} Report")
        self.config(padx=25, pady=25)
        self.report_label = Label(master=self, text=self.create_report(data))
        self.report_label.grid(row=0, column=0, pady=5)
        self.url_button = Button(master=self, text="View Flight Online", command=lambda: self.callback(data['deep_link']),
                                 width=20)
        self.url_button.grid(row=1, column=0, pady=5)
        self.close_button = Button(master=self, text="Close Window", width=20, command=self.destroy)
        self.close_button.grid(row=2, column=0, pady=5)

    def callback(self, url):
        webbrowser.open_new(url=url)

    def create_report(self, data: dict):
        from_city = data['cityFrom']
        from_airport = data['flyFrom']
        to_city = data['cityTo']
        to_airport = data['flyTo']
        price = data['price']
        flight_availability = data['availability']['seats']
        flights_in_route = data['route']
        departure_time = data['local_departure'][:10]

        report_string = f"From: {from_city} ({from_airport})\n\n" \
                        f"To: {to_city} ({to_airport})\n\n" \
                        f"Departs: {departure_time}\n\n" \
                        f"Connecting Flights: {len(flights_in_route) - 1}\n\n" \
                        f"Price: ${price}\n\n" \
                        f"Flight Availability: {flight_availability}"

        return report_string


class MulticityReportToplevel(Tk):
    def __init__(self, flights_data: dict):
        super().__init__()
        self.title(f"{now} Report")
        self.config(padx=25, pady=25)
        self.report_label = Label(master=self, text=self.create_report(flights_data))
        self.report_label.grid(row=0, column=0, pady=5)
        self.url_button = Button(master=self, text="View Flights Online", command=lambda: self.callbacks(flights_data),
                                 width=20)
        self.url_button.grid(row=1, column=0, pady=5)
        self.close_button = Button(master=self, text="Close Window", width=20, command=self.destroy)
        self.close_button.grid(row=2, column=0, pady=5)

    def callbacks(self, flights_data):
        url_list = [report['deep_link'] for report in flights_data]
        for url in url_list:
            webbrowser.open_new(url=url)
            print(url)

    def create_report(self, flights_data):
        report_string = ""
        for report in flights_data:
            from_city = report['cityFrom']
            from_airport = report['flyFrom']
            to_city = report['cityTo']
            to_airport = report['flyTo']
            price = report['price']
            flight_availability = report['availability']['seats']
            flights_in_route = report['route']
            departure_time = report['local_departure'][:10]

            report = f"From: {from_city} ({from_airport})\n" \
                     f"To: {to_city} ({to_airport})\n" \
                     f"Departs: {departure_time}\n" \
                     f"Connecting Flights: {len(flights_in_route) - 1}\n" \
                     f"Price: ${price}\n" \
                     f"Flight Availability: {flight_availability}\n\n"
            report_string += report

        return report_string


class RoundtripReportToplevel(Tk):
    # for roundtrip in roundtrips:

    pass
