from flask import Flask
import random

from .user import User

app = Flask(__name__)

rand_int = random.randint(1, 10)

# Decorators
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_center(fn):
    def wrapped():
        return "<center>" + fn() + "</center>"
    return wrapped

def is_authenticated(fn):
    """Expects the args[0] to be a User object"""
    def wrapped(*args, **kwargs):
        if args[0].is_logged_in == True:
            return fn(*args, **kwargs)
    return wrapped


@app.route("/")
@make_bold
@make_underline
@make_italic
@make_center
def home():
    return "Guess a number between 1 and 10!"


@app.route("/<int:number>")
def check_guess(number):
    if number == rand_int:
        return "<h2>You got it!</h2>" \
               "<img src=https://media3.giphy.com/media/xUPGcMzwkOY01nj6hi/giphy.gif>"
    elif number < rand_int:
        return "<h2>Too low!</h2>" \
               "<img src=https://media.tenor.com/images/af19accc741384df9922db01fc5b32da/tenor.gif>"
    elif number > rand_int:
        return "<h2>Too high!</h2>" \
               "<img src=https://media3.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif>"


@app.route("/stonks")
def stonks():
    return f'<h1>STONKS</h1>' \
           f'<br>' \
           f'<img src=https://media.tenor.com/images/a90e5f63a60f52f36b3bd4f701e3083b/tenor.gif>'


if __name__ == "__main__":
    app.run(debug=True)  # Debug set to on (True) so that we can change the code while the app is running
