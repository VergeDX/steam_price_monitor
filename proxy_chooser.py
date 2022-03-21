USE_PROXY: bool = True

# https://www.scrapingbee.com/blog/python-requests-proxy/
proxies = {
    'http': 'http://127.0.0.1:8889',
    'https': 'http://127.0.0.1:8889',
}


def get_proxies() -> dict:
    return proxies if USE_PROXY else {}
