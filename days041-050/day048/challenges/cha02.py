import os

from selenium import webdriver

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element_by_css_selector('div#articlecount a').text
print(article_count)

driver.quit()
