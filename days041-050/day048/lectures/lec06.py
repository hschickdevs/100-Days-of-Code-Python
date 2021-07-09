import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
