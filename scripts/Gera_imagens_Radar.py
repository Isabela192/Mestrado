import  numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import glob
import pyart
import os

fig = plt.figure(figsize=[12,9])

lonlim, latlim = [-48,-46], [-24,-22] #Campinas
#lonlim, latlim = [-48,-46], [-24.5,-22.5] #Sao Paulo

radar = pyart.aux_io.read_gamic('/media/isabela/YOSHI_2/Analises/dados/Radar/2017-02-02/RADL01046020170202121024.mvol')
#radar.info('compact')

display = pyart.graph.RadarDisplay(radar)




#List and get multiple files:


radar = os.listdir('/media/isabela/YOSHI_2/Analises/dados/Radar/2017-02-02/')
print(type(radar))
# d = 1
#Loop trough the files:
# while d <= len(radar):
    
#     for f in radar:
#         sr = pyart.aux_io.read_gamic('/media/isabela/YOSHI_2/dados_radar/2017-02-02/' + f)

#         show = pyart.graph.RadarMapDisplay(sr)
#         show.plot_ppi_map("corrected_velocity", sweep=1,   vmin=-10, vmax=70.,
#                   min_lat=latlim[0], max_lat=latlim[1], min_lon=lonlim[0], max_lon=lonlim[1],
#                   lat_lines=np.arange(latlim[0], latlim[1], .50), lon_lines=np.arange(lonlim[0], lonlim[1], .50),
#                   shapefile="shapefiles/sao_paulo")
#         show.plot_point(-47.1, -22.9, symbol='D')

#         plt.tight_layout()
#         plt.savefig('Imagens_2017-02-02/radar, bbox_inches='tight')
    
#         plt.clf()
#         d+=1






# sr_19 =
# fig = plt.figure(figsize=[12,10])
# lonlim, latlim = [-48,-46], [-24.5,-22.5]
# lonlim, latlim = [-48,-46], [-24,-22]
# show = pyart.graph.RadarMapDisplay(sr_19)

# show.plot_ppi_map("corrected_reflectivity", sweep=1,   vmin=-10, vmax=70.,
#                   min_lat=latlim[0], max_lat=latlim[1], min_lon=lonlim[0], max_lon=lonlim[1],
#                   lat_lines=np.arange(latlim[0], latlim[1], .50), lon_lines=np.arange(lonlim[0], lonlim[1], .50),
#                   shapefile="shapefiles/sao_paulo")
# show.plot_point(-46.6, -23.5, symbol='D')

# plt.show()
#plt.savefig('teste.png')

