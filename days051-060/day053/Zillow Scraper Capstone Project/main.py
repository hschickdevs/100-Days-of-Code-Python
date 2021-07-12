import os
import PySimpleGUI as sg
from scraper import ZillowScraper
import webbrowser

chrome_driver_path = "/Users/harrison/Desktop/Python Career/Chrome-Webdriver/chromedriver"

scraper = ZillowScraper(chrome_driver_path)

sg.theme('Reddit')

layout = [
    [sg.Text(size=(10, 1)), sg.Image(filename="image_assets/Zillow.png"), sg.Text(size=(10, 1))],
    [sg.Text(size=(5, 1)), sg.Text('City, STATE?', size=(10, 1)), sg.Text(size=(9, 1)), sg.Text('Max Price?')],
    [sg.Text(size=(5, 1)), sg.Input('Dallas, TX', key='-LOCATION-', size=(17, 1)), sg.Text(size=(2, 1)),
     sg.Input('$500,000', key='-MAXPRICE-', size=(17, 1))],
    [sg.Text()],
    [sg.Text("Buy or Rent?", size=(16, 1)), sg.Text("Bedrooms?", size=(16, 1)), sg.Text("Bathrooms?", size=(16, 1))],
    [sg.Listbox(key='-BUYRENT-', default_values=['Rent'], values=['Rent', 'Buy'], size=(15, 4)),
     sg.Listbox(key='-BEDROOMS-', default_values=['Any'], values=['Any', '1+', '2+', '3+', '4+', '5+'], size=(15, 4)),
     sg.Listbox(key='-BATHROOMS-', default_values=['Any'], values=['Any', '1+', '1.5+', '2+', '3+', '4+'],
                size=(15, 4))],
    [sg.Text("", key='-NOTIFICATION-', justification='center', size=(50, 1))],
    [sg.Text(size=(13, 1)), sg.Button('SEARCH', size=(21, 1)), sg.Text(size=(14, 1))]
]

window = sg.Window('ZILLOW WEB SCRAPER', layout, font=('Arial', 20, 'normal'))


def progress_gui():
    pass


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "SEARCH":
        location = values['-LOCATION-']
        max_price = values['-MAXPRICE-'].replace("$", "").replace(",", "")
        buy_rent = values['-BUYRENT-'][0]
        bedrooms = values['-BEDROOMS-'][0]
        bathrooms = values['-BATHROOMS-'][0]

        print(f"Query: {location} | ${max_price} | {buy_rent} | Bed: {bedrooms} | Bath: {bathrooms}")

        results = scraper.scrape_properties(location=location, max_price=max_price, buy_or_rent=buy_rent,
                                            beds=bedrooms, baths=bathrooms)
        print(results)
        window['-NOTIFICATION-'].update(f"Fetch success for {location}!")


window.close()
