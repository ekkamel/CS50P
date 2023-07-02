import sys
from PIL import Image

images = []

for arg in sys.argv[1:]: 
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

## you need to call the images in running the program as follows
## python costumes.py costume1.gif costume2.gif

## A new file names costumes.gif will be created with the animation