import requests
from bs4 import BeautifulSoup

# Use root_url/robots.txt to see what you can and cannot scrape
response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print()

article_tag = soup.find(name='a', class_='storylink')
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name='span', class_='score').getText()
print(article_text)
print(article_link)
print(article_upvote)
print()

article_tags = soup.find_all(name='a', class_='storylink')
article_texts = [article_tag.getText() for article_tag in article_tags]
article_links = [article_tag.get("href") for article_tag in article_tags]

scores = soup.find_all(name='span', class_='score')
article_upvotes = [int(score.getText().strip('points')) for score in scores]
print(article_texts)
print(article_links)
print(article_upvotes)
print()

max_index = article_upvotes.index(max(article_upvotes))

print(article_texts[max_index], article_links[max_index], article_upvotes[max_index])
