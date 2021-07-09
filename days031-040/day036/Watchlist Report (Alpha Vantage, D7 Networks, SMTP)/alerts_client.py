import smtplib
import requests


# ----------- CREATE THE STRING ----------- #
def create_message(ticker_symbol, articles, percent_change, movement):
    message_string = f"ALERT: ${ticker_symbol}: {movement} {percent_change}%\n\n"

    if len(articles) > 0:
        try:
            message_string += articles
        except TypeError:
            message_string += "No headline news found."
    else:
        message_string += "No headline news related to the stock's movement found."

    return message_string


# -------------- FOR EMAIL ---------------- #
def send_email(from_email, from_password, to_email, message, ticker_symbol):
    print("Preparing Email Client..")
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        print("\nEmail connection established...")
        connection.starttls()
        print("tls on...")
        connection.login(user=from_email, password=from_password)
        print("login successful...")
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject: STOCK ALERT FOR {ticker_symbol}!\n\n{message}"
        )
        print(f"Mail Sent Successfully")


# ---------------- FOR SMS ------------------ #
url = "https://http-api.d7networks.com/send"

querystring = {
    "username": "D7_NETWORKS_USERNAME",
    "password": "D7_NETWORKS_PASSWORD",
    "from": "Stock Alert",
    "content": str,
    "dlr-method": "POST",
    "dlr-url": "https://4ba60af1.ngrok.io/receive",
    "dlr": "yes",
    "dlr-level": "3",
    "to": "YOUR_PHONE_NUMBER"
}
headers = {
    'cache-control': "no-cache"
}


def send_sms(message):
    querystring["content"] = message
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
