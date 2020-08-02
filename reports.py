#!/usr/bin/env python3

import os
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

today = datetime.date.today().strftime("%B %d, %Y")
def generate_report(data, dst, title):
    buildlist = []
    toList = []
    report = SimpleDocTemplate(os.path.expanduser(dst + title))
    styles = getSampleStyleSheet()
    #report_title = Paragraph('Processed Update on {}'.format(today), styles['h1'])
    #buildlist.append(report_title)
    bodyString = ""
    blank = Paragraph('<br/>')
   
    S = [].append    
    S(Paragraph('Processed Update on {}'.format(today), styles['h1']))
    for entry in data:
       #S(Paragraph('<br />'))
       S(Spacer(1,20))
       #S(Paragraph())
       value = data[entry]["name"]
       S(Paragraph("name {}".format(value)))
       value2 = data[entry]["weight"]
       S(Paragraph("weight: {}".format(value2)))

    report.build(S.__self__)



