import os

import requests
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


def get_songs(a_date):
    url = f'https://www.billboard.com/charts/hot-100/{a_date}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [a_song.getText() for a_song in soup.find_all('span', class_='chart-element__information__song')]


def get_uris(client, song_list, a_year):
    uri_list = []
    for song in song_list:
        query = f'track:{song} year:{a_year - 1}-{a_year}'
        track = client.search(q=query, limit=1, type='track')
        try:
            uri_list.append(track['tracks']['items'][0]['uri'])
        except IndexError:
            print(f'{song} from {a_year} is not on Spotify!')
    return uri_list


def create_playlist(client, a_date, num_songs):
    playlist_name = f'{date} Billboard 100'
    description = f'Contains the top {num_songs} songs of {a_date} according to Billboard.'
    playlist = client.user_playlist_create(user_id, playlist_name, public=False, description=description)
    return playlist['id']


date = input("Which date to you want to travel to? Type the date in the format YYYY-MM-DD: ")

year = int(date[:4])
songs = get_songs(date)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("BILLBOARD_TO_SPOTIFY_ID"),
                                               client_secret=os.getenv("BILLBOARD_TO_SPOTIFY_SECRET"),
                                               redirect_uri='http://example.com',
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path='token.json'))

user_id = sp.current_user()["id"]

uris = get_uris(sp, songs, year)

playlist_id = create_playlist(sp, date, len(uris))
sp.playlist_add_items(playlist_id, uris)
