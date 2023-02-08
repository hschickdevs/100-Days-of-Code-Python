# Finnhub Setup
RATE_LIMIT = (60, 60)  # (calls per period (seconds), period (seconds))

# Emails Client Setup:
SMTP_SERVER_ADDRESS = "smtp.mail.yahoo.com"
SMTP_SERVER_PORT = 465












# STATIC SETTINGS - IGNORE:
REQUIRED_ENVARS = ["FINNHUB_APIKEY", "FROM_EMAIL", "FROM_EMAIL_PASSWORD"]
MANDATORY_SHEET_COLUMNS = ["Symbol", "Entry Price", "Shares"]