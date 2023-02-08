from os import getenv
from datetime import datetime, timedelta

from portfolio_report.util import handle_env, get_trading_days_close
from portfolio_report.process import PortfolioReport

from apscheduler.schedulers.background import BlockingScheduler

# Handle environment variables:
handle_env()

# Create portfolio report instance:
INPUT_FILEPATH = "data/portfolios_input.xlsx"
RECIPIENT_EMAILS = ["your_email@gmail.com"]
reporter = PortfolioReport(INPUT_FILEPATH, finnhub_apikey=getenv("FINNHUB_APIKEY"),
                           recipient_emails=RECIPIENT_EMAILS)

# Get all trading day close times from now to a year from now:
now = datetime.now().strftime("%Y-%m-%d")
final = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
closing_times = get_trading_days_close(_from=now, _to=final)

# Setup the task scheduler and set the report task for each closing day:
schedule = BlockingScheduler()
for time in closing_times:
    schedule.add_job(reporter.run, 'date', run_date=time.strftime('%Y-%m-%d %H:%M:%S'))

# Start the scheduler to run indefinitely
# TODO: Need to implement error logs
schedule.start()
