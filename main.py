import urllib.parse

# https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python
from typing import Final

# appName_list = ["OneShot", "Florence"]
appId_list: Final = [420530, 1102130]

# https://stackoverflow.com/questions/15799696/how-to-build-urls-in-python
base_url: Final = "https://store.steampowered.com/api/appdetails?"

if __name__ == '__main__':
    for appId in appId_list:
        params = {'appids': appId, 'cc': 'cn', 'filters': 'price_overview'}
        print(base_url + urllib.parse.urlencode(params))
