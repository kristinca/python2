# import requests
# import json
#
#
# response_API = requests.get(URL)
#
# data = response_API.text
#
# print(data)
#
#
import requests
import time
API_KEY =

class Genres:
    URL =
    genres = []

    def __init__(self, api_key):
        self.url = Genres.URL.format(api_key=api_key)
        # print(self.url)

    def fetch_genres_list(self):
        try:
            genres = requests.get(self.url).json()
        except requests.RequestException:
            self.genres = []
            return
        print(genres)
        # self.genres.extend(genres["genres"])
        # self.genres.sort()

genre = Genres(api_key=API_KEY)
genre.fetch_genres_list()

# print(genre)
# print(genre.genres)


# https://developers.themoviedb.org/3/getting-started/introduction

# https://jsonformatter.curiousc oncept.com/