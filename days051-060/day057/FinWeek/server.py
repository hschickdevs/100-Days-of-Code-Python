from datetime import datetime
import requests
from flask import Flask, render_template
import random
from ratelimit import limits, sleep_and_retry

from backend.finnhub_cli import get_stock_news

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@sleep_and_retry
@limits(59, 60)
@app.route("/<symbol>")
def symbol_news(symbol: str):
    articles = get_stock_news(symbol)
    return render_template('symbol_news.html', symbol=symbol, articles=articles)


if __name__ == "__main__":
    app.run(debug=True)