import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import datetime
import pandas as pd
import cartopy as crs
import matplotlib as mpl
from matplotlib import rcParams

plt.rcParams['savefig.dpi'] = 150

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.feature import NaturalEarthFeature, LAND, COASTLINE

era_data = '/media/isabela/YOSHI_2/Analises/dados/ERA5/02_02.nc'
ds = xr.open_dataset(era_data)
lats = ds['latitude']
lons = ds['longitude']
#print(ds)
#LOOPING!
for t in range(0,1):
    time = ds['time'][t]
    tempo = np.datetime_as_string(time, unit='m', timezone = 'UTC')
    rh = ds['r'][t][1][:][:]
    wind_u = ds['u'][t][1][:][:]
    wind_v = ds['v'][t][1][:][:]    
    temp = ds['t'][t][1][:][:]
    hgt_500 = ds['z'][t][0][:][:]
    hgt_1000 = ds['z'][t][2][:][:]

    thk = (hgt_500-hgt_1000)/10
    #Creating the figure plot area:
    def brazil_states(projection = ccrs.PlateCarree()):
        fig, ax = plt.subplots(figsize=(9,5), subplot_kw=dict(projection=projection))
        ax.set_extent([-55,-37,-25.5,-13.5])  
        ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth = 0.5)
        ax.add_feature(cfeature.STATES, linewidth =0.5)
        ax.add_feature(cfeature.BORDERS, linewidth=0.5)
        img_plot=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.5, color='gray', linestyle='--')    
        img_plot.xlabels_top = img_plot.ylabels_right = False
        img_plot.xformatter=LONGITUDE_FORMATTER
        img_plot.yformatter=LATITUDE_FORMATTER
        return fig, ax
    projection = ccrs.PlateCarree()
    fig, ax = brazil_states()
    
    states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')
    plt.title(' {} \n Umidade Relativa (%) e Vento (ms$^-$$^1$) em 850 hPa'.format(tempo), fontsize=14)
    
    img_plot = plt.contourf(lons, lats, rh, levels= np.arange(30, 110, 10), cmap='Blues', transform=projection)
    plt.colorbar(img_plot)  
    img_plot = plt.barbs(lons[::3], lats[::3], wind_u[::3,::3], wind_v[::3,::3],transform=projection, length=5)
    
    fig.canvas.draw()
    plt.tight_layout()
    save_fig = np.array2string(tempo)
    #plt.savefig('/media/isabela/YOSHI_2/Analises/Imagens/UR_vento_0' + str(t) + '.png', transparent = True)


    plt.clf()

    fig, ax = brazil_states()
    states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')

    plt.show()