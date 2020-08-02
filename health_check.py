#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost != "127.0.0.1"

def check_disk(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free<20

def check_mem():
    mu = psutil.virtual_memory().available
    total = mu/(1024 **2)
    return total < 500

def check_cpu():
    usage = psutil.cpu_percent(1)
    return usage > 80

def send_email(subject):
    email = emails.generate_email("", "Please check your system and resolve hte issue as soon as possible", subject, "automation@example.com", "student-00-d3dc0f541a51@example.com")
    emails.send_email(email)


result = check_localhost()
if result:
    subject = "Error - localhost cannot be resolved to 127.0.0.1)"
    send_email(subject)
result = check_disk('/')
if result:
    subject = "Error - Available disk space is less than 20%"
    send_email(subject)
result = check_mem()
if result:
    subject = "Error - Available memory is less then 500MB"
    send_email(subject)
result = check_cpu()
if result:
    subject = "Error - CPU usage is over 80%"
    send_email(subject)
