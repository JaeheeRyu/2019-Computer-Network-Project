#https://i.k-june.com/wp/4560

import json
import urllib.request
from urllib.request import Request, urlopen

class bithumb:
    urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/all')
    readTicker = urlTicker.read()
    jsonTicker = json.loads(readTicker)
    FindBTC = jsonTicker['data']['BTC']['closing_price']
    BTC = int(FindBTC)