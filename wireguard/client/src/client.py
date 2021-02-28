#!/usr/bin/env python3
import requests
import time
import os

while(True):
    uri = os.environ.get('URI', 'http://server-demo-app:5555')
    time.sleep(3)
    try:
        response = requests.get(uri, timeout=1)
        print(response.status_code)
    except requests.RequestException as e:
        print(e)
        pass
