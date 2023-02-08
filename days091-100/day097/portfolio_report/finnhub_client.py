from datetime import datetime
from statistics import mean, StatisticsError

from ._config import RATE_LIMIT

from ratelimit import limits, sleep_and_retry
import finnhub 


class FinnhubClient(finnhub.Client):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.api_key = api_key
        
    @sleep_and_retry
    @limits(calls=RATE_LIMIT[0], period=RATE_LIMIT[1])
    def call_api(self, func, *args):
        """Class method created to limit all API calls to the required period"""
        return func(args)
    
    def get_quote(self, symbol):
        return self.call_api(self.quote, symbol)

    def get_weighted_analyst_trend(self, symbol: str):
        """Returns the highest weighted analyst trend from finnhub"""
        r = self.call_api(self.recommendation_trends, symbol)[0]
        return max(r, key=lambda k: r[k] if type(r[k]) is int else 0)

    def get_twitter_sentiment(self, symbol, _from: datetime, _to: datetime):
        """
        Only takes twitter entries into account if the score is not 0 and there is more than 1 mention

        Range: -1 to 1 with 1 is very positive and -1 is very negative, 0 = No results
        """
        r = self.call_api(self.stock_social_sentiment, symbol, _from.strftime("%Y-%m-%d"), _to.strftime("%Y-%m-%d"))
        try:
            return mean([p['score'] for p in r['twitter'] if p['score'] != 0 and p['mention'] > 1])
        except StatisticsError:
            return 0

