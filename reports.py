#!/usr/bin/env python3

import os
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

today = datetime.date.today().strftime("%B %d, %Y")
print(today)
buildlist= [report_title]
def generate_report(data, dst, title):
    report = SimpleDocTemplate(os.path.expanduser(dst + title))
    styles = getSampleStyleSheet()
    report_title = Paragraph("Processed Update on {}".format(today), styles["h1"])
    blank = Paragraph("<br/>")
    for entry in data:
        name = Paragraph("Name")
        weight = Paragraph("Weight")
        buildlist.append[blank]
        buildlist.append[name]
        buildlist.append[weight]

    report.build(buildlist)




