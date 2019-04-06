import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import glob
import pyart
import os

#armazenando os nomes dos arquivos numa lista:

filename = os.listdir('2017-02-02')
#print(filename)
fig = plt.figure(figsize=[12, 10]) #caracteristicas da figura
d = 1

#Lendo dados de entrada

# while d <= len(filename):
#     for f in filename:
#         radar = pyart.aux_io.read_gamic('/media/isabela/YOSHI_2/dados_radar/2017-02-02/' + f)
#         sector = pyart.util.cross_section_ppi(radar, [0,45])
#         display = pyart.graph.RadarDisplay(sector)
#         display.plot('reflectivity',1)
#         #plt.tight_layout()
#         plt.savefig('Imagens_2017-02-02/cross_section_ppi_%03d.png'%d, bbox_inches='tight')

#         plt.clf()
#         d+=1
#         #plt.show()

radar = pyart.aux_io.read_gamic('/media/isabela/YOSHI_2/dados_radar/2017-02-02/RADL01046020170202235023.mvol')
sector = pyart.util.cross_section_ppi(radar, [45,90])
display = pyart.graph.RadarDisplay(sector)
display.plot('reflectivity',1)
plt.tight_layout()
plt.show()