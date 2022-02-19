import os
import shutil
from colour import Color
import random
from html_ne import html

foldername = "custom"

try:
    shutil.rmtree(foldername)
except:
    pass
os.mkdir(foldername)
os.chdir(foldername)

bg= Color(hue=333, saturation=1, luminance=0.66)

def make_file(month, day):
    day = day.rjust(2, "0")
    month = month.rjust(2, "0")
    bg = Color(hue=random.randrange(0, 361)/360, saturation=1, luminance=0.66).hex
    
    htmlfile = html.format(day=day,month=month,bg=bg)
    
    with open(f"{day}.html", "w") as f:
        f.write(htmlfile)

for month in range(1,13):
    os.mkdir(str(month))
    os.chdir(str(month))
    
    if month == 2:
        for day in range(1,29):
            make_file(str(month),str(day))
    elif month % 2 == 0:
        for day in range(1,32):
            make_file(str(month),str(day))
    else:
        for day in range(1,31):
            make_file(str(month),str(day))
    
    os.chdir("..")
