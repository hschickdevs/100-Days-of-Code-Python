import os
from datetime import datetime

from ._config import REQUIRED_ENVARS

from dotenv import find_dotenv, load_dotenv
import pandas_market_calendars as pmcal


def load_html_template():
    path = os.path.join(os.path.dirname(__file__), "assets", "email_template.html")
    with open(path, 'r') as infile:
        return infile.read()


def handle_env(envpath: str = None):
    """Checks if the .env file exists in the current working dir, and imports the variables if so"""
    try:
        if envpath is None:
            envpath = find_dotenv(raise_error_if_not_found=True, usecwd=True)
        load_dotenv(dotenv_path=envpath)
    except:
        pass
    finally:
        for var in REQUIRED_ENVARS:
            if os.getenv(var) is None:
                raise ValueError(f"Missing environment variable: {var}")


def get_trading_days_close(_from: str, _to: str) -> list[datetime]:
    """
    Fetch the trading day closing schedule for the New York Stock Exchange

    :param _from: The start date to fetch the trading day closing schedule (YYYY-MM-DD)
    :param _to: The end date to fetch the trading day closing schedule (YYYY-MM-DD)
    """
    # print(pmcal.get_calendar_names())
    return pmcal.get_calendar("NYSE").schedule(start_date=_from, end_date=_to)['market_close']
