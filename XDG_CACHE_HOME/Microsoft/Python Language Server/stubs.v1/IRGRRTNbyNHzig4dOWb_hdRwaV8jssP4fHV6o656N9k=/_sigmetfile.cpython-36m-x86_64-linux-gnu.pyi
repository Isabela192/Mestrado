import builtins as _mod_builtins

BIN1 = 'B'
BIN2 = 'H'
BIN4 = 'I'
COLOR_SCALE_DEF = _mod_builtins.tuple()
DSP_DATA_MASK = _mod_builtins.tuple()
FLT4 = 'f'
FLT8 = 'd'
INGEST_CONFIGURATION = _mod_builtins.tuple()
INGEST_DATA_HEADER = _mod_builtins.tuple()
INGEST_HEADER = _mod_builtins.tuple()
MESSAGE = 'I'
PRODUCT_CONFIGURATION = _mod_builtins.tuple()
PRODUCT_END = _mod_builtins.tuple()
PRODUCT_HDR = _mod_builtins.tuple()
RAW_PROD_BHDR = _mod_builtins.tuple()
RECORD_SIZE = 6144
SIGMET_DATA_TYPES = _mod_builtins.dict()
SINT1 = 'b'
SINT2 = 'h'
SINT4 = 'i'
STRUCTURE_HEADER = _mod_builtins.tuple()
class SigmetFile(_mod_builtins.object):
    '\n    A class for accessing data from Sigmet (IRIS) product files.\n\n    Parameters\n    ----------\n    filename : str\n        Filename or file-like object.\n\n    Attributes\n    ----------\n    debug : bool\n        Set True to print out debugging information, False otherwise.\n    product_hdr : dict\n        Product_hdr structure.\n    ingest_header : dict\n        Ingest_header structure.\n    ingest_data_headers : list of dict\n        Ingest_data_header structures for each data type.  Indexed by the\n        data type name (str).  None when data has not yet been read.\n    data_types : list\n        List of data types (int) in the file.\n    data_type_names : list\n        List of data type names (stR) in the file.\n    ndata_types : int\n        Number of data types in the file.\n    _fh : file\n        Open file being read.\n    _raw_product_bhdrs : list\n        List of raw_product_bhdr structure dictionaries seperated by sweep.\n        None when data has not yet been read.\n\n    '
    __class__ = SigmetFile
    def __init__(self):
        ' initalize the object. '
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
    
    def _determine_data_types(self):
        ' Determine the available data types in the file. '
        pass
    
    @property
    def _fh(self):
        pass
    
    def _get_sweep(self):
        '\n        Get the data and metadata from the next sweep.\n\n        If the file ends early None is returned for all values.\n\n        Parameters\n        ----------\n        full_xhdr : bool\n            True to return the full extended headers if they exist padded with\n            ones.  False will return a length 1 extended header converted to\n            int32.  This is useful when the file contains a customer specified\n            extended header (for example aircraft radar).\n        raw_data : bool, optional\n            True to return the raw_data for the given sweep, False to\n            convert the data to floating point representation.\n\n        Returns\n        -------\n        ingest_data_headers : list of dict\n            List of ingest_data_header structures for each data type.\n        sweep_data : list of arrays\n            Sweep data for each data types in the order they appear in the\n            file.\n        sweep_metadata : list of tuples\n            Sweep metadata for each data type in the same order as sweep_data.\n\n        '
        pass
    
    @property
    def _raw_product_bhdrs(self):
        pass
    
    @property
    def _rbuf_pos(self):
        pass
    
    @property
    def _record_number(self):
        pass
    
    def close(self):
        ' Close the file. '
        pass
    
    @property
    def data_type_names(self):
        pass
    
    @property
    def data_types(self):
        pass
    
    @property
    def debug(self):
        pass
    
    @property
    def ingest_data_headers(self):
        pass
    
    @property
    def ingest_header(self):
        pass
    
    @property
    def ndata_types(self):
        pass
    
    @property
    def product_hdr(self):
        pass
    
    def read_data(self):
        "\n        Read all data from the file.\n\n        Parameters\n        ----------\n        full_xhdr : bool\n            True to return the full extended headers if they exist padded with\n            ones.  False will return a length 1 extended header converted to\n            int32.  This is useful when the file contains a customer specified\n            extended header (for example aircraft radar).\n\n        Returns\n        -------\n        data : dict of ndarrays\n            Data arrays of shape=(nsweeps, nrays, nbins) for each data type.\n            Indexed by data type name (str).\n        metadata : dict of dicts\n            Arrays of 'azimuth_0', 'azimuth_1', 'elevation_0', 'elevation_1',\n            'nbins', and 'time' for each data type.  Indexed by data type name\n            (str).  Rays which were not collected are marked with a value of\n            -1 in the 'nbins' array.\n\n        "
        pass
    

