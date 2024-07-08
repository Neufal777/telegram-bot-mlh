import requests
import json
from bs4 import BeautifulSoup

def get_games_from_coolmathgames():
    response = requests.get('https://www.coolmathgames.com/1-new-games')
    soup = BeautifulSoup(response.text, 'html.parser')

    script_tag = soup.find('script', type='application/ld+json')
    json_data = json.loads(script_tag.string)

    games = []
    for item in json_data.get('itemListElement', []):
        games.append({
            'name': item.get('name'),
            'image': item.get('image'),
            'url': item.get('url')
        })

    return games


print(get_games_from_coolmathgames())