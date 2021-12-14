import requests
import pandas as pd

API_URL = "https://api.coindcx.com/"

response = requests.get(API_URL + "exchange/ticker")

def coindcx(symbol, callback):
    _timestamp = ''

    while 1 :
        try:
            df = pd.DataFrame(response.json())
            df = df.where(df["market"]==symbol).dropna()

        except:
            continue

        timestamp = df["timestamp"][0]

        if(_timestamp != timestamp):
            _timestamp = timestamp
            callback(df['last_price'][0])



