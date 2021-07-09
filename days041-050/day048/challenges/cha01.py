import os

from selenium import webdriver

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://python.org')

times = driver.find_elements_by_css_selector('div.event-widget time')
names = driver.find_elements_by_css_selector('div.event-widget li a')

events = {
    index: {
        'time': time.text,
        'name': name.text
    }
    for index, (time, name) in enumerate(zip(times, names))
}

print(events)

driver.quit()

