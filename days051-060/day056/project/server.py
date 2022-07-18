from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("personal.html")

@app.route("/quote/<base>-<quote>")
def quote(base: str, quote: str()):
    return requests.get(f"https://api.binance.com/api/v3/avgPrice?symbol={base.upper()}{quote.upper()}").json()



if __name__ == "__main__":
    app.run(debug=True)