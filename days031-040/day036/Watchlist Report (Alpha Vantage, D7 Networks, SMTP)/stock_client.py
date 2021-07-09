import requests

av_apikey = "ALPHA_VANTAGE_APIKEY"
av_endpoint = "https://www.alphavantage.co/query"

av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": str,
    "apikey": av_apikey,
}


def get_stock_data(ticker_symbol):
    av_params["symbol"] = ticker_symbol
    response = requests.get(av_endpoint, av_params)
    response.raise_for_status()
    stock_data = response.json()
    print(stock_data)
    time_series_data = stock_data["Time Series (Daily)"]
    stock_data_list = [value for (key, value) in time_series_data.items()]
    dates = [key for (key,dict) in time_series_data.items()]

    # Get yesterday's closing price (the 0 index is the most recent market close, which could be today if after-hours.
    close_date = dates[0]
    yesterday_data = stock_data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    print(f"{yesterday_closing_price}")

    # Get the day before yesterday's closing price
    open_date = dates[1]
    day_before_yesterday_data = stock_data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    print(day_before_yesterday_closing_price)

    # Math
    difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
    percent_change = (abs(difference) / float(yesterday_closing_price)) * 100
    print(percent_change)
    if difference < 0:
        movement = "DOWN"
    elif difference > 0:
        movement = "UP"
    if percent_change > 4:
        get_headlines_bool = True
    else:
        get_headlines_bool = False

    return [movement, str(round(percent_change, 1)), get_headlines_bool, [open_date, close_date]]

