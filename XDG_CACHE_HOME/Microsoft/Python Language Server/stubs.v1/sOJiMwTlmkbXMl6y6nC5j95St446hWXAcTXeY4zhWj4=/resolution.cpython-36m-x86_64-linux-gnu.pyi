import builtins as _mod_builtins
import pandas._libs.properties as _mod_pandas__libs_properties
import pandas._libs.tslibs.timestamps as _mod_pandas__libs_tslibs_timestamps

MONTH_ALIASES = _mod_builtins.dict()
class Resolution(_mod_builtins.object):
    RESO_DAY = 6
    RESO_HR = 5
    RESO_MIN = 4
    RESO_MS = 2
    RESO_NS = 0
    RESO_SEC = 3
    RESO_US = 1
    __class__ = Resolution
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.resolution'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    _freq_reso_map = _mod_builtins.dict()
    _reso_freq_map = _mod_builtins.dict()
    _reso_mult_map = _mod_builtins.dict()
    _reso_str_bump_map = _mod_builtins.dict()
    _reso_str_map = _mod_builtins.dict()
    _str_reso_map = _mod_builtins.dict()
    def get_freq(self, cls, resostr):
        "\n        Return frequency str against resolution str.\n\n        Example\n        -------\n        >>> f.Resolution.get_freq('day')\n        'D'\n        "
        pass
    
    def get_freq_group(self, cls, resostr):
        "\n        Return frequency str against resolution str.\n\n        Example\n        -------\n        >>> f.Resolution.get_freq_group('day')\n        4000\n        "
        pass
    
    def get_reso(self, cls, resostr):
        "\n        Return resolution str against resolution code.\n\n        Example\n        -------\n        >>> Resolution.get_reso('second')\n        2\n\n        >>> Resolution.get_reso('second') == Resolution.RESO_SEC\n        True\n        "
        pass
    
    def get_reso_from_freq(self, cls, freq):
        "\n        Return resolution code against frequency str.\n\n        Example\n        -------\n        >>> Resolution.get_reso_from_freq('H')\n        4\n\n        >>> Resolution.get_reso_from_freq('H') == Resolution.RESO_HR\n        True\n        "
        pass
    
    def get_str(self, cls, reso):
        "\n        Return resolution str against resolution code.\n\n        Example\n        -------\n        >>> Resolution.get_str(Resolution.RESO_SEC)\n        'second'\n        "
        pass
    
    def get_str_from_freq(self, cls, freq):
        "\n        Return resolution str against frequency str.\n\n        Example\n        -------\n        >>> Resolution.get_str_from_freq('H')\n        'hour'\n        "
        pass
    
    def get_stride_from_decimal(self, cls, value, freq):
        "\n        Convert freq with decimal stride into a higher freq with integer stride\n\n        Parameters\n        ----------\n        value : integer or float\n        freq : string\n            Frequency string\n\n        Raises\n        ------\n        ValueError\n            If the float cannot be converted to an integer at any resolution.\n\n        Example\n        -------\n        >>> Resolution.get_stride_from_decimal(1.5, 'T')\n        (90, 'S')\n\n        >>> Resolution.get_stride_from_decimal(1.04, 'H')\n        (3744, 'S')\n\n        >>> Resolution.get_stride_from_decimal(1, 'D')\n        (1, 'D')\n        "
        pass
    

Timestamp = _mod_pandas__libs_tslibs_timestamps.Timestamp
class _FrequencyInferer(_mod_builtins.object):
    '\n    Not sure if I can avoid the state machine here\n    '
    __class__ = _FrequencyInferer
    __dict__ = {}
    def __init__(self, index, warn):
        '\n    Not sure if I can avoid the state machine here\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.resolution'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _get_annual_rule(self):
        pass
    
    def _get_monthly_rule(self):
        pass
    
    def _get_quarterly_rule(self):
        pass
    
    def _get_wom_rule(self):
        pass
    
    def _infer_daily_rule(self):
        pass
    
    def _is_business_daily(self):
        pass
    
    day_deltas = _mod_pandas__libs_properties.CachedProperty()
    deltas = _mod_pandas__libs_properties.CachedProperty()
    deltas_asi8 = _mod_pandas__libs_properties.CachedProperty()
    fields = _mod_pandas__libs_properties.CachedProperty()
    def get_freq(self):
        pass
    
    hour_deltas = _mod_pandas__libs_properties.CachedProperty()
    is_unique = _mod_pandas__libs_properties.CachedProperty()
    is_unique_asi8 = _mod_pandas__libs_properties.CachedProperty()
    mdiffs = _mod_pandas__libs_properties.CachedProperty()
    def month_position_check(self):
        pass
    
    rep_stamp = _mod_pandas__libs_properties.CachedProperty()
    ydiffs = _mod_pandas__libs_properties.CachedProperty()

