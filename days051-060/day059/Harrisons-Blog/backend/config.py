from os import getenv

# Blog Posts Config:
# BLOG_URL = "https://api.npoint.io/d9f83de217d4c0cc9a66" <- deprecated in favor of SQLITE database

# ADMINISTRATOR CONFIG:
ADMINISTRATOR_USERNAME = getenv("ADMINISTRATOR_USERNAME", default="<or_hardcode_here>")  # Password = testpass

# SendGrid Config:
SENDGRID_APIKEY = getenv("SENDGRID_APIKEY", default="<or_hardcode_here>")
SENDGRID_FROM_EMAIL = getenv(key="SENDGRID_FROM_EMAIL", default="<or_hardcode_here>")
SENDGRID_TO_EMAIL = getenv(key="SENDGRID_TO_EMAIL", default="<or_hardcode_here>")
