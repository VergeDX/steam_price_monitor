import urllib.parse

import requests

from game_list import monitoring_games
from proxy_chooser import get_proxies

# https://stackoverflow.com/questions/15799696/how-to-build-urls-in-python
base_url: str = "https://store.steampowered.com/api/appdetails?"

if __name__ == '__main__':
    for game in monitoring_games:
        params: dict = {'appids': game.appId, 'cc': 'cn', 'filters': 'price_overview'}
        url: str = base_url + urllib.parse.urlencode(params)

        # https://docs.python-requests.org/en/latest/
        r = requests.get(url, proxies=get_proxies())
