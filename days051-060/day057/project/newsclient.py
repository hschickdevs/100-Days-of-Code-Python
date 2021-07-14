import requests


class NewsClient:
    def __init__(self, api_key):
        self.headers = {"X-Api-Key": api_key}
        self.query = {
            "country": "us",
            "category": "business",
            "q": "Wall Street"
        }
        self.articles = None

    def fetch_news(self):
        self.articles = requests.get(url="https://newsapi.org/v2/top-headlines", params=self.query, headers=self.headers).json()[
            'articles']

    def handle_article_data(self, article_num):
        article_num = int(article_num) - 1
        articles = [article for article in self.articles[:2]]
        article_source = articles[article_num]['source']['name']
        article_title = articles[article_num]['title']
        article_author = articles[article_num]['author']
        article_description = articles[article_num]['description']
        article_body = str(articles[article_num]['content'])
        article_url = articles[article_num]['url']

        return {
            "title": article_title,
            "author": article_author,
            "description": article_description,
            "body": article_body,
            "url": article_url,
            "source": article_source,
        }

# Testing:
# client = NewsClient()
# client.fetch_news()
# print(client.articles)
# print(client.handle_article_data(1))
