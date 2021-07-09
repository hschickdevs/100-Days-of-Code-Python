from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/harrison/Desktop/Python Career/Chrome-Webdriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")


def buy_upgrades():
    store = [upgrade for upgrade in driver.find_element_by_id("store").find_elements_by_tag_name("div")]
    store.reverse()
    for upgrade in store:
        try:
            if upgrade.get_attribute("class") == "grayed":
                pass
            else:
                upgrade.click()
        except Exception:
            pass


check_upgrades = time.time() + 5
while True:
    cookie.click()
    if time.time() > check_upgrades:
        print("Checking for available upgrades...")
        check_upgrades = time.time() + 10
        buy_upgrades()

    time.sleep(0.1)

# driver.close()
# driver.quit()
