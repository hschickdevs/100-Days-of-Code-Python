import os
import time
from selenium import webdriver

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

time.sleep(5)
driver.quit()
