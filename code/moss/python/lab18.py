import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.io.shapereader as shpreader
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import cartopy.mpl.geoaxes
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np



plt.figure(figsize=(9,9))

map = plt.axes(projection=ccrs.PlateCarree())
map.set_extent([-126,-120,42,50 ], ccrs.PlateCarree())
map.add_feature(cfeature.STATES)
map.add_feature(cfeature.LAND)
map.add_feature(cfeature.OCEAN)
map.add_feature(cfeature.COASTLINE)
map.add_feature(cfeature.BORDERS, linestyle=':')
map.add_feature(cfeature.LAKES, alpha=1)
map.add_feature(cfeature.RIVERS)
map.coastlines()

hood_lon, hood_lat = -121.93, 45.45
rainier_lon, rainier_lat = - 121.72, 46.87

map.scatter(hood_lon, hood_lat , color='red', transform = ccrs.PlateCarree())
plt.text(hood_lon, hood_lat, 'Mt.Hood')


# states_provinces = cfeature.NaturalEarthFeature(category='cultural',name='admin_1_states_provinces',scale='10m',facecolor='none')
# map.add_feature(states_provinces, edgecolor='gray')

grid_lines = map.gridlines(draw_labels=True)
grid_lines.xformatter = LONGITUDE_FORMATTER
grid_lines.yformatter = LATITUDE_FORMATTER

plt.show()

# usr_input = input('\nWelcome to the Cascadia, would you line to look at map? [Y]es or [N]o.\n').upper()

# while True:

#     if usr_input == 'N':

#         print('\nGoodbye.')
#         break

#     elif usr_input == 'Y':
        
