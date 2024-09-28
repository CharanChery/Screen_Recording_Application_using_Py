import os
os.system("pip install pillow")

from PIL import Image
filename = "py.png"
img = Image.open(filename)
img.save('logo.ico')
