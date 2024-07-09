import requests
import json
from bs4 import BeautifulSoup


def get_games_from_coolmathgames():
    # Send a GET request to the Cool Math Games new games page
    response = requests.get('https://www.coolmathgames.com/1-new-games')
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the script tag containing the JSON data of the games
    script_tag = soup.find('script', type='application/ld+json')
    
    # Load the JSON data from the script tag
    json_data = json.loads(script_tag.string)
    
    # Initialize an empty list to store the games information
    games = []
    
    # Iterate over each item in the JSON data's itemListElement
    for item in json_data.get('itemListElement', []):
        # Append the game's name, image, and URL to the games list
        games.append({
            'name': item.get('name'),
            'image': item.get('image'),
            'url': item.get('url')
        })
    
    # Return the list of games
    return games

# Print the list of games retrieved from Cool Math Games
print(get_games_from_coolmathgames())
