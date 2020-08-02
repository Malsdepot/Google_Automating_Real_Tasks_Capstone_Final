#!/usr/bin/env python3

import os
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

today = datetime.date.today().strftime("%B %d, %Y")
buildlist= []
def generate_report(data, dst, title):
    report = SimpleDocTemplate(os.path.expanduser(dst + title))
    styles = getSampleStyleSheet()
    report_title = Paragraph('Processed Update on {}'.format(today), styles['h1'])
    buildlist.append(report_title)
    bodyString = ""
    blank = Paragraph('<br/>')
    for entry in data:
        pass
    report.build([report_title, blank])
    return("Report built")



