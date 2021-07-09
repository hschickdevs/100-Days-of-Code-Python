import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://tinder.com')

time.sleep(3)
login_xpath = '//*[@id="q-84965404"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
login_button = driver.find_element_by_xpath(login_xpath)
login_button.click()

time.sleep(3)
fb_xpath = '//*[@id="q-1813346480"]/div/div/div[1]/div/div[3]/span/div[2]/button'
fb_button = driver.find_element_by_xpath(fb_xpath)
fb_button.click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
driver.find_element_by_name('email').send_keys(os.getenv('FB_EMAIL'))
driver.find_element_by_name('pass').send_keys(f"{os.getenv('FB_PASS')}{Keys.ENTER}")

time.sleep(5)

driver.switch_to.window(driver.window_handles[0])

cookies_xpath = '//*[@id="q-84965404"]/div/div[2]/div/div/div[1]/button'
driver.find_element_by_xpath(cookies_xpath).click()

time.sleep(2)
location_xpath = '//*[@id="q-1813346480"]/div/div/div/div/div[3]/button[1]'
driver.find_element_by_xpath(location_xpath).click()

time.sleep(2)
notification_xpath = '//*[@id="q-1813346480"]/div/div/div/div/div[3]/button[2]'
driver.find_element_by_xpath(notification_xpath).click()

left_xpath = '//*[@id="q-84965404"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button'

count = 0
time.sleep(15)
while count < 10:
    try:
        print('Nope')
        driver.find_element_by_css_selector('body').send_keys(Keys.LEFT)
        count += 1
        time.sleep(2)
    except NoSuchElementException:
        print('Error')
driver.quit()
