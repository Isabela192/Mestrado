# Plotando Temepratura, pressão e espessura:
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import datetime
import pandas as pd
import cartopy as crs
import matplotlib as mpl
import metpy.calc as mpcalc
import scipy.ndimage

from matplotlib import rcParams
from wrf import smooth2d
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.feature import NaturalEarthFeature, LAND, COASTLINE
plt.rcParams['savefig.dpi'] = 150


#########################Change HERE:#####################################
era_data = '/p1-mega/isabela/ERA5/reanalysis-era5-pressure-levels_feb.nc'
sg_level_data = '/p1-mega/isabela/ERA5/reanalysis-era5-single-levels_feb.nc'
##########################################################################

ps = xr.open_dataset(era_data)
sgl = xr.open_dataset(sg_level_data)

lats = ps['latitude']
lons = ps['longitude']

time = ps['time'][0]
tempo = np.datetime_as_string(time, unit='m', timezone = 'UTC')

def brazil(projection = ccrs.PlateCarree()):
    fig, ax = plt.subplots(figsize=(7,6), subplot_kw=dict(projection=projection))
    ax.set_extent([-75,-30,-45,5])
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth = 0.5)
    ax.add_feature(cfeature.STATES, linewidth =0.5)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)
    img_plot=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.5, color='gray', linestyle='--')    
    img_plot.xlabels_top = img_plot.ylabels_right = False
    img_plot.xformatter=LONGITUDE_FORMATTER
    img_plot.yformatter=LATITUDE_FORMATTER
    return fig, ax

projection = ccrs.PlateCarree()
fig, ax = brazil()
states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
states = ax.add_feature(states, edgecolor='black')

prnm = sgl['msl'][0][:][:]
prnm = prnm/100
smooth_press = smooth2d(prnm,10, cenweight=0.5)
t_850 = ps['t'][0][4][:][:] - 273.15

hgt_500 = ps['z'][0][0][:][:]
hgt_1000 = ps['z'][0][2][:][:]
thk = (hgt_500-hgt_1000)/10

plt.title('{} \n PRNM (hPa), Temperatura em 850 hPa  e \n Espessura de Geopotencial (m)'.format(tempo), fontsize=14)
    
img_plot = plt.contourf(lons, lats, t_850, transform=projection, cmap = 'coolwarm', levels=np.arange(-10,35,5))
plt.colorbar(img_plot)


img_plot = plt.contour(lons, lats, smooth_press, colors = 'black',
                        transform=projection, levels=np.arange(smooth_press.min(), smooth_press.max(),4))
marker = [(-64,-42),(-50,-42),(-48,-30),(-42,-30),(-42.5,-29),(-37, -42), (-35, -42)] #usar coordenadas geográficas
plt.clabel(img_plot, fmt='%1.f', inline=True, manual = marker, rightside_up= True)


img_plot = plt.contour(lons, lats, thk, levels = np.arange(thk.min(), thk.max(), 20),
                    transform = projection, linestyles = 'dashed', colors='Purple')


fig.canvas.draw()
plt.tight_layout()
plt.savefig('/home/isabela/Weather_Data_Science/ERA5/Imagens/Temp_press' + tempo + '.png')
plt.show()
