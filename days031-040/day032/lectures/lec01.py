import os
import smtplib

from_email = os.getenv('EMAIL')
password = os.getenv('EMAIL_PASS')
to_email = os.getenv('OTHER_EMAIL')

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=from_email, password=password)
connection.sendmail(from_addr=from_email, to_addrs=to_email, msg="Hello!")
connection.close()
