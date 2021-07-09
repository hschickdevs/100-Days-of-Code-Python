import os
from twilio.rest import Client


class NotificationManager:
    def __init__(self, flights):
        self.flights = flights

    def send_messages(self):
        client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        for flight in self.flights:
            msg = f'🚨✈️ Low price alert!🚨✈\nOnly £{flight.price} to fly from {flight.city_from}-{flight.fly_from}' \
                  f'to {flight.city_to}-{flight.fly_to}, from {flight.departure} to {flight.arrival}'
            client.messages.create(
                body=msg,
                from_=os.getenv('TWILIO_NUMBER'),
                to=os.getenv('MY_NUMBER'))
