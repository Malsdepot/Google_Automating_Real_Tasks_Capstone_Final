#!/usr/bin/env python3

import os
import reports
import emails

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
    
    reports.generate_report(data, dst, title)
    sender = "automation@example.com"
    reciever="student-02-43d8639560a1@example.com"
    subject = "Upload Complete - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    msg = emails.generate_email(dst+title, body, subject, sender, reciever)
    emails.send_email(msg)
