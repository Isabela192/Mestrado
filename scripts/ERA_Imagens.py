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
era_data = '/home/isabela/MiniProjects/era_reanaysis_feb.nc'
#sg_level_data = '/home/isabela/Mestrado/MiniProjects/ERA5/single02_02.nc'
##########################################################################

ps = xr.open_dataset(era_data)
#sgl = xr.open_dataset(sg_level_data)

lats = ps['latitude']
lons = ps['longitude']
for t in range(0, len(ps['time'])):
    time = ps['time'][t]
    tempo = np.datetime_as_string(time, unit='m', timezone = 'UTC')
    rh = ps['r'][t][1][:][:]

    wind_u = ps['u'][t][1][:][:]
    wind_v = ps['v'][t][1][:][:]    
    upper_u = ps['u'][t][0][:][:]
    upper_v = ps['v'][t][0][:][:]    
    jet_stream = mpcalc.wind_speed(upper_u, upper_v)
    div = ps['d'][t][0][:][:]

    
    # prnm = sgl['msl'][t][:][:]
    # prnm = prnm/100
    geo = ps['z'][t][0][:][:]
    geo = geo/100
       
    hgt_500 = ps['z'][t][0][:][:]
    hgt_1000 = ps['z'][t][2][:][:]
    thk = (hgt_500-hgt_1000)/10
    
    #Creating the figure plot area:
    def brazil_states(projection = ccrs.PlateCarree()):
        fig, ax = plt.subplots(figsize=(7,5), subplot_kw=dict(projection=projection))
        ax.set_extent([-90,-30,-45,5])
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
    states = NaturalEarthFeature(category='cultural', scale='50m', 
                                 facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')
    skip = 10
    # Ploting jetstreams:
    plt.title(' {} \n Divergência (m$^2$s$^-$$^2$) e  Vento (ms$^-$$^1$) em 200 hPa'.format(tempo), fontsize=14)
    img_plot = plt.contourf(lons, lats, div, cmap='hot_r', transform=projection)
    cbr = plt.colorbar(img_plot)
    cbr.set_label('Divergência ($^-$$^1$)')
    img_plot = plt.quiver(lons[::skip], lats[::skip], upper_u[::skip,::skip], upper_v[::skip,::skip],
                          transform=projection, scale=500)
    img_plot = plt.quiverkey(img_plot, 1, 1.1, 1, '10 ms')

    fig.canvas.draw()
    plt.tight_layout()
    plt.savefig('/home/isabela/MiniProjects/Upper_level_0' + tempo + '.png', transparent = True)

    # #Ploting 850hPa: humidity and wind
    # projection = ccrs.PlateCarree()
    # fig, ax = brazil_states()
    
    # states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    # states = ax.add_feature(states, edgecolor='black')

    # plt.title(' {} \n Umidade Relativa (%) e Vento (ms$^-$$^1$) em 850 hPa'.format(tempo), fontsize=14)
    
    # img_plot = plt.contourf(lons, lats, rh, levels= np.arange(30, 110, 10), cmap='Blues', transform=projection)
    # cbr = plt.colorbar(img_plot)  
    # cbr.set_label('Umidade Relativa (%)')
    # img_plot = plt.barbs(lons[::10], lats[::10], wind_u[::10,::10], wind_v[::10,::10],transform=projection, length=5)
    
    # fig.canvas.draw()
    # plt.tight_layout()
    # plt.savefig('/p1-mega/isabela/ERA5/UR_vento_0' + time + '.png', transparent = True)


    # #Plotting Surface: MSLP and Geopotential Thickness
    # smooth_press = smooth2d(prnm,50, cenweight=5)
    # fig, ax = brazil_states()
    # states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    # states = ax.add_feature(states, edgecolor='black')
    
    # plt.title('{} \n PRNM (hPa) e Espessura Geopotencial'.format(tempo), fontsize=14)

    # img_plot = plt.contour(lons, lats, smooth_press, colors='blue', transform=projection, levels=np.arange(smooth_press.min(), smooth_press.max(),4))
    # plt.clabel(img_plot, fmt='%1.f', inline=True)
    
    # smooth_thk = smooth2d(thk, 50, cenweight=5)
    # img_plot = plt.contour(lons, lats, smooth_thk, levels=np.arange(thk.min(), thk.max(), 50), colors='firebrick', linestyles='dashed')
    
    # fig.canvas.draw()
    # plt.tight_layout()
    

    # plt.savefig('/p1-mega/isabela/ERA5/THK_press_0' + time + '.png', transparent = True)


    

   












