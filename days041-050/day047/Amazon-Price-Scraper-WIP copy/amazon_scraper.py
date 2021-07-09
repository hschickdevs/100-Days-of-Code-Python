import requests
from bs4 import BeautifulSoup
import lxml

header = {
    "Request Line": "GET / HTTP/1.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
    "X-Http-Proto": "HTTP/1.1"
}


def get_price(url):
    try:
        response = requests.get(url, headers=header)
        good_url = True

    except Exception:
        print(f"Invalid URL: {url}")
        good_url = False

    if good_url:
        try:
            source = BeautifulSoup(response.text, 'lxml')
            # print(source.find("span", class_="a-size-medium a-color-price").text)
            price = source.find("span", id="price_inside_buybox")
            if price is not None:
                price_text = price.text
            else:
                price = source.find("span", id="priceblock_ourprice")
                if price is not None:
                    price_text = price.text
                else:
                    price_text = "Price Scrape Bocked"

            price = price_text.replace('$', "")
            price = price.replace(',', "")

            try:
                price = float(price)
            except Exception:
                pass

            availability_div = source.find("div", id="availability")

            availability = availability_div.find("span", class_="a-size-medium a-color-success")
            if availability is not None:
                availability_data = availability.text.strip()
            else:
                availability = availability_div.find("span", class_="a-size-medium a-color-price")
                if availability is not None:
                    availability_data = availability.text.strip()
                else:
                    availability_data = "No Stock Data"

            try:
                availability_data = int(availability_data.split(" ")[1])
            except Exception:
                pass

            return [price, availability_data]

        except Exception as e:
            return [e, e]
    else:
        return["BAD URL", "BAD URL"]
