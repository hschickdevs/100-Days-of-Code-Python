import smtplib

email = "bot_email"
password = "bot_email_password"


def send_mail(to_email):
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to_email,
                            msg="Subject: ISS ALERT!\n\nThe ISS is visible overhead!")
        print(f"Alert email send to {to_email}.")
