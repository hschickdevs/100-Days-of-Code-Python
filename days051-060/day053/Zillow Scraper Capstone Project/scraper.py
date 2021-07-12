from random import uniform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from time import sleep
import os
import csv
import requests

chrome_driver_path = "/Users/harrison/Desktop/Python Career/Chrome-Webdriver/chromedriver"


class ZillowScraper():
    def __init__(self, path_to_chrome_webdriver):
        self.path_to_driver = path_to_chrome_webdriver

    def scrape_properties(self, location, max_price, buy_or_rent, beds, baths):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=self.path_to_driver)  # , options=chrome_options)
        wait = WebDriverWait(driver, 10)

        results_data = []

        # Open search site
        driver.get("https://www.zillow.com/homes/")

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="srp-search-box"]/form/div[1]/input')))

        # Enter desired location into search box
        location_search = driver.find_element_by_xpath('//*[@id="srp-search-box"]/form/div[1]/input')
        for num in range(len(location_search.get_attribute('value'))):
            # .clear() not working...
            location_search.send_keys(Keys.BACKSPACE)
        sleep(0.5)
        location_search.send_keys(location)
        sleep(0.5)
        location_search.send_keys(Keys.RETURN)

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="listing-type"]'))).click()
        # driver.find_element_by_xpath('//*[@id="listing-type"]').click()
        sleep(1)
        if buy_or_rent == "Rent":
            driver.find_element_by_xpath('//*[@id="isForRent"]').click()
        else:
            driver.find_element_by_xpath(
                '//*[@id="isForSaleByAgent_isForSaleByOwner_isNewConstruction_isComingSoon_isAuction_isForSaleForeclosure_isPreMarketForeclosure_isPreMarketPreForeclosure"]').click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="price"]'))).click()
        # driver.find_element_by_xpath('//*[@id="price"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="price-form"]/fieldset/div/div[2]/label/div').click()
        sleep(1)
        max_price_entry = driver.find_element_by_xpath('//*[@id="price-exposed-max"]')
        max_price_entry.send_keys(max_price)
        sleep(1)
        max_price_entry.send_keys(Keys.RETURN)

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="beds"]'))).click()
        # driver.find_element_by_xpath('//*[@id="beds"]').click()
        sleep(1)

        bed_buttons = driver.find_element_by_name('beds-options').find_elements_by_tag_name('button')
        # bed_buttons = beds_buttons_container.find_elements_by_tag_name('button')
        for button in bed_buttons:
            if button.text == beds:
                button.click()

        sleep(1)


        baths_buttons_container = driver.find_element_by_name('baths-options')
        bath_buttons = baths_buttons_container.find_elements_by_tag_name('button')
        for button in bath_buttons:
            if button.text == baths:
                button.click()

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="search-page-react-content"]/section/div[2]/div/div[3]/div/div/div/button'))).click()
        # driver.find_element_by_xpath('//*[@id="search-page-react-content"]/section/div[2]/div/div[3]/div/div/div/button').click()
        sleep(1)

        if buy_or_rent == "Rent":
            search_results = driver.find_element_by_xpath('//*[@id="grid-search-results"]/div[1]/div/span').text
            print(search_results)
            response = f'Scraped {search_results.split(" ")[0]} rental results in {location}.'
        else:
            agent_results = driver.find_element_by_xpath(
                '//*[@id="grid-search-results"]/div[1]/div/div[1]/div/button[1]/div').text
            response = f'Found {agent_results} listings by agent in {location}.'

        # Scrape results:
        current_page = 2
        good_results = 0

        while True:
            print('Waiting for results to load...')
            sleep(5)
            index = 0
            search_results_container = driver.find_element_by_css_selector('#grid-search-results > ul')
            search_results = search_results_container.find_elements_by_tag_name('li')

            for result in search_results:
                try:
                    price = result.find_element_by_class_name('list-card-price').text
                    address = result.find_element_by_class_name('list-card-addr').text
                    url = result.find_element_by_tag_name('a').get_attribute('href')

                    results_data.append({'Price': price, "Address": address, "URL": url})

                    print(f"\nResult {good_results + 1}:")
                    print(f"{price} | {address} | {url}")
                    good_results += 1
                except Exception:
                    pass

                try:
                    driver.execute_script("arguments[0].scrollIntoView();", search_results[index + 1])
                except Exception:
                    pass
                index += 1

            try:
                sleep(2)

                next_page_button = driver.find_element_by_xpath("//a[@title='Next page']")
                tabindex = next_page_button.get_attribute('tabindex')

                print(f'Tab index Info: {tabindex} | {type(tabindex)}')

                if tabindex != "-1":
                    next_page_button.click()
                    current_page += 1
                    print(f'Found next page. Now on page {current_page}')
                else:
                    print(f'Could not find the tabindex for next page.')
                    driver.quit()
                    break

            except Exception:
                driver.quit()
                break

        self.results_to_csv(results_data, location)

        return f"Expected: {response} | Actual: {good_results}"

    def results_to_csv(self, results, location):
        csv_header = ['Price', 'Address', 'URL']
        filename = f'csv_output/{location.replace(",", "")}-Scrape-Result.csv'
        try:
            with open(filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_header)
                writer.writeheader()
                for result in results:
                    writer.writerow(result)
        except IOError:
            print("I/O error")

# For testing:
# scraper = ZillowScraper(chrome_driver_path)
# results = scraper.scrape_properties(location="Plano, TX", max_price="400000", buy_or_rent="Buy",
#                                     beds="Any", baths="Any")