# Image Manipulation
# Version 1
# Mitch Chapman

from PIL import Image

img = Image.open("code/mitch/python/earth.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b, a = pixels[i, j]

        y = int(r * 0.299 + g * 0.587 + b * 0.114)

        pixels[i, j] = (y, y, y, a)

img.show()
























