import os

from internet_speed import InternetSpeedTwitterBot

PROMISED_DOWN = 400
PROMISED_UP = 100
TWITTER_USERNAME = os.getenv('TWITTER_USER')
TWITTER_PASSWORD = os.getenv('TWITTER_PASS')

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

bot = InternetSpeedTwitterBot(chromedriver_path)

bot.get_internet_speed()
bot.tweet_at_provider(PROMISED_DOWN, PROMISED_UP, TWITTER_USERNAME, TWITTER_PASSWORD)
del bot
