import os
import smtplib
from twilio.rest import Client


class NotificationManager:
    def __init__(self, flights):
        self.flights = flights
        self.messages = []
        for flight in self.flights:

            msg = f'️Low price alert!\nOnly £{flight.price} to fly from {flight.city_from}-{flight.fly_from} ' \
                  f'to {flight.city_to}-{flight.fly_to}, from {flight.departure} to {flight.arrival}'
            if flight.stop_overs == 1:
                msg += f'Flight has 1 stop over, via {flight.via_city}.'
            msg += f'\nLink: https://www.google.co.uk/flights?hl=en#flt={flight.fly_from}.{flight.fly_to}.' \
                   f'{flight.departure}*{flight.fly_to}.{flight.fly_from}.{flight.arrival}'

            self.messages.append(msg)

    def send_messages(self):
        client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        for msg in self.messages:
            client.messages.create(
                body=msg,
                from_=os.getenv('TWILIO_NUMBER'),
                to=os.getenv('MY_NUMBER'))

    def send_emails(self, emails):
        from_email = os.getenv('EMAIL')
        password = os.getenv('EMAIL_PASS')
        for msg in self.messages:
            msg = 'Subject: Flight Club Notification\n\n' + msg
            msg = msg.encode('utf-8')
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=from_email, password=password)
                connection.sendmail(from_addr=from_email,
                                    to_addrs=emails,
                                    msg=msg)
