import os
import random
import smtplib
import datetime as dt

import pandas as pd


def get_message(a_name):
    letter_filename = random.choice(('letter_1.txt', 'letter_2.txt', 'letter_3.txt'))
    with open(f'letter_templates/{letter_filename}') as file:
        letter = file.read()
    return f"Subject:Happy Birthday!\n\n{letter.replace('[NAME]', a_name)}"


def send_email(a_name, to_email):
    from_email = os.getenv('EMAIL')
    password = os.getenv('EMAIL_PASS')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email,
                            to_addrs=to_email,
                            msg=get_message(a_name))


df = pd.read_csv('birthdays.csv')
now = dt.datetime.now()
birthdays = {row['name']: row.email for _, row in df.iterrows() if row.month == now.month and row.day == now.day}
for name, email in birthdays.items():
    send_email(name, email)
