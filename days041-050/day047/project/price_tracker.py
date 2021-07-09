import os
import smtplib

import lxml
import requests

from bs4 import BeautifulSoup


def send_email(item, price, link):
    email = os.getenv('EMAIL')
    password = os.getenv('EMAIL_PASS')
    message = f"Subject: 🚨 Low Price Alert 🚨\n\n{item} is now ${price:.2f}. Buy now!\n{link}".encode('utf-8')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=message)


url = 'https://www.amazon.com/Magicians-Trilogy-Boxed-Set-Magician/dp/0147517389/'
headers = {
    'USER-AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'ACCEPT-LANGUAGE': 'en-US,en;q=0.9,pt;q=0.8'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

title = soup.find('span', id='productTitle').getText()
price = float(soup.find('span', id='price').getText().strip('$'))

if price < 40:
    send_email(title, price, url)
