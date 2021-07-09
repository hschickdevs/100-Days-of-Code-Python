import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('http://secure-retreat-92358.herokuapp.com/')

name = driver.find_element_by_name('fName')
surname = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')

name.send_keys('Paula')
surname.send_keys('Rodrigues')
email.send_keys(f'{os.getenv("EMAIL")}{Keys.ENTER}')

time.sleep(10)
driver.quit()
