import asyncio
import time
import aiohttp
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv

chrome_driver_path = "/Users/harrison/Desktop/Python Career/Chrome-Webdriver/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://taapi.io/indicators/")

indicators_body = driver.find_element_by_id("indicators-endpoints-data")

indicators = [{'Indicator': table_row.find_element_by_tag_name("a").text,
               'Request URL': table_row.find_element_by_tag_name("a").get_attribute("href")} for table_row in
              indicators_body.find_elements_by_tag_name("tr")]

driver.close()
driver.quit()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "X-Http-Proto": "HTTP/1.1",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Request Line": "GET / HTTP/1.1",
}


async def download_site(session, url):
    async with session.get(url) as client_response:
        return await client_response.text()


async def download_all_sites(site_headers):
    timeout = aiohttp.ClientTimeout(total=60)
    connector = aiohttp.TCPConnector(limit_per_host=50)
    async with aiohttp.ClientSession(timeout=timeout, connector=connector, headers=site_headers) as session:
        tasks = []
        for indicator in indicators:
            task = asyncio.ensure_future(download_site(session, indicator['Request URL']))
            tasks.append(task)
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

expected_urls = len(indicators)
start_time = time.time()
responses = asyncio.run(download_all_sites(headers))
duration = time.time() - start_time
print(f"Scraped {len(indicators)} indicator URLs in {duration} seconds")

for (i, response) in enumerate(responses):
    try:
        source = BeautifulSoup(response, "html.parser")
        try:
            indicator_url = source.select("div pre code")[0].text
            indicators[i]['Request URL'] = indicator_url.replace("[GET] ", "").replace("BTC", "{symbol}").replace(
                "MY_SECRET", "{api_key}").replace("interval=1h", "interval={interval}")
        except Exception:
            print(f"Could not obtain url for {indicators[i]['Indicator']}")
    except Exception as e:
        print(f"Exception Occured: {e}")


valid_urls = [indicator['Request URL'] for indicator in indicators if "{symbol}" in indicator['Request URL']]

print(f"\nFound {len(valid_urls)} valid URLs.\n")

# Check output
if expected_urls == len(valid_urls):
    print(f"{len(valid_urls)}/{expected_urls} URLS Found.")
    print("Download Success!")

    csv_columns = ['Indicator', 'Request URL']
    dict_data = indicators
    csv_file = "output.csv"

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except Exception as e:
        print(f"CSV Error: {e}")

else:
    print("URL Fetch does not match expected URLS.")
