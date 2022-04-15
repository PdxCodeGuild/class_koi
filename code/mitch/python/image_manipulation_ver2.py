# Image Manipulation
# Version 2
# Mitch Chapman

from PIL import Image
import colorsys

img = Image.open("code/mitch/python/earth.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b, a = pixels[i, j]

        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        h *= 0.9
        s *= 1.5
        v *= 0.8
        
        
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)  
        
        pixels[i, j] = (r, g, b, a)

img.show()
























