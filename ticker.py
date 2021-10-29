import requests
import random
import json
import hashlib
import hmac
import urllib
import uuid
import time as t
import copy
import math
import sys
from datetime import datetime
import calendar
import os
from requests_toolbelt import MultipartEncoder
from time import sleep
import os.path
import threading
import pandas as pd


API_URL = 'https://api.wazirx.com/api/v2/'
FILE = "data.csv"

def wazirt():

    head=["date", "buy", "sell", "low", "high", "last", "vol"] 
    print(head,file=open(FILE,"a"))

    at = ''

    while 1 :
        x=requests.get(API_URL+"tickers/btcinr")
        a=x.content
        try:
            b=json.loads(a)
        except:
            continue

        if(at != b['at']):
            ticker = b['ticker']
            row=[str(datetime.fromtimestamp(b['at'])), ticker['buy'], ticker['sell'], ticker['low'], ticker['high'], ticker['last'], ticker['vol']]

            print(row,file=open(FILE,"a"))

        at = b['at']


y = threading.Thread(target=wazirt)
y.daemon=True
y.start()

print("before while")
while input()!="stop":
    continue
driver.close()
sys.exit()

