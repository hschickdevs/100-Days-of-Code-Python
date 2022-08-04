import requests

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

from .config import *

sendgrid_cli = SendGridAPIClient(api_key=SENDGRID_APIKEY)


def send_contact_email(_subject: str, _message: str):
    formatted_mail = Mail(from_email=Email(SENDGRID_FROM_EMAIL),
                          to_emails=[SENDGRID_TO_EMAIL],
                          subject=_subject, plain_text_content=_message)

    sendgrid_cli.client.mail.send.post(request_body=formatted_mail.get())
