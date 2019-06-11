import builtins as _mod_builtins
import shapely.geos as _mod_shapely_geos

__builtins__ = {}
__doc__ = '\nThis module pulls together _trace.cpp, proj.4, GEOS and _crs.pyx to implement a function\nto project a LinearRing/LineString. In general, this should never be called manually,\ninstead leaving the processing to be done by the :class:`cartopy.crs.Projection`\nsubclasses.\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/cartopy/trace.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'cartopy.trace'
__package__ = 'cartopy'
__test__ = _mod_builtins.dict()
lgeos = _mod_shapely_geos.LGEOS340()
def project_linear():
    '\n    Return the MultiLineString which results from projecting the given\n    geometry from the source projection into the destination projection.\n\n    Parameters\n    ----------\n    line_string\n        A shapely LineString or LinearRing to be projected.\n    src_crs\n        The cartopy.crs.CRS defining the coordinate system of the line\n        to be projected.\n    dest_projection\n        The cartopy.crs.Projection defining the projection for the\n        resulting projected line.\n\n    '
    pass

