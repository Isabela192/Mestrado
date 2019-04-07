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
caso = '_caso_02'
era_data = '/home/isabela/Documentos/Mestrado/Analises/Mestrado/ERA5/02_02.nc'
sg_level_data = '/home/isabela/Documentos/Mestrado/Analises/Mestrado/ERA5/single02_02.nc'
ps = xr.open_dataset(era_data)
sgl = xr.open_dataset(sg_level_data)
lats = ps['latitude']
lons = ps['longitude']
#print(ds)
#LOOPING!
for t in range(0,8):
    time = ps['time'][t]
    tempo = np.datetime_as_string(time, unit='m', timezone = 'UTC')
    rh = ps['r'][t][1][:][:]
    wind_u = ps['u'][t][1][:][:]
    wind_v = ps['v'][t][1][:][:]    
    
    t2m = sgl['t2m'][t][:][:]
    t2m = t2m - 273.15
    
    prnm = sgl['msl'][t][:][:]
    prnm = prnm/100
    hgt_500 = ps['z'][t][0][:][:]
    hgt_1000 = ps['z'][t][2][:][:]
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
    ## save_fig = np.array2string(tempo)
    plt.savefig('/home/isabela/Documentos/Mestrado/Analises/Mestrado/Imagens_ERA/UR_vento_0' + str(t) + caso + '.png', transparent = True)


    plt.clf()

    fig, ax = brazil_states()
    states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')
    
    plt.title('{} \n Temperatura a 2 metros (°C) e PRNM (hPa)'.format(tempo), fontsize=14)

    img_plot = plt.contourf(lons, lats, t2m, levels=np.arange(12,40,2), cmap='hot_r')
    plt.colorbar(img_plot)
    img_plot = plt.contour(lons, lats, prnm, levels=np.arange(prnm.min(), prnm.max(), 2), colors='black')
    plt.clabel(img_plot, inline = 1, fontsize=10, use_clabeltext=True)

    fig.canvas.draw()
    plt.tight_layout()

    plt.savefig('/home/isabela/Documentos/Mestrado/Analises/Mestrado/Imagens_ERA/T2m_press_0' + str(t) + caso + '.png', transparent = True)


    

   











