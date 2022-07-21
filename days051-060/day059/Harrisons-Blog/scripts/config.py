from os import getenv

# Blog Posts Config:
BLOG_URL = "https://api.npoint.io/d9f83de217d4c0cc9a66"

# SendGrid Config:
SENDGRID_APIKEY = getenv("SENDGRID_APIKEY", default="<or_hardcode_here>")
SENDGRID_FROM_EMAIL = getenv(key="SENDGRID_FROM_EMAIL", default="<or_hardcode_here>")
SENDGRID_TO_EMAIL = getenv(key="SENDGRID_TO_EMAIL", default="<or_hardcode_here>")

# Assertions
assert not any(v == "<or_hardcode_here>" for v in [SENDGRID_APIKEY, SENDGRID_FROM_EMAIL, SENDGRID_TO_EMAIL])
