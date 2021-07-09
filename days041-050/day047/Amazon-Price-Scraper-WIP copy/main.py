import time
from random import randint
from amazon_scraper import get_price
import PySimpleGUI as sg
import yaml

with open("settings.yaml", "r") as s:
    settings = yaml.load(s, Loader=yaml.FullLoader)
urls = [url for url in settings['urls']]

while True:
    for url in urls:
        response = get_price(url)
        print(f"URL: {url}")
        print(f"Current Price: {response[0]}")
        print(f"Remaining Stock: {response[1]}\n")
    time.sleep(randint(0,2))

# -------- DEPRICATED GUI -------- #
# # Define the window's contents
# layout = [[sg.Text("Input Amazon Item URL:")],
#           [sg.Input(key='-INPUT-')],
#           [sg.Text(size=(40, 1), key='-OUTPUT-')],
#           [sg.Submit(), sg.Button('Quit'), sg.Button('Clear')]]
#
# # Create the window
# window = sg.Window('Window Title', layout)
#
# while True:
#     event, values = window.read()
#     # See if user wants to quit or window was closed
#     if event == sg.WINDOW_CLOSED or event == 'Quit':
#         break
#     elif event == "Submit":
#         window['-OUTPUT-'].update("Url: " + values['-INPUT-'])
#         response = get_price(values['-INPUT-'])
#         print(response)
#     elif event == "Clear":
#         window['-INPUT-'].update("")
#
# # Finish up by removing from the screen
# window.close()