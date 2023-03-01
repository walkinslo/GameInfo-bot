import requests
from bs4 import BeautifulSoup

from .output_table import data_to_dict
from .errors import NoGameOrInvalidInput


class GameInfo:
    def __init__(self, game):
        self.game = game

    def get_status(self):
        '''Request the website and the find everyting that contains
            the "row" tag (basically crack data).'''
        
        request = requests.get(f'https://steamcrackedgames.com/games/{self.game}')

        try:
            soup = BeautifulSoup(request.text, 'html.parser')
            
            table_raw = str(soup.find('dl', class_='row').text.replace('\n\n\n', '\n'))
            table = data_to_dict(str(table_raw))
    
            picture = soup.find('div', class_='col-md-2') # Find the game cover.
            for i in picture:
                url = str(soup.find('img', class_='img-fluid asdad lazyload d02 mb-3'))
                src = BeautifulSoup(url, 'html.parser')
    
                data_src = src.img['data-src'] # Extract the cover.
    
            return data_src, table
        
        except:
            raise NoGameOrInvalidInput(request.status_code)