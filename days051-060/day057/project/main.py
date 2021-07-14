from flask import Flask, render_template
from newsclient import NewsClient
import os

app = Flask(__name__)
news_client = NewsClient(os.getenv('NEWS_API_KEY'))


@app.route('/')
def home():
    news_client.fetch_news()
    article1 = news_client.handle_article_data(1)
    article2 = news_client.handle_article_data(2)
    return render_template(
        "index.html",
        article1_title=article1['title'],
        article1_author=article1['author'],
        article2_title=article2['title'],
        article2_author=article2['author']
    )


@app.route('/<article_num>')
def full_article(article_num):
    article = news_client.handle_article_data(article_num=article_num)
    title = article['title']
    description = article['description']
    body = article['body']
    source = article['source']
    url = article['url']
    return render_template('article.html',
                           title=title,
                           description=description,
                           body=body,
                           source=source,
                           url=url
                           )


if __name__ == "__main__":
    app.run(debug=True)
