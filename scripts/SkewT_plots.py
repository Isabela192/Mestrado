import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import datetime 


import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import add_metpy_logo, SkewT, Hodograph
from metpy.units import units
from siphon.simplewebservice.wyoming import WyomingUpperAir
from matplotlib import rcParams

#Pegando os dados do Wyoming com o Siphon:

date = datetime.datetime(2017, 1, 31, 12)
station = 'SBMT' #código do Campo de Marte
sounding = WyomingUpperAir.request_data(date, station)
#Aumentando a qualidade da iamgem
plt.rcParams['savefig.dpi'] = 255

p = sounding['pressure'].values * units.hPa
T = sounding['temperature'].values * units.degC
Td = sounding['dewpoint'].values * units.degC
u = sounding['u_wind'].values * units.knot
v = sounding['v_wind'].values * units.knot
#print(mpcalc.cape_cin(p, T, Td, prof))
print(mpcalc.most_unstable_cape_cin(p, T, Td))
print(mpcalc.surface_based_cape_cin(p, T, Td))


mask_100 = p>= 100 * units.hPa #máscara para plotar o vento até 100hPa
fig = plt.figure(figsize=(7, 9))
gs = gridspec.GridSpec(3, 3)
skew = SkewT(fig, rotation=45)

skew = SkewT(fig, rotation=45)

#SkewT Básico:
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
plt.xlabel('Temperatura (°C)', fontsize = 12)
plt.ylabel('Pressão (hPa)', fontsize = 12)

skew.ax.set_ylim(1000, 100)
skew.ax.set_xlim(-30, 50)
skew.plot_barbs(p[mask_100][::2], u[mask_100][::2], v[mask_100][::2], flip_barb = False) # Faz com que as barbelas fiquem no sentido certo (HS)

#Adicionando Emoção:
lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0]) #Cálculo do LCL
skew.plot(lcl_pressure, lcl_temperature, 'ko', markerfacecolor='black')
prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC') #cáclculo da trajetória da parcela depois do lcl
skew.plot(p, prof, 'k', linewidth=2)

skew.ax.axvline(0, color='c', linestyle='--', linewidth=2)
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()

date = date.strftime('%Y-%m-%d %H:%M')

plt.suptitle('Sondagem ' + date, fontsize = 16, y=0.91)
plt.savefig('/home/isabela/Mestrado/MiniProjects/Sondagens/sondagem_' + date + '.png' , format = 'png')
plt.show()
# ################################################ HODOGRAPH ###########################################
# #Get wind data for the first 10 km (~100 hPa)
# p_10km, u_10km, v_10km = mpcalc.get_layer(p, u, v, depth=10 * units.km)
# ax = fig.add_subplot(gs[0, -1])
# h = Hodograph(ax, component_range=60.)
# h.add_grid(increment=10)
# h.add_grid(increment=20, color = 'k', linestyle = '-')
# h.plot(u_10km, v_10km)
# ax.set_xlabel('Nós', fontsize = 12)
# ax.set_ylabel('Nós', fontsize = 12)
# print(np.round(cape, decimals = 3))
# print(np.round(cin, decimals = 3))
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.text(-96, -150, 'CAPE = 783.326 J/kg', fontsize=25)
# plt.text(-96, -180, 'CINE = -24.417 J/kg', fontsize=25)

# plt.suptitle('Sondagem do Dia 02/02/2017 - 12Z (SBMT)', fontsize = 16, y=0.91)
# plt.savefig('sondagem_02022017.png', format = 'png')