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
        detail_url = detail["detailPageURL"]
        url_update = f'https://api.pokemon.com{detail_url}'
        url_response = requests.get(url_update)
        soup = BeautifulSoup(url_response.text, 'html.parser')
        ul_element = soup.find_all("ul", class_="gauge")
        div_poke_active = soup.find("div", class_="pokemon-stats-info active")
        span_text = div_poke_active.find_all('span')

        for ul in ul_element:
            data_points = ul.find('li', attrs={'data-value': True})
            image = soup.find('img', class_='active')
            print('values: ', data_points['data-value'])                
        for span in span_text:
            print(span.get_text())
                    # for character in content:
                

build_url()

