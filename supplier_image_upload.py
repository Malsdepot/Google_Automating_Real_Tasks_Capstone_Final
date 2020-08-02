#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
src = os.path.expanduser("~/supplier-data/images/")

for item in os.listdir(src):
    if "jpeg" in item:
        with open(src + str(item), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            if 199 < r.status_code < 300:
                print("Successful upload")
            else:
                print("r.raise_for_status()")
