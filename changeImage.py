#!/usr/bin/env python3

import os
from PIL import Image

src = os.path.expanduser("~/supplier-data/images/")
dst = src

outFormat = "JPEG"
outSize = (600, 400)

for f in os.listdir(src):
    try:
        im=Image.open(src + f)
    except OSError:
        print("Unable to open: " + str(src + f))
        next
    
    im = im.convert("RGB")
    im = im.resize(outSize)
    newName = os.path.basename(f)
    print(newName)
    outFile = src + f
    im = im.save(outFile+".jpeg", outFormat)
    print ("Saved as : " + str(outFile))
