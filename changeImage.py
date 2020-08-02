#!/usr/bin/env python3

import os
from PIL import Image

src = os.path.expanduser("~/supplier-data/images/")
dst = src

outFormat = "JPEG"
outSize = (600, 400)

for f in os.listdir(src):
    if "tiff" in str(f):
        try:
            im=Image.open(src + f)
        except OSError:
            print("Unable to open: " + str(src + f))
            next
    
        im = im.convert("RGB")
        im = im.resize(outSize)
        newName = os.path.basename(f)
        newName = newName.replace("tiff", "jpeg")
        print(src + newName)
        im = im.save(src + newName, outFormat)
