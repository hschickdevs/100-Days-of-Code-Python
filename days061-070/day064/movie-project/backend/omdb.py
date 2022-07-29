import os
import json
from dataclasses import dataclass
from turtle import st

import requests


ENDPOINT = "https://api.themoviedb.org/3"
IMG_ENDPOINT = "https://image.tmdb.org/t/p/w500"


@dataclass
class OMDBMovie:
    id: int
    title: str
    description: str
    release_year: str
    img_url: str
    

class OMDBClient:
    def __init__(self, api_key: str = None):
        if api_key is None:
            assert os.getenv('TMDB_API_KEY') is not None, 'TMDB_API_KEY not found in environment'
            self.api_key = os.getenv('TMDB_API_KEY')
        else:
            self.api_key = api_key
        
    def search_movies(self, query: str):
        return requests.get(ENDPOINT + "/search/movie", params={'api_key': self.api_key, 'query': query}).json()["results"]
    
    def get_movie(self, movie_id: int) -> OMDBMovie:
        r = requests.get(ENDPOINT + "/movie/" + str(movie_id), params={'api_key': self.api_key}).json()
        return OMDBMovie(id=r['id'], 
                         title=r['title'], 
                         description=r['overview'], 
                         release_year=r['release_date'].split("-")[0], 
                         img_url=IMG_ENDPOINT + r['poster_path'])