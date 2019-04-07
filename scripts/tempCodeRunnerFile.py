import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import netCDF4

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.feature import NaturalEarthFeature, LAND, COASTLINE
#from cpt_convert import loadCPT
from matplotlib.colors import LinearSegmentedColormap

#Creating color palete
#cpt = loadCPT('./IR4AVHRR6.cpt')
#cpt_convert = LinearSegmentedColormap('cpt', cpt)

#ir_cmap.set_under['k']
#Band 04: longwave window (IR)
path = '/home/isabela/Documentos/Mestrado/Analises/Mestrado/GOES-13/'
file = 'goes_2017_01_31/goes13.2017.031.170018.BAND_04.nc'

#NetCDF4 library 
ds = netCDF4.Dataset(path + file, 'r')
time_var = ds.variables['time']
date = netCDF4.num2date(time_var[:], time_var.units)

#Reading with Xarray:
#ds = xr.open_dataset(file)

lons = ds.variables['lon'][:]
lats = ds.variables['lat'][:]
print(lons)
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

#Conversion of longitude and latitude arguments:
ilon_min = np.unravel_index(np.argmin(lons), lons.shape)
ilon_max = np.unravel_index(np.argmax(lons), lons.shape)
ilat_min = np.unravel_index(np.argmin(lats), lats.shape)
ilat_max = np.unravel_index(np.argmax(lats), lats.shape)

mapcrs = ccrs.Geostationary(central_longitude=-75)
LONpt0 = mapcrs.transform_point(lons[ilon_min], lats[ilon_min], ccrs.Geodetic())[0]
LONpt1 = mapcrs.transform_point(lons[ilon_max], lats[ilon_max], ccrs.Geodetic())[0]

LATpt0 = mapcrs.transform_point(lons[ilat_min], lats[ilat_min], ccrs.Geodetic())[1]
LATpt1 = mapcrs.transform_point(lons[ilat_max], lats[ilat_max], ccrs.Geodetic())[1]