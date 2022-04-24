# Image Manipulation
# Version 3
# Mitch Chapman

from PIL import Image, ImageDraw


width = 500
height = 500

skin_color = "maroon"


img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill="white")

circle_x = width/2
circle_y = height/4
circle_radius = 40
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill=skin_color)

draw.line((250, 125, 250, 300), width=10, fill=skin_color) # neck


draw.line((250, 220, 200, 262), width=10, fill=skin_color) # arm
draw.line((250, 220, 300, 262), width=10, fill=skin_color) # arm


draw.line((250, 300, 200, 400), width=10, fill=skin_color) # leg
draw.line((250, 300, 300, 400), width=10, fill=skin_color) # leg

img.show()



















