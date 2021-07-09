import os
import random
import smtplib
import datetime as dt


def get_message():
    with open('quotes.txt') as file:
        lines = file.readlines()
    return f'Subject: Motivational Friday!\n\n{random.choice(lines)}'


def day_of_week():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    now = dt.datetime.now()
    return weekdays[now.weekday()]


def send_email(message):
    from_email = os.getenv('EMAIL')
    to_email = os.getenv('OTHER_EMAIL')
    password = os.getenv('EMAIL_PASS')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email,
                            to_addrs=to_email,
                            msg=message)


if day_of_week() == 'Friday':
    send_email(get_message())