TASK_CALIB_INFO = _mod_builtins.tuple()
TASK_CONFIGURATION = _mod_builtins.tuple()
TASK_DSP_INFO = _mod_builtins.tuple()
TASK_DSP_MODE_BATCH = _mod_builtins.tuple()
TASK_END_INFO = _mod_builtins.tuple()
TASK_FILE_SCAN_INFO = _mod_builtins.tuple()
TASK_MANUAL_SCAN_INFO = _mod_builtins.tuple()
TASK_MISC_INFO = _mod_builtins.tuple()
TASK_PPI_SCAN_INFO = _mod_builtins.tuple()
TASK_RANGE_INFO = _mod_builtins.tuple()
TASK_RHI_SCAN_INFO = _mod_builtins.tuple()
TASK_SCAN_INFO = _mod_builtins.tuple()
TASK_SCHED_INFO = _mod_builtins.tuple()
UINT1 = 'B'
UINT16_T = 'H'
UINT2 = 'H'
UINT4 = 'I'
YMDS_TIME = _mod_builtins.tuple()
__builtins__ = {}
__doc__ = '\npyart.io._sigmetfile\n====================\n\nA class and supporting functions for reading Sigmet (raw format) files.\n\n.. autosummary::\n    :toctree: generated/\n\n    SigmetFile\n    convert_sigmet_data\n    bin2_to_angle\n    bin4_to_angle\n    _data_types_from_mask\n    _is_bit_set\n    _parse_ray_headers\n    _unpack_structure\n    _unpack_key\n    _unpack_ingest_data_headers\n    _unpack_ingest_data_header\n    _unpack_raw_prod_bhdr\n    _unpack_product_hdr\n    _unpack_ingest_header\n\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pyart/io/_sigmetfile.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pyart.io._sigmetfile'
__package__ = 'pyart.io'
__test__ = _mod_builtins.dict()
def _data_types_from_mask():
    '\n    Return a list of the data types from the words in the data_type mask.\n    '
    pass

def _is_bit_set():
    ' Return True if bit is set in number. '
    pass

def _parse_ray_headers():
    '\n    Parse the metadata from Sigmet ray headers.\n\n    Parameters\n    ----------\n    ray_headers : array, shape=(..., 6)\n        Ray headers to parse.\n\n    Returns\n    -------\n    az0 : array\n        Azimuth angles (in degrees) at beginning of the rays.\n    el0 : array\n        Elevation angles at the beginning of the rays.\n    az1 : array\n        Azimuth angles at the end of the rays.\n    el1 : array\n        Elevation angles at the end of the rays.\n    nbins : array\n        Number of bins in the rays.\n    time : array\n        Seconds since the start of the sweep for the rays.\n    prf_flag : array\n        Numerical indication of what PRF was used, 0 for high, 1 for low.\n        Not applicable if dual-PRF is not used during collection.\n\n    '
    pass

def _unpack_ingest_data_header():
    '\n    Unpack a single ingest_data_header from record.  Return None on error.\n    '
    pass

def _unpack_ingest_data_headers():
    '\n    Unpack one or more ingest_data_header from a record.\n\n    Returns a list of dictionaries or None when an error occurs.\n\n    '
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


def _unpack_ingest_header():
    '\n    Return a dict with the unpacked ingest_header from the second record.\n    '
    pass

def _unpack_key():
    ' Unpack a key. '
    pass

def _unpack_product_hdr():
    '\n    Return a dict with the unpacked product_hdr from the first record.\n    '
    pass

def _unpack_raw_prod_bhdr():
    ' Return a dict with the unpacked raw_prod_bhdr from a record. '
    pass

def _unpack_structure():
    ' Unpack a structure '
    pass

def bin2_to_angle():
    ' Return an angle from Sigmet bin2 encoded value (or array). '
    pass

def bin4_to_angle():
    ' Return an angle from Sigmet bin4 encoded value (or array). '
    pass

def convert_sigmet_data():
    ' Convert sigmet data. '
    pass

