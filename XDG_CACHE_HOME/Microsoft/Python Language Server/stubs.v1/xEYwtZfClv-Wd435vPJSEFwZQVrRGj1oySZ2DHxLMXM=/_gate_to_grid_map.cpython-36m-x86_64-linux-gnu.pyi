import builtins as _mod_builtins

class ConstantRoI(RoIFunction):
    ' Constant radius of influence class. '
    __class__ = ConstantRoI
    def __init__(self):
        ' intialize. '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_roi(self):
        ' Return contstant radius of influence. '
        pass
    

class DistBeamRoI(RoIFunction):
    '\n    Radius of influence which expands with distance from multiple radars.\n    '
    __class__ = DistBeamRoI
    def __init__(self):
        ' initalize. '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_roi(self):
        ' Return the radius of influence for coordinates in meters. '
        pass
    

class DistRoI(RoIFunction):
    ' Radius of influence which expands with distance from the radar. '
    __class__ = DistRoI
    def __init__(self):
        ' initalize. '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_roi(self):
        ' Return the radius of influence for coordinates in meters. '
        pass
    

class GateToGridMapper(_mod_builtins.object):
    '\n    A class for efficient mapping of radar gates to a regular grid by\n    weighting all gates within a specified radius of influence by distance.\n\n    Parameters\n    ----------\n    grid_shape, : tuple of ints\n        Shape of the grid along the z, y, and x dimensions.\n    grid_starts, grid_steps  : tuple of ints\n        Starting points and step sizes in meters of the grid along the\n        z, y and x dimensions.\n    grid_sum, grid_wsum : 4D float32 array\n        Array for collecting grid weighted values and weights for each grid\n        point and field.  Dimension are order z, y, x, and fields. These array\n        are modified in place when mapping gates unto the grid.\n\n    '
    __class__ = GateToGridMapper
    def __init__(self):
        ' initialize. '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def find_roi_for_grid(self):
        '\n        Fill in the radius of influence for each point in the grid.\n\n        Parameters\n        ----------\n        roi_array : 3D float32 array\n            Array which will be filled by the radius of influence for each\n            point in the grid.\n        roi_func : RoIFunction\n            Object whose get_roi method returns the radius of influence.\n\n        '
        pass
    
    def map_gates_to_grid(self):
        '\n        Map radar gates unto the regular grid.\n\n        The grid_sum and grid_wsum arrays used to initalize the class\n        are update with the mapped gate data.\n\n        Parameters\n        ----------\n        ngates, nrays : int\n            Number of gates and rays in the radar volume.\n        gate_z, gate_y, gate_x : 2D float32 array\n            Cartesian locations of the gates in meters.\n        field_data : 3D float32 array\n            Array containing field data for the radar, dimension are ordered\n            as nrays, ngates, nfields.\n        field_mask : 3D uint8 array\n            Array containing masking of the field data for the radar,\n            dimension are ordered as nrays, ngates, nfields.\n        excluded_gates : 2D uint8 array\n            Array containing gate masking information.  Gates with non-zero\n            values will not be included in the mapping.\n        offset : tuple of floats\n            Offset of the radar from the grid origin.  Dimension are ordered\n            as z, y, x.\n            Top of atmosphere.  Gates above this level are considered.\n        roi_func : RoIFunction\n            Object whose get_roi method returns the radius of influence.\n        weighting_function : int\n            Function to use for weighting gates based upon distance.\n            0 for Barnes, 1 for Cressman weighting.\n\n        '
        pass
    

class RoIFunction(_mod_builtins.object):
    ' A class for storing radius of interest calculations. '
    __class__ = RoIFunction
    def __init__(self, *args, **kwargs):
        ' A class for storing radius of interest calculations. '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_roi(self):
        ' Return the radius of influence for coordinates in meters. '
        pass
    

__builtins__ = {}
__doc__ = '\npyart.map._gate_to_grid_map\n===========================\n\nCython classes and functions for efficient mapping of radar gates to\na uniform grid.\n\n.. autosummary::\n    :toctree: generated/\n    :template: dev_template.rst\n\n    GateToGridMapper\n    RoIFunction\n    ConstantRoI\n    DistRoI\n    DistBeamRoI\n\n'
## You are using the Python ARM Radar Toolkit (Py-ART), an open source
## library for working with weather radar data. Py-ART is partly
## supported by the U.S. Department of Energy as part of the Atmospheric
## Radiation Measurement (ARM) Climate Research Facility, an Office of
## Science user facility.
##
## If you use this software to prepare a publication, please cite:
##
##     JJ Helmus and SM Collis, JORS 2016, doi: 10.5334/jors.119


__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pyart/map/_gate_to_grid_map.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pyart.map._gate_to_grid_map'
__package__ = 'pyart.map'
def __pyx_unpickle_ConstantRoI():
    pass

def __pyx_unpickle_DistBeamRoI():
    pass

def __pyx_unpickle_DistRoI():
    pass

def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_GateToGridMapper():
    pass

def __pyx_unpickle_RoIFunction():
    pass

__test__ = _mod_builtins.dict()
