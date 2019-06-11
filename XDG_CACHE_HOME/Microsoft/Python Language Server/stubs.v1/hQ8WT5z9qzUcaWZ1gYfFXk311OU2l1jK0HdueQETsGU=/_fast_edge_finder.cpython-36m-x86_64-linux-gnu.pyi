
## You are using the Python ARM Radar Toolkit (Py-ART), an open source
## library for working with weather radar data. Py-ART is partly
## supported by the U.S. Department of Energy as part of the Atmospheric
## Radiation Measurement (ARM) Climate Research Facility, an Office of
## Science user facility.
##
## If you use this software to prepare a publication, please cite:
##
##     JJ Helmus and SM Collis, JORS 2016, doi: 10.5334/jors.119

import builtins as _mod_builtins

class _EdgeCollector(_mod_builtins.object):
    '\n    Class for collecting edges, used by _edge_sum_and_count function.\n    '
    __class__ = _EdgeCollector
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
    
    def get_indices_and_velocities(self):
        ' Return the edge indices and velocities. '
        pass
    

__builtins__ = {}
__doc__ = '\npyart.correct._fast_edge_finder\n===============================\n\nCython routine for quickly finding edges between connected regions.\n\n.. autosummary::\n    :toctree: generated/\n\n    _fast_edge_finder\n\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pyart/correct/_fast_edge_finder.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pyart.correct._fast_edge_finder'
__package__ = 'pyart.correct'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _fast_edge_finder():
    '\n    Return the gate indices and velocities of all edges between regions.\n    '
    pass

