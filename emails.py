#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import os
import smtplib

def generate_email(inAttachement, inBody, inSubject, inSender, inReciever):
    m = EmailMessage()
    m['From'] = inSender
    m['To'] = inReciever
    m['Subject'] = inSubject
    m.set_content(inBody)
    mime_type, _ = mimetypes.guess_type(inAttachement)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(inAttachement, 'rb') as ap:
        m.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(inAttachement))
    return m 

def send_email(message):
    print("Sending email")
    mail_server = smtplib.SMTP('localhost')
    mail_server. send_message(message)
    mail_server.quit()
