#!/usr/bin/env python3

import os
#import reports

dst = "/tmp/processed.pdf"
src = os.path.expanduser("~/supplier-data/descriptions/")
data = {}   

if __name__ == "__main__":
    title = "processed.pdf"
    dst = "/tmp/"
    for f in os.listdir(src):
        data[f]={}
        with open(src+f) as fh:
            name = fh.readline()
            name = name.strip()
            data[f]["name"] = name

            weight = fh.readline()
            weight = weight.strip()
            data[f]["weight"] = weight
    
    print(data)
    #reports.generate_report(data, dst, title)