_ONE_DAY = 86400000000000
_ONE_HOUR = 3600000000000
_ONE_MICRO = 1000
_ONE_MILLI = 1000000
_ONE_MINUTE = 60000000000
_ONE_SECOND = 1000000000
class _TimedeltaFrequencyInferer(_FrequencyInferer):
    __class__ = _TimedeltaFrequencyInferer
    __dict__ = {}
    def __init__(self, index, warn):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _infer_daily_rule(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pandas/_libs/tslibs/resolution.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.resolution'
__package__ = 'pandas._libs.tslibs'
__test__ = _mod_builtins.dict()
def _is_multiple():
    pass

def _maybe_add_count():
    pass

def build_field_sarray():
    '\n    Datetime as int64 representation to a structured array of fields\n    '
    pass

cache_readonly = _mod_pandas__libs_properties.CachedProperty
def get_freq_group():
    "\n    Return frequency code group of given frequency str or offset.\n\n    Example\n    -------\n    >>> get_freq_group('W-MON')\n    4000\n\n    >>> get_freq_group('W-FRI')\n    4000\n    "
    pass

int_to_weekday = _mod_builtins.dict()
def resolution():
    pass

def tz_convert():
    '\n    Convert the values (in i8) from timezone1 to timezone2\n\n    Parameters\n    ----------\n    vals : int64 ndarray\n    tz1 : string / timezone object\n    tz2 : string / timezone object\n\n    Returns\n    -------\n    int64 ndarray of converted\n    '
    pass

def unique(values):
    "\n    Hash table-based unique. Uniques are returned in order\n    of appearance. This does NOT sort.\n\n    Significantly faster than numpy.unique. Includes NA values.\n\n    Parameters\n    ----------\n    values : 1d array-like\n\n    Returns\n    -------\n    unique values.\n      - If the input is an Index, the return is an Index\n      - If the input is a Categorical dtype, the return is a Categorical\n      - If the input is a Series/ndarray, the return will be an ndarray\n\n    Examples\n    --------\n    >>> pd.unique(pd.Series([2, 1, 3, 3]))\n    array([2, 1, 3])\n\n    >>> pd.unique(pd.Series([2] + [1] * 5))\n    array([2, 1])\n\n    >>> pd.unique(Series([pd.Timestamp('20160101'),\n    ...                   pd.Timestamp('20160101')]))\n    array(['2016-01-01T00:00:00.000000000'], dtype='datetime64[ns]')\n\n    >>> pd.unique(pd.Series([pd.Timestamp('20160101', tz='US/Eastern'),\n    ...                      pd.Timestamp('20160101', tz='US/Eastern')]))\n    array([Timestamp('2016-01-01 00:00:00-0500', tz='US/Eastern')],\n          dtype=object)\n\n    >>> pd.unique(pd.Index([pd.Timestamp('20160101', tz='US/Eastern'),\n    ...                     pd.Timestamp('20160101', tz='US/Eastern')]))\n    DatetimeIndex(['2016-01-01 00:00:00-05:00'],\n    ...           dtype='datetime64[ns, US/Eastern]', freq=None)\n\n    >>> pd.unique(list('baabc'))\n    array(['b', 'a', 'c'], dtype=object)\n\n    An unordered Categorical will return categories in the\n    order of appearance.\n\n    >>> pd.unique(Series(pd.Categorical(list('baabc'))))\n    [b, a, c]\n    Categories (3, object): [b, a, c]\n\n    >>> pd.unique(Series(pd.Categorical(list('baabc'),\n    ...                                 categories=list('abc'))))\n    [b, a, c]\n    Categories (3, object): [b, a, c]\n\n    An ordered Categorical preserves the category ordering.\n\n    >>> pd.unique(Series(pd.Categorical(list('baabc'),\n    ...                                 categories=list('abc'),\n    ...                                 ordered=True)))\n    [b, a, c]\n    Categories (3, object): [a < b < c]\n\n    An array of tuples\n\n    >>> pd.unique([('a', 'b'), ('b', 'a'), ('a', 'c'), ('b', 'a')])\n    array([('a', 'b'), ('b', 'a'), ('a', 'c')], dtype=object)\n\n    See Also\n    --------\n    pandas.Index.unique\n    pandas.Series.unique\n\n    "
    pass

