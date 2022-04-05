'''
PDX Code Guild - Class Koi
Python Mini Capstone - Heightmap to 3D Mesh converter
Matt Walsh
'''


#



from requests import get
from PIL import Image
import shutil
Image.MAX_IMAGE_PIXELS = None

north = 46.43818760852738
south = 41.9485018317411
east = -116.8570597157284
west = -124.6259687261131
api_key = '564f38a0efbbc1397191fc77b41fbb55'
dataset = 'SRTMGL3'
url = f'https://portal.opentopography.org/API/globaldem?demtype={dataset}&south={south}&north={north}&west={west}&east={east}&outputFormat=GTiff&API_Key={api_key}'

response = get(url, stream=True)
if response.status_code == 200:
    with open('./code/matt/python/minicapstone/temp.tif','wb') as temp_img:
        shutil.copyfileobj(response.raw, temp_img)
    img = Image.open('./code/matt/python/minicapstone/temp.tif')
    width, height = img.size
    pixels = img.load()
    for x in range(width):
        for y in range(height):
            # find white/error pixels
            if pixels[x,y] == 255:
                print(f'{x},{y}')
    # img.show()
else:
    print('An error has occurred.')

