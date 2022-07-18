import os
from datetime import datetime, timedelta
from json import dumps

from dotenv import load_dotenv
import finnhub

load_dotenv()

client = finnhub.Client(os.getenv("FINNHUB_APIKEY"))

def get_stock_news(symbol: str, days_backtrack: int = 7) -> list[dict]:
    _from = datetime.now() - timedelta(days=days_backtrack)
    _to = datetime.now()
    return client.company_news(symbol.upper(), _from.strftime("%Y-%m-%d"), _to.strftime("%Y-%m-%d"))