import os
from datetime import datetime, timedelta
from json import dumps
from datetime import datetime

from dotenv import load_dotenv
import finnhub

load_dotenv()

client = finnhub.Client(os.getenv("FINNHUB_APIKEY"))


def get_stock_news(symbol: str, days_backtrack: int = 7) -> list[dict]:
    _from = datetime.now() - timedelta(days=days_backtrack)
    _to = datetime.now()
    r = client.company_news(symbol.upper(), _from.strftime("%Y-%m-%d"), _to.strftime("%Y-%m-%d"))
    for i, c_r in enumerate(r.copy()):
        r[i]['date'] = datetime.fromtimestamp(int(c_r.pop('datetime'))).strftime("%m/%d/%Y %H:%M")

    return r
