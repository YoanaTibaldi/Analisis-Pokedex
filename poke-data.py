import requests
import json
from bs4 import BeautifulSoup


url = "https://api.pokemon.com"
api = "https://api.pokemon.com/el/api/pokedex"

"""
Tomar las urls de la api y pasarla como parametro a la url original. Con BeautifulSoup extraigo los datos que quiero de la página
"""

def build_url(): 
    response = requests.get(api)
    data = json.loads(response.text) 

    for detail in data:
        detailURL = detail["detailPageURL"]
        urlUpdate = f'https://api.pokemon.com{detailURL}'
        url_response = requests.get(urlUpdate)
        soup = BeautifulSoup(url_response.text)
        print(soup)


build_url()