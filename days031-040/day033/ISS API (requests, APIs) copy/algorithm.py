import requests
from datetime import datetime


class Tracker:
    def check_proximity(self, my_longitude, my_latitude):
        # Call the API
        response = requests.get(url="http://api.open-notify.org/iss-now.json")

        # Check to see if the API was able to get the data that we wanted
        response.raise_for_status()

        # turn the API response data into an iterable dict from the JSON
        response_data = response.json()

        # UTILIZE THE ISS DATA:
        iss_lon = float(response_data["iss_position"]["longitude"])
        iss_lat = float(response_data["iss_position"]["latitude"])
        print(f"The ISS is at: {iss_lat} lat and {iss_lon} lon.")

        my_parameters = {
            "lat": my_latitude,
            "lng": my_longitude,
            "formatted": 0
        }

        # BONUS: run the code every 60 seconds.
        # Your position is within +5 or -5 degrees of the ISS position.
        def iss_is_nearby():
            if (my_parameters["lat"] - 5) <= iss_lat <= (my_parameters["lat"] + 5) and (
                    my_parameters["lng"] - 5) <= iss_lon <= (
                    my_parameters["lng"] + 5):
                return True
            else:
                return False

        # Get sun and time data:
        # sun_status_response = requests.get("https://api.sunrise-sunset.org/json", params=my_parameters)
        # response.raise_for_status()
        # sun_data = sun_status_response.json()
        # sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
        # sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
        #
        # hour_now = datetime.now().hour
        #
        # def is_dark():
        #     if sunset < hour_now < sunrise:
        #         return True
        #     else:
        #         return False

        # check if it's dark and the ISS is nearby
        if iss_is_nearby():  # and is_dark():
            return [True, iss_lat, iss_lon]
        else:
            return [False, iss_lat, iss_lon]