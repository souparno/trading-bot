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

def wazirt(symbol, callback, target, check_against):
    at = ''
    while 1 :
        try:
            response = requests.get(API_URL+"tickers/" + symbol)
            b=json.loads(response.content)
        except:
            continue

        if(at != b['at']):
            ticker = b['ticker']
            callback(target, ticker["last"], check_against)

        at = b['at']



