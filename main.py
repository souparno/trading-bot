
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

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from ticker import coindcx

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://web.whatsapp.com/") 
# wait = WebDriverWait(driver, 600)

class Notify():
    def __init__(self, price, target):
        self.price = price
        self.target = target

    def texting(self, last_price):         # Whatsapp Text Code
        x_arg = "//span[contains(@title, '"+ self.target +"') and text()='" + self.target + "']"
        group_title = wait.until(EC.visibility_of_element_located((By.XPATH, x_arg)))
        group_title.click() 

        inp_xpath = "//div[contains(@title, 'Type a message')]"
        input_box = wait.until(EC.visibility_of_element_located((By.XPATH, inp_xpath)))

        # string = str(arg)
        # if float(last_price) >= self.price:
        input_box.send_keys(last_price + Keys.ENTER) 
        input_box.send_keys("you made some profit !!!" + Keys.ENTER)



notify = Notify(3980000, "Souparno Majumder")

y = threading.Thread(target=coindcx, args=["BTCINR", notify.texting])
y.daemon=True
y.start()

while input()!="stop":
    continue

driver.close()
sys.exit()
