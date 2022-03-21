import urllib.parse

import grequests

from game_list import monitoring_games

# https://stackoverflow.com/questions/15799696/how-to-build-urls-in-python

base_url: str = "https://store.steampowered.com/api/appdetails?"

if __name__ == '__main__':
    # https://stackoverflow.com/questions/9110593/asynchronous-requests-with-python-requests
    async_list = []

    for game in monitoring_games:
        params: dict = {'appids': game.appId, 'cc': 'cn', 'filters': 'price_overview'}
        url: str = base_url + urllib.parse.urlencode(params)

        # https://github.com/spyoungtech/grequests
        action_item = grequests.get(url)
        async_list.append(action_item)

    grequests.map(async_list)
