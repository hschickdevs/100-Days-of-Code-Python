from newsapi import NewsApiClient

# Init
news_api = NewsApiClient(api_key="9bb42f40494e4b23b6594e62eea57c28")


# /v2/top-headlines
def get_news(company_name, dates: list):
    headlines_string = ""
    all_articles = news_api.get_everything(q=company_name,
                                           language='en',
                                           sort_by='relevancy',
                                           from_param=dates[0],
                                           to=dates[1])

    for article in all_articles["articles"][:5]:
        headlines_string += f"{article['source']['name']}:\n"
        headlines_string += f"{article['title']}\n"
        headlines_string += f"{article['url']}\n\n"

    return headlines_string
