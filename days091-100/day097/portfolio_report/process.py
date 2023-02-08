from datetime import datetime, timedelta
from os import getenv

from .finnhub_client import FinnhubClient
from .data import load_portfolio
from .util import load_html_template
from .email_client import send_email

from pandas import DataFrame


class PortfolioReport:
    def __init__(self, input_path: str, finnhub_apikey: str, recipient_emails: list):
        self.path = input_path
        self.finnhub = FinnhubClient(finnhub_apikey)
        self.recipients = recipient_emails

    def build_dataframes(self) -> list[list[str, DataFrame, float, float]]:
        """
        :return: List of tuples containing:
            - sheet (portfolio) name (str)
            - Portfolio dataframe (DataFrame)
            - total portfolio value (float)
            - total portfolio PnL (float)
        """
        try:
            print("Loading input portfolio data...")
            sheets = load_portfolio(self.path)
        except Exception as exc:
            raise Exception(f"Could not load portfolio input file - {exc}")

        # Update each sheet's dataframe with the required data:
        for i, sheet in enumerate(sheets):
            sheet_name, sheet_data = sheet
            print(f"Appending data to sheet {sheet_name}...")
            symbols = list(sheet_data['Symbol'])
            quotes = [self.finnhub.get_quote(symbol) for symbol in symbols]
            entries = list(sheet_data['Entry Price'])
            shares = list(sheet_data['Shares'])
            now = datetime.now()
            yesterday = now - timedelta(days=1)

            # Append new data to dataframe
            sheet_data['PnL'] = [(quote['c'] - entry) * shares for quote, entry, shares in zip(quotes, entries, shares)]
            sheet_data['Value'] = [quote['c'] * shares for quote, entry, shares in zip(quotes, entries, shares)]
            sheet_data['Day Open'] = [quote['o'] for quote in quotes]
            sheet_data['Day Close'] = [quote['c'] for quote in quotes]
            sheet_data['Day Change (%)'] = [(quote['c'] - quote['o']) / quote['o'] for quote in quotes]
            sheet_data['Weighted Analyst Trend'] = [self.finnhub.get_weighted_analyst_trend(symbol) for symbol in symbols]
            sheet_data['1d Twitter Sentiment'] = [self.finnhub.get_twitter_sentiment(symbol, yesterday, now) for symbol in symbols]

            sheets[i].append(sum(sheet_data['Value']))
            sheets[i].append(sum(sheet_data['PnL']))

        return sheets

    def build_html(self, portfolios_data: list[list[str, DataFrame, float, float]]) -> str:
        """Expects the portfolios_data parameter to be as returned by self.build_dataframes()"""
        print("Building HTML template...")
        html = load_html_template().format(date=datetime.now().strftime("%Y-%m-%d"))
        html += "<div align='center'>\n"
        for i, portfolio_data in enumerate(portfolios_data):
            name, data, value, pnl = portfolio_data
            html += f"<h2>{name}:</h2>\n"
            html += data.to_html(index=False)
            html += f"<p><b>Total Value:</b> ${value:.2f} | <b>Total PnL:</b> ${pnl:.2f}</p>\n"
            html += "<br>\n"
        html += "</div>"
        return html

    def run(self):
        print("Process started...")

        portfolios = self.build_dataframes()

        constructed_email = self.build_html(portfolios)

        send_email(subject=f'{datetime.now().strftime("%Y-%m-%d")} Portfolio{"s" if len(portfolios) >1 else ""} Report',
                   content=constructed_email,
                   _to=self.recipients, _from=getenv("FROM_EMAIL"),
                   password=getenv("FROM_EMAIL_PASSWORD"))

        print(f"Portfolio report completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")

