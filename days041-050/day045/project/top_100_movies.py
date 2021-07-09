import requests

from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')
titles = [f'{title.getText()}\n' for title in soup.find_all('h3', class_='title')]

with open('top_100_movies.txt', 'w') as file:
    file.writelines(reversed(titles))
