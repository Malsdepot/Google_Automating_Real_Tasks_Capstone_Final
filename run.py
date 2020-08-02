#!/usr/bin/env python3

import os
import requests
import json
import re

src = os.path.expanduser("~/supplier-data/descriptions/")
url = "http://localhost/fruits/"
fruits = {}

def textToJSON(source, f):
    dict1 = {}
    with open(source + f) as fh:
        name = fh.readline()
        name = name.strip()
        dict1["name"] = name

        weight = fh.readline()
        weight = weight.strip()
        weight = re.sub("[^0-9]", "", weight)
        dict1["weight"] = weight

        description = fh.readline()
        decription = description.strip()
        dict1["description"] = description

        image = str(f)
        image = image.replace("txt","jpeg")
        dict1["image_name"] = image
    return dict1

for f in os.listdir(src):
    fruits = textToJSON(src, f)
    r = requests.post(url, json=fruits)
    if 199 < r.status_code < 300:
        print("Successful post")
    else:
        print(r.raise_for_status())

