import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self, chromedriver_path):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        go_button = self.driver.find_element_by_class_name('start-text')
        go_button.click()

        xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/'
        down_xpath = f'{xpath}div[2]/div/div[2]/span'
        up_xpath = f'{xpath}div[3]/div/div[2]/span'

        while self.down == 0 and self.up == 0:
            try:
                self.down = float(self.driver.find_element_by_xpath(down_xpath).text)
                self.up = float(self.driver.find_element_by_xpath(up_xpath).text)
            except ValueError:
                self.down = 0
                self.up = 0
            time.sleep(5)

    def tweet_at_provider(self, promised_download, promised_upload, username, password):
        self.driver.get('https://twitter.com/login')
        time.sleep(5)
        self.driver.find_element_by_name('session[username_or_email]').send_keys(username)
        self.driver.find_element_by_name('session[password]').send_keys(f'{password}{Keys.ENTER}')
        time.sleep(5)
        tweet_bad = f'Hey @valenetoficial why is my internet speed {self.down} DOWNLOAD/{self.up}' \
                    f' UPLOAD when I pay for {promised_download} DOWNLOAD/ {promised_upload}UPLOAD?'
        tweet_good = f'Hey @valenetoficial thanks! My internet speed {self.down} DOWNLOAD/{self.up}' \
                     f' UPLOAD when I pay for {promised_download} DOWNLOAD/ {promised_upload} UPLOAD'
        xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/' \
                'div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'

        tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div' \
                      '[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]'
        tweet_input = self.driver.find_element_by_xpath(xpath)
        if self.down < promised_download or self.up < promised_upload:
            tweet_input.send_keys(tweet_bad)
        else:
            tweet_input.send_keys(tweet_good)

        self.driver.find_element_by_xpath(tweet_xpath).click()

    def __del__(self):
        self.driver.quit()
