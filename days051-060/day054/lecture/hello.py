from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"

@app.route("/<name>")
def greet(name):
    return f"<p>Hello {name}!</p>"

@app.route("/stonks")
def stonks():
    return f'<h1>STONKS</h1>' \
           f'<br>' \
           f'<img src=https://media.tenor.com/images/a90e5f63a60f52f36b3bd4f701e3083b/tenor.gif>'


if __name__ == "__main__":
    app.run(debug=True)
