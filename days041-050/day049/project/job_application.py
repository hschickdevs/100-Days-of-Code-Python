import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=1060'
           '57199&keywords=python%20developer&location=Brazil&sortBy=R')

sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()

time.sleep(3)
driver.find_element_by_id('username').send_keys(os.getenv('LINKEDIN_EMAIL'))
driver.find_element_by_id('password').send_keys(f"{os.getenv('LINKEDIN_PASS')}{Keys.ENTER}")

time.sleep(3)
jobs = driver.find_elements_by_css_selector('.job-card-container--clickable')

for job in jobs:
    driver.execute_script("arguments[0].scrollIntoView();", job)
    job.click()
    time.sleep(3)
    try:
        driver.find_element_by_css_selector(".jobs-s-apply button").click()
        time.sleep(3)
    except NoSuchElementException:
        print("No link!")
        continue
    try:
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(os.getenv('MY_NUMBER')[3:])
    except NoSuchElementException:
        print("No phone number showing")

        driver.find_element_by_class_name("artdeco-modal__dismiss").click()
        time.sleep(2)
        driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1].click()
        time.sleep(5)
        continue

    button = driver.find_element_by_css_selector('footer button')
    if button.get_attribute("data-control-name") == 'continue_unify':
        driver.find_element_by_class_name("artdeco-modal__dismiss").click()
        time.sleep(2)
        driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1].click()
        print("To complex!")
    else:
        button.click()
        time.sleep(2)
        driver.find_element_by_class_name("artdeco-modal__dismiss").click()
        print("Applied!")

driver.quit()
