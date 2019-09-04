import pyart
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import glob
import numpy as np
import os, errno
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import netCDF4
from datetime import datetime


plt.rcParams.update({'figure.max_open_warning': 0})
plt.rcParams.update({'font.size':15})
campinas_lat = -22.9
campinas_lon = -47.06
sp_lat = -23.55
sp_lon = -46.65
date = "2017-02-22"
shape = "/home/isabela/Weather_Data_Science/scripts/shapefiles/sp_municipios/35MUE250GC_SIR.shp"
radar = os.listdir('/p1-mega/isabela/radar/SAOROQUE/' + date)

for f in radar:
    fig = plt.figure(figsize=[15,7])
    ax = plt.subplot(projection=ccrs.PlateCarree())
    ax_1 = plt.subplot(projection=ccrs.PlateCarree())
    ax_1 = ax_1.add_geometries(shpreader.Reader(shape).geometries(), ccrs.PlateCarree(), 
                            edgecolor='black', facecolor='none', alpha=0.5)

    sr = pyart.aux_io.read_gamic('/p1-mega/isabela/radar/SAOROQUE/' + date +'/' + f)
    tempo=netCDF4.num2date(sr.time['data'][0], sr.time['units'])
    tempo=tempo.strftime("%Y-%m-%d %H:%M")
    show = pyart.graph.RadarMapDisplay(sr)
    show.plot_ppi_map("corrected_reflectivity", sweep=0, vmin=-10, vmax=70.,
                        min_lon=-50, max_lon=-45, min_lat=-25, max_lat=-21,
                        lon_lines=np.arange(-50,-44,.5), resolution='10m', 
                        title = '{} \n Refletividade Equivalente - elevação 0.5°'.format(tempo),
                        colorbar_label='dBZ',
                        lat_lines=np.arange(-25,-20,.5), projection=ccrs.PlateCarree(), cmap="pyart_RefDiff",
                        ax=ax, fig=fig, lat_0=sr.latitude['data'][0], lon_0=sr.longitude['data'][0], alpha=0.9)
    show.plot_point(lon=sp_lon, lat=sp_lat,symbol='d',color='indigo')
    fig.canvas.draw()
    plt.tight_layout()
    nome = f[:-5]
    try:
        os.makedirs('/home/isabela/Mestrado/MiniProjects/Sao_Roque/Imagens_' + date)
        print('Saving')
        plt.savefig('/home/isabela/Mestrado/MiniProjects/Sao_Roque/Imagens_' + date + '/' + nome, bbox_inches='tight')
    except FileExistsError:
        print('Directory Exists - Saving')
        plt.savefig('/home/isabela/Mestrado/MiniProjects/Sao_Roque/Imagens_' + date + '/' + nome, bbox_inches='tight')
    plt.clf()