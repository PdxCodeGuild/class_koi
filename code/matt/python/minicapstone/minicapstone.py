'''
PDX Code Guild - Class Koi
Python Mini Capstone - Heightmap to 3D Mesh converter
Matt Walsh
'''


# import modules and set parameters
from requests import get
import shutil
from secrets import SECRET_KEY
import PySimpleGUI as sg
import numpy as np
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
import pathlib
path = pathlib.Path(__file__).parent.resolve()

def heightmap_api(center,dataset,map_size):
    """
    Gets heightmap from API and saves. Returns bool based on success/failure.
    """
    # approximately convert miles from user input to lat/long offset value
    size_scale = round(map_size / 120, 14)
    # find edges of area using center point and offset value
    north = center[0] + size_scale
    south = center[0] - size_scale
    east = center[1] + size_scale
    west = center[1] - size_scale
    # grab hidden API key
    api_key = SECRET_KEY
    # build URL for request
    url = f'https://portal.opentopography.org/API/globaldem?demtype={dataset}&south={south}&north={north}&west={west}&east={east}&outputFormat=GTiff&API_Key={api_key}'
    # request from API, save image if successful and return bool
    response = get(url, stream=True)
    if response.status_code == 200:
        with open(f'{path}/img_cache.tif','wb') as img_cache:
            shutil.copyfileobj(response.raw, img_cache)
            return True
    else:
        return False

def make_heightmap():
    """
    Future - generate heightmap
    """
    pass

def user_image():
    """
    Future - allow user to select a heightmap of their own
    """
    pass

def open_img():
    """
    Opens image and handles 16-bit pixel values.
    """
    # open image and create variables
    img = Image.open(f'{path}/img_cache.tif')
    width,height = img.size
    pixels = img.load()
    # reprocess to properly use 16-bit ints
    new_pixels = []
    for y in range(height):
        new_pixels.append([])
        for x in range(width):
            new_pixels[y].append(pixels[x,y])
    img_array = np.array(new_pixels, dtype=np.uint16)
    img = Image.fromarray(img_array)
    # save reprocessed image and regenerate/return variables
    img.save(f'{path}/img_cache.tif')
    width,height = img.size
    pixels = img.load()
    return pixels,width,height

def img_resize(pixels,width,height):
    """
    Resizes images to standard size for processing time
    """
    # process modified pixels back into an image
    resize_pixels = []
    for y in range(height):
        resize_pixels.append([])
        for x in range(width):
            resize_pixels[y].append(pixels[x,y])
    img_array = np.array(resize_pixels, dtype=np.uint16)
    # reload image and resize
    img_resize = Image.fromarray(img_array)
    img_resize = img_resize.resize((600,600))
    # regenerate/return variables from image
    width,height = img_resize.size
    pixels = img_resize.load()
    return pixels,width,height

def find_white(pixels,width,height,show_cleanup):
    """
    Scans image for anomalous white pixels and feeds them to white_correct
    when found.
    """
    # create empty list if user asked to see cleaned image
    if show_cleanup:
        clean_pixels = []
    # iterate through both axes
    for y in range(height):
        if show_cleanup:
            clean_pixels.append([])
        for x in range(width):
            # save pixel value to z variable
            z = pixels[x,y]
            # find white/error pixels and send to correction function
            if z >= 65000:
                z = white_correct(x,y,pixels,width,height)
                # change pixel value to results of cleanup
                pixels[x,y] = z
            if show_cleanup:
                clean_pixels[y].append(z)
    # recreate image and display if user requested
    if show_cleanup:
        img_array = np.array(clean_pixels, dtype=np.uint16)
        img_clean = Image.fromarray(img_array)
        img_clean.show()
    # return cleaned pixels
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
    while pixels[x,search[0]] >= 65000:
        # break if needed to avoid range error
        if search[0] == 0:
            n = True
            break
        search[0] -= 1
        distance[0] += 1
        values[0] = pixels[x,search[0]]
    while pixels[x,search[1]] >= 65000:
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
    while pixels[search[2],y] >= 65000:
        # break if needed to avoid range error
        if search[2] == 0:
            e = True
            break
        search[2] -= 1
        distance[2] += 1
        values[2] = pixels[search[2],y]
    while pixels[search[3],y] >= 65000:
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
    # create empty list to hold vertices
    vertices = []
    # iterate through all pixels
    for x in range(width):
        for y in range(height):
            # add tuple with x, y, and z coordinates to vertices list
            vertices.append((x,y,round(pixels[x,y] * depth,2)))
    # return completed list
    return vertices

def make_polys(width,height):
    """
    Generates polygons from vertices
    """
    # empty list to hold poly information
    polys = []
    # create polys referencing x/y vertices
    for x in range(width - 1):
        for y in range(height - 1):
            base = x * width + y
            a = base
            b = base + 1
            c = base + width + 1
            d = base + width
            # add poly pairs to list
            polys.append((a,b,c))
            polys.append((a,c,d))
    # return poly list
    return polys

