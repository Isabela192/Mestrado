import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import xarray as xr
import netCDF4

from cartopy.feature import NaturalEarthFeature, LAND, COASTLINE
#from cpt_convert import loadCPT
from matplotlib.colors import LinearSegmentedColormap

#Creating color palete
#cpt = loadCPT('./IR4AVHRR6.cpt')
#cpt_convert = LinearSegmentedColormap('cpt', cpt)

#ir_cmap.set_under['k']
#Band 04: longwave window (IR)
file = '/media/isabela/YOSHI_2/Analises/dados/Satelite/goes_2017_01_31/goes13.2017.031.164518.BAND_04.nc'

#NetCDF4 library 
ds = netCDF4.Dataset(file, 'r')
time_var = ds.variables['time']
date = netCDF4.num2date(time_var[:], time_var.units)
print(date)

#Reading with Xarray:
#ds = xr.open_dataset(file)

# The satellites sensor converts radiation falling on the sensor to a voltage which 
# is generally reported in counts(often ranging from 0-255 counts for 1-byte data or 
# 0-1023 for 10-bit data)

#Passing from 16 to 10 bits divide by 32:
IR_16bits = ds.variables['data'][0] #getting the first dimension
#print(IR_16bits.max()) # file counts
IR_10bits = IR_16bits/32
print(IR_10bits.max()) #file bytes

#Convertion from Radiance to temperature:
#Ref: https://www.ospo.noaa.gov/Operations/GOES/calibration/gvar-conversion.html#temp
#Defining constants for IR band (chanel 4):
#Inverse Plank Ctes:
c_1 = 1.191066e-5
c_2 = 1.438833
#GOES-13 ctes for channel 4:
n = 937.23
a = -0.386043
b = 1.001298

#Convert Raw counts to Radiance:
R_ir = (IR_10bits-15.6854)/5.2285
#Radiance to effective temperature
T_eff = (c_2*n)/(np.log(1+(c_1*n**3)/R_ir))

#T_eff to Temperature (K):
T_K = a+b*T_eff
T_C = T_K - 273.15
print(T_C.max())

#Figure Parameters:
def brazil_states(projection = ccrs.PlateCarree()):
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(projection=projection))
    ax.set_extent([-54,-38,-26,-14])
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth = 0.5)
    ax.add_feature(cfeature.STATES, linewidth =0.5)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)
    return fig, ax

#Map settings
fig, ax = brazil_states()
states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',name='admin_1_states_provinces_shp')
states = ax.add_feature(states, edgecolor='black')
mapcrs = ccrs.Geostationary(central_longitude=-75) #aqui vc entra com a longitude do satelite

img = ax.imshow(T_C, cmap='Greys_r', origin='upper', extent =[-100,-20,-65,15])
cbar = plt.colorbar(img, orientation='vertical', aspect=50)

plt.show()

