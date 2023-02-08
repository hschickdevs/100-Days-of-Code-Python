import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ._config import SMTP_SERVER_ADDRESS, SMTP_SERVER_PORT


def send_email(subject: str, content: str, _to: list[str], _from: str, password: str, content_type="html"):
    assert content_type == "html", f"{content_type} is not a currently supported content type."

    try:
        # Create smtp auth server:
        server = smtplib.SMTP_SSL(SMTP_SERVER_ADDRESS, SMTP_SERVER_PORT)
        # server.starttls()  # <-- Yahoo mail does not require TLS, and instead requires the SSL SMTP server
        server.login(_from, password)
    except Exception as exc:
        raise ConnectionError(f"An error occurred when attempting to login to SMTP: {exc}")

    try:
        # Send emails to each specified recipient:
        for to_email in _to:
            print(f"Sending email to {to_email}...")
            # Build message container
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = _from
            msg['To'] = to_email
            content = MIMEText(content, content_type)
            msg.attach(content)

            # Send email using the SMTP server specified in CONFIG
            server.sendmail(from_addr=_from, to_addrs=to_email, msg=msg.as_string())
    except Exception as exc:
        raise Exception(f"An error occurred when attempting to send the email: {exc}")
    finally:
        server.quit()
