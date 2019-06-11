import builtins as _mod_builtins

class Geodesic(_mod_builtins.object):
    '\n    Define an ellipsoid on which to solve geodesic problems.\n\n    '
    __class__ = Geodesic
    def __init__(self, *args, **kwargs):
        '\n    Define an ellipsoid on which to solve geodesic problems.\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def circle(self):
        '\n        Find a geodesic circle of given radius at a given point.\n\n        Parameters\n        ----------\n        lon\n            Longitude coordinate of the centre.\n        lat\n            Latitude coordinate of the centre.\n        radius\n            The radius of the circle (metres).\n        n_samples: optional\n            Integer number of sample points of circle.\n        endpoint: optional\n            Boolean for whether to repeat endpoint at the end of returned\n            array.\n\n        Returns\n        -------\n        An n_samples by 2 np.ndarray of evenly spaced lon-lat points on the\n        circle.\n\n        '
        pass
    
    def direct(self):
        '\n        Solve the direct geodesic problem where the length of the geodesic is\n        specified in terms of distance.\n\n        Can accept and broadcast length 1 arguments. For example, given a\n        single start point and distance, an array of different azimuths can be\n        supplied to locate multiple endpoints.\n\n        Parameters\n        ----------\n        points\n            An n (or 1) by 2 numpy.ndarray, list or tuple of lon-lat\n            points.  The starting point(s) from which to travel.\n\n        azimuths\n            A length n (or 1) numpy.ndarray or list of azimuth\n            values (degrees).\n\n        distances\n            A length n (or 1) numpy.ndarray or list of distances\n            values (metres).\n\n        Returns\n        -------\n        An n by 3 np.ndarray of lons, lats, and forward azimuths of the\n        located endpoint(s).\n\n        '
        pass
    
    def inverse(self):
        '\n        Solve the inverse geodesic problem.\n\n        Can accept and broadcast length 1 arguments. For example, given a\n        single start point, an array of different endpoints can be supplied to\n        find multiple distances.\n\n        Parameters\n        ----------\n        points\n            An n (or 1) by 2 numpy.ndarray, list or tuple of lon-lat points.\n            The starting point(s) from which to travel.\n\n        endpoints:\n            An n (or 1) by 2 numpy.ndarray, list or tuple of lon-lat points.\n            The point(s) to travel to.\n\n        Returns\n        -------\n        An n by 3 np.ndarray of distances, and the (forward) azimuths of\n        the start and end points.\n\n        '
        pass
    

__builtins__ = {}
__doc__ = '\nThis module defines the Geodesic class which can interface with the Proj.4.\ngeodesic functions.\n\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/cartopy/geodesic/_geodesic.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'cartopy.geodesic._geodesic'
__package__ = 'cartopy.geodesic'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
