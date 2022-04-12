# opentopo API key:     d9c3fc6cd49cdeb9dce77f5d519ebba1 ! HIDE THIS !
import requests
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
# import cartopy.io.shapereader as shpreader
# import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import cartopy.mpl.geoaxes
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
from ridge_map import RidgeMap # NOT WORKING #

#----- CITATIONS & REFERENCES -----#

# NCAR GEOCAT, Michaela Sizemore, https://github.com/michaelavs/cartopy_tutorial


#----- REGIONAL MAP -----#

plt.figure(figsize=(9,9))

map = plt.axes(projection=ccrs.PlateCarree())
map.set_extent([-125,-120,42,49], ccrs.PlateCarree())
grid_lines = map.gridlines(draw_labels=True)
grid_lines.xformatter = LONGITUDE_FORMATTER
grid_lines.yformatter = LATITUDE_FORMATTER

# roads = cfeature.NaturalEarthFeature(category = 'cultural', name = 'roads', scale = '10m', facecolor = 'none')
# map.add_feature(texture)
# texture = cfeature.NaturalEarthFeature(category = 'raster', name = 'GRAY_LR_SR_OB', scale = '50m', facecolor = 'none')
# map.add_feature(texture)
# states_provinces = cfeature.NaturalEarthFeature(category='cultural',name='admin_1_states_provinces',scale='10m',facecolor='none')
# map.add_feature(states_provinces, edgecolor='gray')
map.add_feature(cfeature.STATES) # state border
map.add_feature(cfeature.LAND) # land
map.add_feature(cfeature.OCEAN) # ocean
map.add_feature(cfeature.COASTLINE) #coastlines
map.add_feature(cfeature.LAKES, alpha=1)
map.add_feature(cfeature.RIVERS)

# map.add_feature(cfeature.BORDERS, linestyle=':') international border
# map.coastlines()

#----- WASHINGTON -----#

baker_lon, baker_lat = 48.776797, -121.814467
map.scatter(baker_lon, baker_lat , color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(baker_lon, baker_lat, 'Mt.Baker')

shuksn_lon, shuksn_lat = -121.602849, 48.831284
map.scatter(shuksn_lon, shuksn_lat , color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(shuksn_lon, shuksn_lat, 'Mt.Shuksan')

rainier_lon, rainier_lat = -121.760424, 46.852947 
map.scatter(rainier_lon, rainier_lat, color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(rainier_lon, rainier_lat, 'Mt.Rainier')

adams_lon, adams_lat =  -121.490746, 46.202494
map.scatter(adams_lon, adams_lat, color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(adams_lon, adams_lat, 'Mt.Adams')

stuart_lon, stuart_lat = -120.902476, 47.475198
map.scatter(stuart_lon, stuart_lat , color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(stuart_lon, stuart_lat, 'Mt.Stuart')

helens_lon, helens_lat = -122.195606, 46.191418
map.scatter(helens_lon, helens_lat , color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(helens_lon, helens_lat, 'S.Helens')

#----- OREGON -----#

hood_lon, hood_lat = -121.695966, 45.373496 
map.scatter(hood_lon, hood_lat , color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(hood_lon, hood_lat, 'Mt.Hood')

jeff_lon, jeff_lat = -121.799565, 44.6743
map.scatter(jeff_lon, jeff_lat, color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(jeff_lon, jeff_lat, 'Mt.Jefferson')

sis_lon, sis_lat = -121.769378, 44.103548, 
map.scatter(sis_lon, sis_lat, color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(sis_lon, sis_lat, 'S.Sister')

mclo_lon, mclo_lat = -122.315881, 42.444515
map.scatter( mclo_lon, mclo_lat, color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(mclo_lon, mclo_lat, 'Mt.Mcloughlin')

thiel_lon, thiel_lat  = -122.066502, 43.152769 
map.scatter(thiel_lon, thiel_lat , color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(thiel_lon, thiel_lat, 'Mt.Thielsen')

bach_lat, bach_lon  = -121.688467, 43.979347, 
map.scatter(bach_lon, bach_lat , color ='red', marker = '^', transform = ccrs.PlateCarree())
plt.text(bach_lon, bach_lat, 'Mt.Bachelor')

# plt.show()

#----- MT DATA CSV -----#

path_to_folder = './data/mt_data.csv'
with open(path_to_folder, 'r') as file:
    lines = file.read().split('\n')

rows_list = []

for line in lines:
    rows_list.append(line.split(','))

key_list = rows_list.pop(0)

mt_list = []

for row in rows_list:
    mt_list.append({key_list[0]:row[0],
                        key_list[1]:row[1],
                        key_list[2]:row[2],
                        key_list[3]:row[3]})

# print('-'*72)
# print(lines)
# print('-'*72)
# print(rows_list)
print('-'*72)
print(key_list)
print('-'*72)
print(mt_list)

#----- GMRT ELEVATION REQUEST -----#

response = requests.get(f'http://www.gmrt.org/services/PointServer?latitude={hood_lat}&longitude={hood_lon}&format=json')

print('-'*72)
print(response)
print('-'*72)
print(response.text)
print('-'*72)

#convert elevation from meter to feet#

#------ ELEVATION CHART -----#

fig = plt.figure(figsize=(10,6))
map2 = fig.add_subplot()
map2.plot(np.random.rand(10))
map2.set_ylim(0,16_000)
map2.set_ylabel('Elevation(feet)')
map2.set_xticks(ticks= [1,2,3,4])
map2.set_xticklabels(labels=['Mt.Hood', 'Mt.Jefferson', 'S.Sister', 'Mt.Rainier'])
map2.set_xlabel('Mountains')
fig.suptitle('Mountain Elevations')

inset = inset_axes(map2, width ='35%', height = '25%', loc = 'upper right', 
                   axes_class = cartopy.mpl.geoaxes.GeoAxes, 
                   axes_kwargs = dict(map_projection = ccrs.PlateCarree()))

inset.coastlines()

plt.show()

#----- 3D MODEL -----#

# RidgeMap().plot_map()


#----- USER INTERACTION -----#

# usr_input = input('\nWelcome to the Cascade Range, would you like to look at the map and elavation data? [Y]es or [N]o.\n').upper()

# while True:

#     if usr_input == 'N':

#         print('\nGoodbye.')
#         break

#     elif usr_input == 'Y':
#         plt.show()
        