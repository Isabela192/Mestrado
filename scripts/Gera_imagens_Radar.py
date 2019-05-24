import  numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cartopy.crs as ccrs
import glob
import pyart
import os


######################################################################################################
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import glob
import pyart
import numpy as np
import os
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

shape = "/home/isabela/Mestrado/MiniProjects/scripts/shapefiles/sp_municipios/35MUE250GC_SIR.shp"

plt.show()

file = '/p1-mega/isabela/radar/SAOROQUE/2017-02-02/RADL01046020170202193023.mvol'
sr = pyart.aux_io.read_gamic(file)
fig = plt.figure(figsize=[10,5])
ax = plt.subplot(projection=ccrs.PlateCarree())
ax_1 = plt.subplot(projection=ccrs.PlateCarree())
ax_1 = ax_1.add_geometries(shpreader.Reader(shape).geometries(), ccrs.PlateCarree(), 
                           edgecolor='black', facecolor='none', alpha=0.5)
show = pyart.graph.RadarMapDisplay(sr)
show.plot_ppi_map("corrected_reflectivity", sweep=0, vmin=-10, vmax=70.,
                  min_lon=-49, max_lon=-46, min_lat=-24, max_lat=-22,
                  lon_lines=np.arange(-50,-45,.5), resolution='10m',
                  lat_lines=np.arange(-25,-21,.5), projection=ccrs.PlateCarree(),
                  ax=ax, fig=fig, lat_0=sr.latitude['data'][0], lon_0=sr.longitude['data'][0], alpha=0.9)

plt.show()






radar = os.listdir('/p1-mega/isabela/radar/SAOROQUE/2017-02-02/')
print(type(radar))
# #Loop trough the files:
    
for f in radar:
    sr = pyart.aux_io.read_gamic('/p1-mega/isabela/radar/SAOROQUE/2017-02-02/' + f)
    
    show = pyart.graph.RadarMapDisplay(sr)
    show.plot_ppi_map("corrected_reflectivity", sweep=0,   vmin=-10, vmax=70.,
                           projection=ccrs.PlateCarree(), ax = states)
    #show.plot_point(-47.1, -22.9, symbol='D')

    plt.tight_layout()
    
    f = f[:-5]
    
    plt.savefig('/home/isabela/Mestrado/MiniProjects/Sao_Roque/Imagens_02_02/' + f, bbox_inches='tight')

    plt.clf()