def make_obj(vertices,polys,filename):
    """
    Writes .obj file with data taken from heightmap
    """
    # create file pased on user input
    with open(f'{path}/{filename}.obj', 'w') as obj_file:
        # add vertices in format "v x-value y-value z-value"
        for vertex in vertices:
            obj_file.write(f'v {vertex[0]} {vertex[1]} {vertex[2]}\n')
        # add polys in format "f corner-1 corner-2 corner-3"
        for poly in polys:
            obj_file.write(f'f {poly[2] + 1} {poly[1] + 1} {poly[0] + 1}\n')

def main():
    """
    Main app function
    """
    while True:
        # set app-ending variable to False
        end_app = False
        # initialize GUI and save events and values to variables
        event,values = options_window.read()
        # break and set app-ending bariable to True if user closes GUI
        if event == sg.WIN_CLOSED or event == 'Cancel':
            end_app = True
            break
        # save variables from input if user clicks "generate"
        elif event == 'Generate':
            # take coordinate string input, split, and save to variable
            center = []
            for coord in values['coord'].split(','):
                center.append(float(coord))
            map_size = values['map_size']
            dataset = values['dataset']
            do_cleanup = values['do_cleanup']
            show_cleanup = values['show_cleanup']
            # adjust depth input to approximately simulate 100% = real terrain
            depth = values['depth'] / 8000
            filename = values['filename']
            break
        # disable/enable "display cleaned heightmap" option based on "perform cleanup option"
        if values['do_cleanup'] == True:
            options_window['show_cleanup'].update(disabled=False)
        if values['do_cleanup'] == False:
            options_window['show_cleanup'].update(disabled=True)
    # close GUI
    options_window.close()
    # close app if user closed GUI above
    if end_app:
        return
    # if API request was successful, call functions
    if heightmap_api(center,dataset,map_size):
        pixels,width,height = open_img()
        if do_cleanup:
            pixels = find_white(pixels,width,height,show_cleanup)
        pixels,width,height = img_resize(pixels,width,height)
        vertices = make_verts(pixels,width,height,depth)
        polys = make_polys(width,height)
        make_obj(vertices,polys,filename)
    # if API request failed, display error
    else:
        print('An error has occurred.')

if __name__ == '__main__':
    # set up parameters for GUI
    sg.set_options(element_padding=(0,1)) 
    options_layout = [
        [sg.T('COORDINATES', font=('Any',12,'bold'))],
        [sg.T('Coordinates should be entered as "N,E" with no characters except numbers, commas, and "-" (if needed).')],
        [sg.T('Coordinates are the center point of the area.')],
        [sg.T('Enter coordinates: '),sg.In('45.52224116692548, -122.66723816400605',key='coord')],
        [sg.T('\n')],
        [sg.Column([
            [sg.T('AREA SIZE', font=('Any',12,'bold'),size=40)],
            [sg.T('Choose width/height of area in miles.')],
            [sg.T('Larger areas take longer to process.')],
            [sg.Slider(range=(1,1000),default_value=30,size=(40,15),orientation='h',key='map_size')],
        ],vertical_alignment='t'),
        sg.Column([
            [sg.T('DATASET', font=('Any',12,'bold'),size=40)],
            [sg.T('Select an elevation dataset to use.')],
            [sg.T('SRTMGL3 is recommended for processing time.')],
            [sg.T('Select Dataset: '),sg.Combo(['SRTMGL1','SRTMGL3'],size=(20),default_value='SRTMGL3',key='dataset')],
        ],vertical_alignment='t')],
        [sg.T('\n')],
        [sg.Column([
            [sg.T('ANOMALY CLEANUP',font=('Any',12,'bold'),size=40)],
            [sg.T('Allows automatic cleanup of anomalous readings.')],
            [sg.CB('Perform cleanup',True,enable_events=True,key='do_cleanup')],
            [sg.CB('Display cleaned heightmap',False,disabled=False,key='show_cleanup')],
        ],vertical_alignment='t'),
        sg.Column([
            [sg.T('SCALE HEIGHT',font=('Any',12,'bold'),size=40)],
            [sg.T('Scale height of elevation changes (% of default).')],
            [sg.Slider(range=(1,1000),default_value=400,size=(40,15),orientation='h',key='depth')],
        ],vertical_alignment='t')],
        [sg.T('\n')],
        [sg.T('FILENAME', font=('Any',12,'bold'))],
        [sg.T('Enter a filename for your mesh: '),sg.In('mesh',size=20,key='filename'),sg.T('.obj')],
        [sg.T('\n')],
        [sg.B('Generate',bind_return_key=True),sg.B('Cancel')],
    ]
    options_window = sg.Window('Mesh generation options',options_layout)
    # call main function
    main()