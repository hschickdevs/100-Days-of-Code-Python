from random import uniform
from selenium import webdriver
from time import sleep
import os
import csv

datafile = open('Instagram_Follower_Bot/profile_urls.csv')
profiles = [row for row in csv.DictReader(datafile)]
datafile.close()

INSTA_USERNAME = os.getenv('INSTA_USER')
INSTA_PASSWORD = os.getenv('INSTA_PASS')
print(f'Credentials: {INSTA_USERNAME} {INSTA_PASSWORD}')

chrome_driver_path = "/Users/harrison/Desktop/Python Career/Chrome-Webdriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for profile in profiles:
    url = profile['url']
    print(f'Attempting to run bot on {profile["username"]}...\n')
    try:
        driver.get(url)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    except Exception:
        print('Could not open profile page initially, must login first...\n')
    sleep(3)

    try:
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTA_USERNAME)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTA_PASSWORD)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button').click()
        sleep(3)
        print(f'Successfully Logged in as @{INSTA_USERNAME}...\n')
    except Exception:
        print(f'Do not need to log in, already logged in as {INSTA_USERNAME}.\n')

    driver.get(url)
    sleep(2)

    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    except Exception:
        pass

    sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    sleep(3)

    index = 0
    while True:
        try:
            profiles_to_follow = driver.find_elements_by_tag_name('li')
            for profile in profiles_to_follow[index:]:
                buttons = profile.find_elements_by_tag_name('button')
                for button in buttons:
                    if button.text.upper().strip() == "FOLLOW":
                        button.click()
                        sleep(round(uniform(0.25, 1.25), 2))

            driver.execute_script("arguments[0].scrollIntoView(true);", profiles_to_follow[-1])
            index = len(profiles_to_follow - 1)
            sleep(1.5)
        except Exception as e:
            print(f'Could not continue scroll.\n{e}')
            break

driver.close()
print('Bot is finished!')
