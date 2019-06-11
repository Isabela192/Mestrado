import builtins as _mod_builtins
import logging as _mod_logging
import shapely.geometry.linestring as _mod_shapely_geometry_linestring
import shapely.geometry.point as _mod_shapely_geometry_point
import shapely.geometry.polygon as _mod_shapely_geometry_polygon
import shapely.geos as _mod_shapely_geos

LineString = _mod_shapely_geometry_linestring.LineString
LinearRing = _mod_shapely_geometry_polygon.LinearRing
Point = _mod_shapely_geometry_point.Point
__builtins__ = {}
__doc__ = None
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/shapely/speedups/_speedups.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'shapely.speedups._speedups'
__package__ = 'shapely.speedups'
__test__ = _mod_builtins.dict()
def affine_transform():
    pass

def coordseq_ctypes():
    pass

def coordseq_iter():
    pass

def destroy():
    pass

def geom_factory(g, parent):
    pass

def geos_linearring_from_py():
    pass

def geos_linestring_from_py():
    pass

has_numpy = True
lgeos = _mod_shapely_geos.LGEOS340()
log = _mod_logging.Logger()
def required():
    'Return an object that meets Shapely requirements for self-owned\n    C-continguous data, copying if necessary, or just return the original\n    object.'
    pass

