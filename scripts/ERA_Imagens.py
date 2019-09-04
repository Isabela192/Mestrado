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
era_data = '/p1-mega/isabela/ERA5/reanalysis-era5-pressure-levels_jan.nc'
sg_level_data = '/p1-mega/isabela/ERA5/reanalysis-era5-single-levels_jan.nc'
##########################################################################

ps = xr.open_dataset(era_data)
sgl = xr.open_dataset(sg_level_data)

lats = ps['latitude']
lons = ps['longitude']
for t in range(0, len(ps['time'])):
    time = ps['time'][t]
    tempo = np.datetime_as_string(time, unit='m', timezone = 'UTC')
         
    
    #Creating the  plot area:
    def sudeste_states(projection = ccrs.PlateCarree()):
        fig, ax = plt.subplots(figsize=(7,5), subplot_kw=dict(projection=projection))
        ax.set_extent([-60,-30,-35,-10])
        ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth = 0.5)
        ax.add_feature(cfeature.STATES, linewidth =0.5)
        ax.add_feature(cfeature.BORDERS, linewidth=0.5)
        img_plot=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.5, color='gray', linestyle='--')    
        img_plot.xlabels_top = img_plot.ylabels_right = False
        img_plot.xformatter=LONGITUDE_FORMATTER
        img_plot.yformatter=LATITUDE_FORMATTER
        return fig, ax
    projection = ccrs.PlateCarree()
    fig, ax = sudeste_states()
    states = NaturalEarthFeature(category='cultural', scale='50m', 
                                 facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')
    
    # #Ploting Divergence
    # div = ps['d'][t][0][:][:] * 10**4
    # skip = 5
    # plt.title('{} \n Divergência (s$^-$$^1$) 10$^-$$^5$ e  Vento (ms$^-$$^1$) em 200 hPa'.format(tempo), fontsize=14)
    # img_plot = plt.contourf(lons, lats, div, levels = np.arange(-2,3,0.5), cmap='PuBuGn_r', transform=projection)
    # cbr = plt.colorbar(img_plot)
    # img_plot = plt.quiver(lons[::skip], lats[::skip], upper_u[::skip,::skip], upper_v[::skip,::skip],
    #                       angles='xy', transform=projection, scale=300)
    # img_plot = plt.quiverkey(img_plot, 1.13, 1.03, 30, '30 m/s')

    # fig.canvas.draw()
    # plt.tight_layout()
    # plt.savefig('/home/isabela/Weather_Data_Science/ERA5/Imagens/Upper_level_0' + tempo + '.png')
    # plt.clf()

    # #Ploting 850hPa: humidity and wind
    wind_u = ps['u'][t][4][:][:]
    wind_v = ps['v'][t][4][:][:]
    rh_850 = ps['r'][t][1][:][:]
    
    projection = ccrs.PlateCarree()
    fig, ax = sudeste_states()
    
    states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')

    plt.title(' {} \n Umidade Relativa (%) e Vento (ms$^-$$^1$) em 850 hPa'.format(tempo), fontsize=14)
    
    img_plot = plt.contourf(lons, lats, rh_850, levels= np.arange(30, 120, 10), cmap='Blues', transform=projection)
    skip = 5
    cbr = plt.colorbar(img_plot, ticks = [40,50,60,70,80,90,100])  
    img_plot = plt.quiver(lons[::skip], lats[::skip], wind_u[::skip,::skip], wind_v[::skip,::skip],transform=projection, scale=200)
    img_plot = plt.quiverkey(img_plot, 1.13, 1.03, 20, '20 ms')

    fig.canvas.draw()
    plt.tight_layout()
    plt.savefig('/home/isabela/Weather_Data_Science/ERA5/Imagens/UR_vento_zoom_0' + tempo + '.png')
    plt.clf()
    
    # Mean RH 
    rh_700 = ps['r'][t][3][:][:]
    rh_500 = ps['r'][t][2][:][:]
    
    mean_rh = (rh_500+rh_700)/2

    fig, ax = sudeste_states()
    states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')
    
    plt.title('{} \n Umidade Relativa Média entre 700-500 hPa'.format(tempo), fontsize=14)
    #print(vert_w)
    img_plot = plt.contourf(lons, lats, mean_rh, levels=np.arange(30,110,10), cmap='Blues', transform=projection)
    plt.colorbar(img_plot, ticks = [30,40,50,60,70,80,90,100])
    # img_plot = plt.contour(lons, lats, vert_w, transform=projection, colors='black')
    # img_plot = plt.clabel(img_plot,inline=True)
    fig.canvas.draw()
    plt.tight_layout()

    plt.savefig('/home/isabela/Weather_Data_Science/ERA5/Imagens/UR_Media' + tempo + '.png')
    plt.clf()


    # Plotting Surface: MSLP and 850 hPa Temperature

    
    
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

    
    fig, ax = brazil()
    states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')
    

    # #Ploting 850hPa: humidity and wind
    wind_u = ps['u'][t][4][:][:]
    wind_v = ps['v'][t][4][:][:]
    rh_850 = ps['r'][t][1][:][:]
    
    projection = ccrs.PlateCarree()
    fig, ax = brazil()
    
    states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')

    plt.title(' {} \n Umidade Relativa (%) e Vento (ms$^-$$^1$) em 850 hPa'.format(tempo), fontsize=14)
    
    img_plot = plt.contourf(lons, lats, rh_850, levels= np.arange(30, 120, 10), cmap='Blues', transform=projection)
    skip = 5
    cbr = plt.colorbar(img_plot, ticks = [40,50,60,70,80,90,100])  
    img_plot = plt.quiver(lons[::skip], lats[::skip], wind_u[::skip,::skip], wind_v[::skip,::skip],transform=projection, scale=200)
    img_plot = plt.quiverkey(img_plot, 1.13, 1.03, 20, '20 ms')

    fig.canvas.draw()
    plt.tight_layout()
    plt.savefig('/home/isabela/Weather_Data_Science/ERA5/Imagens/UR_vento_0' + tempo + '.png')
    plt.clf()
    
    # Ploting jetstreams:
    upper_u = ps['u'][t][0][:][:]
    upper_v = ps['v'][t][0][:][:]    
    jet_stream = mpcalc.wind_speed(upper_u, upper_v)
    
    projection = ccrs.PlateCarree()
    fig, ax = brazil()
    
    states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp', linewidth = 0.4)
    states = ax.add_feature(states, edgecolor='black')

    skip = 10
    plt.title('{} \n Vento (ms$^-$$^1$) em 200 hPa'.format(tempo), fontsize=14)
    img_plot = plt.contourf(lons, lats, jet_stream, levels = np.arange(20,90,10),cmap='hot_r', transform=projection)
    cbr = plt.colorbar(img_plot)
    img_plot = plt.quiver(lons[::skip], lats[::skip], upper_u[::skip,::skip], upper_v[::skip,::skip], transform = projection, scale=500)
    img_plot = plt.quiverkey(img_plot, 1.13, 1.03, 50, '50 ms')

    fig.canvas.draw()
    plt.tight_layout()
    plt.savefig('/home/isabela/Weather_Data_Science/ERA5/Imagens/Upper_level_jet_0' + tempo + '.png')
    plt.clf()    
    
    


    

   












