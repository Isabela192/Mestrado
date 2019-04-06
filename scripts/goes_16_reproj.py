#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import gc
from osgeo import osr
from osgeo import gdal

# gc,enable()
# def remap_grid(path, var_name, lat0, lat1, lon0, lon1, resolution=2):
#     '''
#     Change the projection of GOES16 nc files from 'geos' to 'longlat'(pseudomercator)
#     All constants came form NOOA datasheet for GOES16
#  	path = str(), goes-16 ABI-l2 netCDF4 file path
#  	var_name = str(), goes-16 ABI-l2 var/channel name
#  	lat0, lat1 = float(), latitude limits (deserid area)
#  	lon0, lon1 = float(), longitude limits (deserid area)
#  	resolution = uint(), factor of resolution simplification (1~10, 10 is the lowest)
#     '''
#     # GOES-16 average kilometer per degree of latitude
#     KM_PER_DEGREE = 111.32
#     # GOES-16 Extention (satellite projection, position of corners) [llx, lly, urx, ury]
#     GOES16_EXTENT = [-5434894.885056, -5434894.885056, 5434894.885056, 5434894.885056]
    
#     # GOES-16 Spatial reference system and adjustments 
#     # h = orbital hight
#     sourcePrj = osr.SpatialReference()
#     sourcePrj.ImportFromProj4('+proj=geos +h=35786023.0 +a=6378137.0 +b=6356752.31414 +f=0.00335281068119356027 +lat_0=0.0 +lon_0=-75 +sweep=x +no_defs')
    
#     # Lat/lon WSG84 Spatial reference system(projection, elipsoid and geoid)
#     targetPrj = osr.SpatialReference()
#     targetPrj.ImportFromProj4('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs') #change here for other projections

#     if not gdal.GetDriverByName('HDF5'):
#         raise Exception('HDF5 library is not available')

#     # The netCDF4 file have must be moved from a .nc to .h5 file, otherwise gdal won't work (why?why?)
#     connectionInfo = 'HDF5:\"'+ path.split('.')[0] + 'h5' + '\"://' + var_name
#     raw = gdal.Open(connectionInfo, gdal.GA_ReadOnly)
#     raw.SetProjection(sourcePrj.ExportToWkt())
#     raw.SetGeoTransform(getGeoT(GOES16_EXTENT, raw.RasterYSize, raw.RasterXSize))

#     sizex = int(((lat1 - lat0) * KM_PER_DEGREE)/resolution)
#     sizey = int(((lon1 - lon0) * KM_PER_DEGREE)/resolution)

#     memDriver = gdal.GetDriverByName('MEM')
#     grid = memDriver.Create('grid', sizex, sizey, 1, gdal.GDT_Float32)
#     grid.SetProjection(targetPrj.ExportToWkt())
#     grid.SetGeoTransform(getGeoT(extent, grid.RasterYSize, grid.RasterXSize))

#     gdal.ReprojectImage(raw, grid, sourcePrj.ExportToWkt(), targetPrj.ExportToWkt(), gdal.GRA_NearestNeighbour) 
#     print ('End of reprojection, time:', t.time() - start, 'seconds')
#     array = grid.ReadAsArray()
#     np.ma.masked_where(array, array == -1, False)
#     grid.GetRasterBand(1).SetNoDataValue(-1)

#     grid.GetRasterBand(1).WriteArray(array)
#     out = grid.ReadAsArray()
#     del grid, raw, KM_PER_DEGREE, GOES16_EXTENT, sourcePrj, targetPrj
#     gc.collect()
#     return out
