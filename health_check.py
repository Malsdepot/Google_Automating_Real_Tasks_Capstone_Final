#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost != "127.0.0.1", "Error - localhost cannot be resolved to 127.0.0.1)"

def check_disk(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free<20, "Error - Available disk spac is less than 20%"

def check_mem():
    mu = psutil.virtual_memory().available
    total = mu/(1024 **2)
    return total < 500, "Error - Available memory is less then 500MB"

def check_cpu():
    usage = psutil.cpu_percent(1)
    return usage <80, "Error - CPU usage is over 80%"

def send_email(subject):
    email = emails.generate_email("automation@example.com", "student-02-43d8639560a1@example.com", subject, "Please check you system and resolve the issue as soon as possible")
    emails.send_email(email)

result, subject = check_localhost()
if result:
    send_email(subject)
result, subject = check_disk('/')
if result:
    send_email(subject)
result, subject = check_mem()
if result:
    send_email(subject)
result, subject = check_cpu()
if result:
    send_email(subject)
