import builtins as _mod_builtins

class PointRectDistanceTracker(_mod_builtins.object):
    __class__ = PointRectDistanceTracker
    def __init__(self, *args, **kwargs):
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
    

class RectRectDistanceTracker(_mod_builtins.object):
    __class__ = RectRectDistanceTracker
    def __init__(self, *args, **kwargs):
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
    

class Rectangle(_mod_builtins.object):
    __class__ = Rectangle
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '\nCopyright (c) 2001, 2002 Enthought, Inc.\nAll rights reserved.\n\nCopyright (c) 2003-2012 SciPy Developers.\nAll rights reserved.\n\nRedistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are met:\n\n  a. Redistributions of source code must retain the above copyright notice,\n     this list of conditions and the following disclaimer.\n  b. Redistributions in binary form must reproduce the above copyright\n     notice, this list of conditions and the following disclaimer in the\n     documentation and/or other materials provided with the distribution.\n  c. Neither the name of Enthought nor the names of the SciPy Developers\n     may be used to endorse or promote products derived from this software\n     without specific prior written permission.\n\n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"\nAND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\nIMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\nARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR\nANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL\nDAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR\nSERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER\nCAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT\nLIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY\nOUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH\nDAMAGE.\n\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pyart/map/ckdtree.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pyart.map.ckdtree'
__package__ = 'pyart.map'
__test__ = _mod_builtins.dict()
class cKDTree(_mod_builtins.object):
    '\n    cKDTree(data, int leafsize=10)\n\n    kd-tree for quick nearest-neighbor lookup\n\n    This class provides an index into a set of k-dimensional points\n    which can be used to rapidly look up the nearest neighbors of any\n    point. \n\n    The algorithm used is described in Maneewongvatana and Mount 1999. \n    The general idea is that the kd-tree is a binary trie, each of whose\n    nodes represents an axis-aligned hyperrectangle. Each node specifies\n    an axis and splits the set of points based on whether their coordinate\n    along that axis is greater than or less than a particular value. \n\n    During construction, the axis and splitting point are chosen by the \n    "sliding midpoint" rule, which ensures that the cells do not all\n    become long and thin. \n\n    The tree can be queried for the r closest neighbors of any given point \n    (optionally returning only those within some maximum distance of the \n    point). It can also be queried, with a substantial gain in efficiency, \n    for the r approximate closest neighbors.\n\n    For large dimensions (20 is already large) do not expect this to run \n    significantly faster than brute force. High-dimensional nearest-neighbor\n    queries are a substantial open problem in computer science.\n\n    Parameters\n    ----------\n    data : array-like, shape (n,m)\n        The n data points of dimension mto be indexed. This array is \n        not copied unless this is necessary to produce a contiguous \n        array of doubles, and so modifying this data will result in \n        bogus results.\n    leafsize : positive integer\n        The number of points at which the algorithm switches over to\n        brute-force.\n\n    '
    __class__ = cKDTree
    def __init__(self, *args, **kwargs):
        '\n    cKDTree(data, int leafsize=10)\n\n    kd-tree for quick nearest-neighbor lookup\n\n    This class provides an index into a set of k-dimensional points\n    which can be used to rapidly look up the nearest neighbors of any\n    point. \n\n    The algorithm used is described in Maneewongvatana and Mount 1999. \n    The general idea is that the kd-tree is a binary trie, each of whose\n    nodes represents an axis-aligned hyperrectangle. Each node specifies\n    an axis and splits the set of points based on whether their coordinate\n    along that axis is greater than or less than a particular value. \n\n    During construction, the axis and splitting point are chosen by the \n    "sliding midpoint" rule, which ensures that the cells do not all\n    become long and thin. \n\n    The tree can be queried for the r closest neighbors of any given point \n    (optionally returning only those within some maximum distance of the \n    point). It can also be queried, with a substantial gain in efficiency, \n    for the r approximate closest neighbors.\n\n    For large dimensions (20 is already large) do not expect this to run \n    significantly faster than brute force. High-dimensional nearest-neighbor\n    queries are a substantial open problem in computer science.\n\n    Parameters\n    ----------\n    data : array-like, shape (n,m)\n        The n data points of dimension mto be indexed. This array is \n        not copied unless this is necessary to produce a contiguous \n        array of doubles, and so modifying this data will result in \n        bogus results.\n    leafsize : positive integer\n        The number of points at which the algorithm switches over to\n        brute-force.\n\n    '
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
    
    def count_neighbors(self, other, r, p):
        'count_neighbors(self, other, r, p)\n\n        Count how many nearby pairs can be formed.\n\n        Count the number of pairs (x1,x2) can be formed, with x1 drawn\n        from self and x2 drawn from `other`, and where\n        ``distance(x1, x2, p) <= r``.\n        This is the "two-point correlation" described in Gray and Moore 2000,\n        "N-body problems in statistical learning", and the code here is based\n        on their algorithm.\n\n        Parameters\n        ----------\n        other : KDTree instance\n            The other tree to draw points from.\n        r : float or one-dimensional array of floats\n            The radius to produce a count for. Multiple radii are searched with\n            a single tree traversal.\n        p : float, 1<=p<=infinity\n            Which Minkowski p-norm to use\n\n        Returns\n        -------\n        result : int or 1-D array of ints\n            The number of pairs. Note that this is internally stored in a numpy int,\n            and so may overflow if very large (2e9).\n\n        '
        pass
    
    @property
    def data(self):
        pass
    
    @property
    def leafsize(self):
        pass
    
    @property
    def m(self):
        pass
    
    @property
    def maxes(self):
        pass
    
    @property
    def mins(self):
        pass
    
    @property
    def n(self):
        pass
    
    def query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf):
        'query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf)\n        \n        Query the kd-tree for nearest neighbors\n\n        Parameters\n        ----------\n        x : array_like, last dimension self.m\n            An array of points to query.\n        k : integer\n            The number of nearest neighbors to return.\n        eps : non-negative float\n            Return approximate nearest neighbors; the kth returned value \n            is guaranteed to be no further than (1+eps) times the \n            distance to the real k-th nearest neighbor.\n        p : float, 1<=p<=infinity\n            Which Minkowski p-norm to use. \n            1 is the sum-of-absolute-values "Manhattan" distance\n            2 is the usual Euclidean distance\n            infinity is the maximum-coordinate-difference distance\n        distance_upper_bound : nonnegative float\n            Return only neighbors within this distance.  This is used to prune\n            tree searches, so if you are doing a series of nearest-neighbor\n            queries, it may help to supply the distance to the nearest neighbor\n            of the most recent point.\n\n        Returns\n        -------\n        d : array of floats\n            The distances to the nearest neighbors. \n            If x has shape tuple+(self.m,), then d has shape tuple+(k,).\n            Missing neighbors are indicated with infinite distances.\n        i : ndarray of ints\n            The locations of the neighbors in self.data.\n            If `x` has shape tuple+(self.m,), then `i` has shape tuple+(k,).\n            Missing neighbors are indicated with self.n.\n\n        '
        pass
    
    def query_ball_point(self, x, r, p, eps):
        'query_ball_point(self, x, r, p, eps)\n        \n        Find all points within distance r of point(s) x.\n\n        Parameters\n        ----------\n        x : array_like, shape tuple + (self.m,)\n            The point or points to search for neighbors of.\n        r : positive float\n            The radius of points to return.\n        p : float, optional\n            Which Minkowski p-norm to use.  Should be in the range [1, inf].\n        eps : nonnegative float, optional\n            Approximate search. Branches of the tree are not explored if their\n            nearest points are further than ``r / (1 + eps)``, and branches are\n            added in bulk if their furthest points are nearer than\n            ``r * (1 + eps)``.\n\n        Returns\n        -------\n        results : list or array of lists\n            If `x` is a single point, returns a list of the indices of the\n            neighbors of `x`. If `x` is an array of points, returns an object\n            array of shape tuple containing lists of neighbors.\n\n        Notes\n        -----\n        If you have many points whose neighbors you want to find, you may save\n        substantial amounts of time by putting them in a cKDTree and using\n        query_ball_tree.\n\n        Examples\n        --------\n        >>> from scipy import spatial\n        >>> x, y = np.mgrid[0:4, 0:4]\n        >>> points = zip(x.ravel(), y.ravel())\n        >>> tree = spatial.cKDTree(points)\n        >>> tree.query_ball_point([2, 0], 1)\n        [4, 8, 9, 12]\n\n        '
        pass
    
    def query_ball_tree(self, other, r, p, eps):
        'query_ball_tree(self, other, r, p, eps)\n\n        Find all pairs of points whose distance is at most r\n\n        Parameters\n        ----------\n        other : KDTree instance\n            The tree containing points to search against.\n        r : float\n            The maximum distance, has to be positive.\n        p : float, optional\n            Which Minkowski norm to use.  `p` has to meet the condition\n            ``1 <= p <= infinity``.\n        eps : float, optional\n            Approximate search.  Branches of the tree are not explored\n            if their nearest points are further than ``r/(1+eps)``, and\n            branches are added in bulk if their furthest points are nearer\n            than ``r * (1+eps)``.  `eps` has to be non-negative.\n\n        Returns\n        -------\n        results : list of lists\n            For each element ``self.data[i]`` of this tree, ``results[i]`` is a\n            list of the indices of its neighbors in ``other.data``.\n\n        '
        pass
    
    def query_pairs(self, r, p, eps):
        'query_pairs(self, r, p, eps)\n\n        Find all pairs of points whose distance is at most r.\n\n        Parameters\n        ----------\n        r : positive float\n            The maximum distance.\n        p : float, optional\n            Which Minkowski norm to use.  `p` has to meet the condition\n            ``1 <= p <= infinity``.\n        eps : float, optional\n            Approximate search.  Branches of the tree are not explored\n            if their nearest points are further than ``r/(1+eps)``, and\n            branches are added in bulk if their furthest points are nearer\n            than ``r * (1+eps)``.  `eps` has to be non-negative.\n\n        Returns\n        -------\n        results : set\n            Set of pairs ``(i,j)``, with ``i < j`, for which the corresponding\n            positions are close.\n\n        '
        pass
    
    def sparse_distance_matrix(self, max_distance, p):
        'sparse_distance_matrix(self, max_distance, p)\n\n        Compute a sparse distance matrix\n\n        Computes a distance matrix between two KDTrees, leaving as zero\n        any distance greater than max_distance.\n\n        Parameters\n        ----------\n        other : cKDTree\n\n        max_distance : positive float\n\n        Returns\n        -------\n        result : dok_matrix\n            Sparse matrix representing the results in "dictionary of keys" format.\n            FIXME: Internally, built as a COO matrix, it would be more\n            efficient to return this COO matrix.\n\n        '
        pass
    

## You are using the Python ARM Radar Toolkit (Py-ART), an open source
## library for working with weather radar data. Py-ART is partly
## supported by the U.S. Department of Energy as part of the Atmospheric
## Radiation Measurement (ARM) Climate Research Facility, an Office of
## Science user facility.
##
## If you use this software to prepare a publication, please cite:
##
##     JJ Helmus and SM Collis, JORS 2016, doi: 10.5334/jors.119


class coo_entries(_mod_builtins.object):
    __class__ = coo_entries
    def __init__(self, *args, **kwargs):
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
    
    def to_matrix(self):
        pass
    

class heap(_mod_builtins.object):
    __class__ = heap
    def __init__(self, *args, **kwargs):
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
    

