from flask import Flask
import random

app = Flask(__name__)

rand_int = random.randint(1, 10)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Guess a number between 1 and 10!</h1>'


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
    app.run(debug=True)
