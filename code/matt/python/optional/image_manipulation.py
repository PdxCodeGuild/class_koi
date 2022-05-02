'''
PDX Code Guild - Class Koi
Optional Lab - Image Manipulation
Matt Walsh
'''

# Version 1
'''
from PIL import Image
# open from class_koi
img = Image.open("./code/matt/python/optional/image_manipulation.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        # calculate grey value
        y = int(0.299*r + 0.587*g + 0.114*b)
        # assign each pixel subvalue to grey
        pixels[i, j] = (y, y, y)
# display result
img.show()
'''


# Version 2
'''
# import libraries
from PIL import Image
import colorsys

# open from class_koi
img = Image.open("./code/matt/python/optional/image_manipulation.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        # convert values to hsv
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        # make Lena psychadelic
        h *= 4
        s *= 2
        v *= 1.5
        # convert back to rgb
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        # replace pixels with new values
        pixels[i, j] = (r, g, b)
# display result
img.show()
'''


# Version 3

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# background
draw.rectangle([0,0,width,height],(145, 6, 204))
# torso
draw.line([250,175,250,300],'Black',5)
# arms
draw.line([250,250,100,100],'Black',5)
draw.line([250,250,400,100],'Black',5)
# legs
draw.line([250,300,200,450],'Black',5)
draw.line([250,300,300,450],'Black',5)
# big ol' head
draw.ellipse([175,25,325,175],'White','Black',5)
# eyes
draw.ellipse([215,75,225,85],'Black')
draw.ellipse([275,75,285,85],'Black')
# mouth
draw.arc([215,115,285,145],0,180,'Black',5)
# display
img.show()