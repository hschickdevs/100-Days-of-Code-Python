import os
import smtplib

from_email = os.getenv('EMAIL')
password = os.getenv('EMAIL_PASS')
to_email = os.getenv('OTHER_EMAIL')

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=from_email, password=password)
    connection.sendmail(from_addr=from_email,
                        to_addrs=to_email,
                        msg="Subject:Hello\n\nThis is the body of my other email!")
