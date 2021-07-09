import os
import time
from selenium import webdriver

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')
items_id = [item.get_attribute('id') for item in driver.find_elements_by_css_selector('div#store div')]


stop_time = time.time() + 300
interval = time.time() + 5

while time.time() < stop_time:
    cookie.click()
    if time.time() > interval:
        money = int(driver.find_element_by_id('money').text)

        affordables = []
        for item_id in items_id:
            item = driver.find_element_by_css_selector(f'#{item_id} b').text
            if item == '':
                continue
            price = int(item.split('-')[1].replace(',', ''))
            if price > money:
                break
            affordables.append(item_id)
        index = len(affordables) - 1
        if index == -1:
            continue
        buy = driver.find_element_by_id(items_id[index])
        buy.click()

        interval = time.time() + 5

cookies_per_second = driver.find_element_by_id('cps')
print(cookies_per_second.text)
driver.quit()
