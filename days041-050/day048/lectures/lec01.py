import os
import time
from selenium import webdriver

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://amazon.com')

time.sleep(5)

driver.close()  # single tab
driver.quit()  # whole browser
