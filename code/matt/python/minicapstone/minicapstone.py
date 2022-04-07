'''
PDX Code Guild - Class Koi
Python Mini Capstone - Heightmap to 3D Mesh converter
Matt Walsh
'''


#
from requests import get
from PIL import Image, ImageOps
import shutil
Image.MAX_IMAGE_PIXELS = None

def heightmap_api():
    """
    Gets heightmap from API and saves. Returns bool based on success/failure.
    """
    ################################################################################
    # hardcoded variables for fetching heightmap - will convert to user input
        
    # # OR
    # north = 46.43818760852738
    # south = 41.9485018317411
    # east = -116.8570597157284
    # west = -124.6259687261131

    # # PDX
    # north = 45.660086463160255
    # south = 45.295022112927974
    # east = -122.29957331548121
    # west = -122.98863270927748

    # # small
    # north = 45.55737739574253
    # south = 45.50861426656856
    # east = -122.62195713718967
    # west = -122.6929981799035

    center = [45.52224116692548, -122.66723816400605]
    # center = [42.94115821029393, -122.11283955448688]

    north = center[0] + .25
    south = center[0] - .25
    east = center[1] + .25
    west = center[1] - .25


    api_key = '564f38a0efbbc1397191fc77b41fbb55'
    dataset = 'SRTMGL3'
    url = f'https://portal.opentopography.org/API/globaldem?demtype={dataset}&south={south}&north={north}&west={west}&east={east}&outputFormat=GTiff&API_Key={api_key}'
    ################################################################################

    response = get(url, stream=True)
    if response.status_code == 200:
        with open('./code/matt/python/minicapstone/img_cache.tif','wb') as img_cache:
            shutil.copyfileobj(response.raw, img_cache)
            return True
    else:
        return False

def make_heightmap():
    """
    (MAYBE??) generate heightmap
    """
    pass

def user_image():
    """
    (MAYBE??) allow user to select a heightmap of their own
    """
    pass

def open_img():
    """
    Opens image, converts to grayscale, and offers to resize if too large
    """
    img = Image.open('./code/matt/python/minicapstone/img_cache.tif')
    img = ImageOps.grayscale(img)

    width, height = img.size
    pixels = img.load()
    return pixels,width,height

def find_white(pixels,width,height):
    """
    Scans image for anomalous white pixels and feeds them to white_correct
    when found.
    """
    for x in range(width):
        for y in range(height):
            z = pixels[x,y]
            # find white/error pixels
            if z >= 255:
                z = white_correct(x,y,pixels,width,height)
                pixels[x,y] = z
    return pixels

def white_correct(x,y,pixels,width,height):
    """
    Handles anomalous white pixels formed by visible or atmospheric
    reflectivity. Finds approximate intended value by sampling adjacent
    pixels on each side and adjusting pixel value based on their distance
    from the anomalous pixel.
    """
    # lists to hold n/s/e/w values
    search = [y,y,x,x] # pixel locations
    values = [0,0,0,0] # pixel values
    distance = [0,0,0,0] # distance searched to find non-white pixel
    # set bool for each direction
    n,s,e,w = False,False,False,False
    # search for non-white pixel to the north/south
    while pixels[x,search[0]] == 255:
        # break if needed to avoid range error
        if search[0] == 0:
            n = True
            break
        search[0] -= 1
        distance[0] += 1
        values[0] = pixels[x,search[0]]
    while pixels[x,search[1]] == 255:
        # break if needed to avoid range error
        if search[1] == height - 1:
            s = True
            break
        search[1] += 1
        distance[1] += 1
        values[1] = pixels[x,search[1]]
    # copy value of other pixel on axis if a range error was avoided
    if n:
        values[0] = values[1]
    if s:
        values[1] = values[0]
    # search for non-white pixel to the east/west
    while pixels[search[2],y] == 255:
        # break if needed to avoid range error
        if search[2] == 0:
            e = True
            break
        search[2] -= 1
        distance[2] += 1
        values[2] = pixels[search[2],y]
    while pixels[search[3],y] == 255:
        # break if needed to avoid range error
        if search[3] == width - 1:
            w = True
            break
        search[3] += 1
        distance[3] += 1
        values[3] = pixels[search[3],y]
    # copy value of other pixel on axis if a range error was avoided
    if e:
        values[2] = values[3]
    if w:
        values[3] = values[2]
    # calculate total distance searched in each direction
    y_distance = abs(distance[0]) + abs(distance[1])
    x_distance = abs(distance[2]) + abs(distance[3])
    # calculate difference between values of found pixels
    tot_y_change = values[0] - values[1]
    tot_x_change = values[2] - values[3]
    # calculate what portion of that value to apply based on pixel location
    this_y_change = (tot_y_change / y_distance) * abs(distance[0])
    this_x_change = (tot_x_change / x_distance) * abs(distance[2])
    # apply pixel value change to each direction
    y_val = values[0] - this_y_change
    x_val = values[2] - this_x_change
    # combine directions and return
    return int(round((y_val + x_val) / 2,0))

def make_verts(pixels,width,height,depth):
    """
    Generates vertices from heightmap data
    """
    vertices = []
    for x in range(width):
        for y in range(height):
            vertices.append((x,y,pixels[x,y] * depth))
    return vertices

def make_polys(width,height):
    """
    Generates polygons from vertices
    """
    # empty list to hold poly information
    polys = []
    #
    for x in range(width - 1):
        for y in range(height - 1):
            base = x * width + y
            a = base
            b = base + 1
            c = base + width + 1
            d = base + width

            polys.append((a,b,c))
            polys.append((a,c,d))
    return polys

def make_obj(vertices,polys,filename):
    """
    Writes .obj file with data taken from heightmap
    """
    with open(f'./code/matt/python/minicapstone/{filename}.obj', 'w') as obj_file:
        for vertex in vertices:
            obj_file.write(f'v {vertex[0]} {vertex[1]} {vertex[2]}\n')
        for poly in polys:
            obj_file.write(f'f {poly[2] + 1} {poly[1] + 1} {poly[0] + 1}\n')

################################################################################
# hardcoded - will convert to user input
depth = .1
filename = 'mesh'
################################################################################


def main():
    if heightmap_api():
        
        pixels,width,height = open_img()
        pixels = find_white(pixels,width,height)
        
        # if too big, prompt for resizing. ask for scale, recommend scale######################################
        

        vertices = make_verts(pixels,width,height,depth)
        polys = make_polys(width,height)
        make_obj(vertices,polys,filename)



        # img.show()
        #

    else:
        print('An error has occurred.')

if __name__ == '__main__':
    main()