import _sre as _mod__sre
import builtins as _mod_builtins
import collections as _mod_collections

class CRS(_mod_builtins.object):
    '\n    Define a Coordinate Reference System using proj.4.\n\n    '
    __class__ = CRS
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getstate__(self):
        'Return the full state of this instance for reconstruction\n        in ``__setstate__``.\n\n        '
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Hash the CRS based on its proj4_init string.'
        return 0
    
    def __init__(self):
        '\n        Parameters\n        ----------\n        proj4_params: iterable of key-value pairs\n            The proj4 parameters required to define the\n            desired CRS.  The parameters should not describe\n            the desired elliptic model, instead create an\n            appropriate Globe instance. The ``proj4_params``\n            parameters will override any parameters that the\n            Globe defines.\n        globe: :class:`~cartopy.crs.Globe` instance, optional\n            If omitted, the default Globe instance will be created.\n            See :class:`~cartopy.crs.Globe` for details.\n\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        '\n        Implement the __reduce__ API so that unpickling produces a stateless\n        instance of this class (e.g. an empty tuple). The state will then be\n        added via __getstate__ and __setstate__.\n\n        '
        return ''; return ()
    
    def __setstate__(self, state):
        "\n        Take the dictionary created by ``__getstate__`` and passes it\n        through to the class's __init__ method.\n\n        "
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _as_mpl_transform(self):
        '\n        Cast this CRS instance into a :class:`matplotlib.axes.Axes` using\n        the Matplotlib ``_as_mpl_transform`` interface.\n\n        '
        pass
    
    def as_geocentric(self):
        '\n        Return a new Geocentric CRS with the same ellipse/datum as this\n        CRS.\n\n        '
        pass
    
    def as_geodetic(self):
        '\n        Return a new Geodetic CRS with the same ellipse/datum as this\n        CRS.\n\n        '
        pass
    
    def is_geodetic(self):
        pass
    
    @property
    def proj4_init(self):
        pass
    
    @property
    def proj4_params(self):
        pass
    
    def transform_point(self):
        '\n        transform_point(x, y, src_crs)\n\n        Transform the given float64 coordinate pair, in the given source\n        coordinate system (``src_crs``), to this coordinate system.\n\n        Parameters\n        ----------\n        x\n            the x coordinate, in ``src_crs`` coordinates, to transform\n        y\n            the y coordinate, in ``src_crs`` coordinates, to transform\n        src_crs\n            instance of :class:`CRS` that represents the coordinate\n            system of ``x`` and ``y``.\n        trap\n            Whether proj.4 errors for "latitude or longitude exceeded\n            limits" and "tolerance condition error" should be trapped.\n\n        Returns\n        -------\n        (x, y) in this coordinate system\n\n        '
        pass
    
    def transform_points(self):
        '\n        transform_points(src_crs, x, y[, z])\n\n        Transform the given coordinates, in the given source\n        coordinate system (``src_crs``), to this coordinate system.\n\n        Parameters\n        ----------\n        src_crs\n            instance of :class:`CRS` that represents the\n            coordinate system of ``x``, ``y`` and ``z``.\n        x\n            the x coordinates (array), in ``src_crs`` coordinates,\n            to transform.  May be 1 or 2 dimensional.\n        y\n            the y coordinates (array), in ``src_crs`` coordinates,\n            to transform.  Its shape must match that of x.\n        z: optional\n            the z coordinates (array), in ``src_crs`` coordinates, to\n            transform.  Defaults to None.\n            If supplied, its shape must match that of x.\n\n        Returns\n        -------\n            Array of shape ``x.shape + (3, )`` in this coordinate system.\n\n        '
        pass
    
    def transform_vectors(self):
        "\n        transform_vectors(src_proj, x, y, u, v)\n\n        Transform the given vector components, with coordinates in the\n        given source coordinate system (``src_proj``), to this coordinate\n        system. The vector components must be given relative to the\n        source projection's coordinate reference system (grid eastward and\n        grid northward).\n\n        Parameters\n        ----------\n        src_proj\n            The :class:`CRS.Projection` that represents the coordinate system\n            the vectors are defined in.\n        x\n            The x coordinates of the vectors in the source projection.\n        y\n            The y coordinates of the vectors in the source projection.\n        u\n            The grid-eastward components of the vectors.\n        v\n            The grid-northward components of the vectors.\n\n        Note\n        ----\n            x, y, u and v may be 1 or 2 dimensional, but must all have matching\n            shapes.\n\n        Returns\n        -------\n            ut, vt: The transformed vector components.\n\n        Note\n        ----\n           The algorithm used to transform vectors is an approximation\n           rather than an exact transform, but the accuracy should be\n           good enough for visualization purposes.\n\n        "
        pass
    

