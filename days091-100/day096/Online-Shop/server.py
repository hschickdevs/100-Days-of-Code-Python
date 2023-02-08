import os

from flask import Flask, redirect
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY', '<OR_HARDCODE_KEY_HERE>')
assert stripe.api_key != '<OR_HARDCODE_KEY_HERE>', 'Stripe API key not supplied.'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'


@app.route('/')
def home():
    return redirect(YOUR_DOMAIN + '/checkout.html')


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': '<YOUR_PRICE_OBJECT_ID>',  # See here: https://stripe.com/docs/api/checkout/sessions/create
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


if __name__ == '__main__':
    app.run(port=4242)