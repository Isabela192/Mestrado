import wradlib as wrl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import numpy as np
import glob
import os
import pyart
# For the sake of help
# https://groups.google.com/forum/#!searchin/wradlib-users/plot$20gamic%7Csort:date/wradlib-users/H8_TIP9Npw0/bs8uF43oCQAJ

scans = [0]
filenames = []


shape = "/home/isabela/Weather_Data_Science/scripts/shapefiles/sp_municipios/35MUE250GC_SIR.shp"
data, metadata = wrl.io.read_gamic_hdf5('/p1-mega/isabela/radar/SAOROQUE/2017-02-02/RADL01046020170202193023.mvol')
scandata = data['SCAN0']['Z']['data']
r = metadata['SCAN0']['r']
az = metadata['SCAN0']['az']
# Relação Z-R do Morales:
R = wrl.zr.z_to_r(scandata, a=378, b=1.34)

fig = plt.figure(figsize=[15,7])
ax = plt.subplot(projection=ccrs.PlateCarree())
ax_1 = plt.subplot(projection=ccrs.PlateCarree())
ax_1 = ax_1.add_geometries(shpreader.Reader(shape).geometries(), ccrs.PlateCarree(), 
                        edgecolor='black', facecolor='none', alpha=0.5)




