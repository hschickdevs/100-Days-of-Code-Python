import smtplib


class NotificationManager:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_mail(self, to_email, message, from_city, to_city):
        print("Preparing Email Client..")
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            print("\nEmail connection established...")
            connection.starttls()
            print("tls on...")
            connection.login(user=self.email, password=self.password)
            print("login successful...")
            connection.sendmail(
                from_addr=self.email,
                to_addrs=to_email,
                msg=f"Subject: Cheapest Flight from {from_city} to {to_city}\n\n{message}"
            )
            print(f"Mail Sent Successfully")