class Geocentric(CRS):
    '\n    Define a Geocentric coordinate system, where x, y, z are Cartesian\n    coordinates from the center of the Earth.\n\n    '
    __class__ = Geocentric
    __dict__ = {}
    def __init__(self, globe):
        '\n        Parameters\n        ----------\n        globe: A :class:`cartopy.crs.Globe`, optional\n            Defaults to a "WGS84" datum.\n\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Geodetic(CRS):
    '\n    Define a latitude/longitude coordinate system with spherical topology,\n    geographical distance and coordinates are measured in degrees.\n\n    '
    __class__ = Geodetic
    __dict__ = {}
    def __init__(self, globe):
        '\n        Parameters\n        ----------\n        globe: A :class:`cartopy.crs.Globe`, optional\n            Defaults to a "WGS84" datum.\n\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Globe(_mod_builtins.object):
    '\n    Define an ellipsoid and, optionally, how to relate it to the real world.\n\n    '
    __class__ = Globe
    __dict__ = {}
    def __init__(self, datum, ellipse, semimajor_axis, semiminor_axis, flattening, inverse_flattening, towgs84, nadgrids):
        '\n        Parameters\n        ----------\n        datum\n            Proj4 "datum" definiton. Defaults to None.\n        ellipse\n            Proj4 "ellps" definiton. Defaults to \'WGS84\'.\n        semimajor_axis\n            Semimajor axis of the spheroid / ellipsoid.  Defaults to None.\n        semiminor_axis\n            Semiminor axis of the ellipsoid.  Defaults to None.\n        flattening\n            Flattening of the ellipsoid.  Defaults to None.\n        inverse_flattening\n            Inverse flattening of the ellipsoid.  Defaults to None.\n        towgs84\n            Passed through to the Proj4 definition.  Defaults to None.\n        nadgrids\n            Passed through to the Proj4 definition.  Defaults to None.\n\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'cartopy._crs'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def to_proj4_params(self):
        '\n        Create an OrderedDict of key value pairs which represents this globe\n        in terms of proj4 params.\n\n        '
        pass
    

OrderedDict = _mod_collections.OrderedDict
PROJ4_RELEASE = 'Rel. 5.0.1, April 1st, 2018'
PROJ4_VERSION = _mod_builtins.tuple()
class Proj4Error(_mod_builtins.Exception):
    '\n    Raised when there has been an exception calling proj.4.\n\n    Add a ``status`` attribute to the exception which has the\n    proj.4 error reference.\n\n    '
    __class__ = Proj4Error
    __dict__ = {}
    def __init__(self):
        '\n    Raised when there has been an exception calling proj.4.\n\n    Add a ``status`` attribute to the exception which has the\n    proj.4 error reference.\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'cartopy._crs'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__builtins__ = {}
__doc__ = '\nThis module defines the core CRS class which can interface with Proj.4.\nThe CRS class is the base-class for all projections defined in :mod:`cartopy.crs`.\n\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/cartopy/_crs.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'cartopy._crs'
__package__ = 'cartopy'
__test__ = _mod_builtins.dict()
_match = _mod__sre.SRE_Match()
