from datetime import datetime
import requests
from flask import Flask, render_template
import random

from backend import get_stock_news

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<symbol>")
def symbol(symbol: str):
    articles = get_stock_news(symbol)
    return render_template('symbol_news.html', symbol=symbol, articles=articles)


if __name__ == "__main__":
    app.run(debug=True)