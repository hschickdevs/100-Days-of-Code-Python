import os

from selenium import webdriver

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://python.org')

search_bar = driver.find_element_by_name('q')
print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute('placeholder'))

logo = driver.find_element_by_class_name('python-logo')
print(logo.size)

doc_link = driver.find_element_by_css_selector('.documentation-widget a')
print(doc_link.text)

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

driver.quit()
