import urllib.parse
from typing import Final

from game_model import SteamGame

OneShot: SteamGame = SteamGame("OneShot", 420530, 1800)
Florence: SteamGame = SteamGame("Florence", 1102130, 1000)

# https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python
monitoring_games: Final = [OneShot, Florence]

# https://stackoverflow.com/questions/15799696/how-to-build-urls-in-python
base_url: Final = "https://store.steampowered.com/api/appdetails?"

if __name__ == '__main__':
    for game in monitoring_games:
        params = {'appids': game.appId, 'cc': 'cn', 'filters': 'price_overview'}
        print(base_url + urllib.parse.urlencode(params))
