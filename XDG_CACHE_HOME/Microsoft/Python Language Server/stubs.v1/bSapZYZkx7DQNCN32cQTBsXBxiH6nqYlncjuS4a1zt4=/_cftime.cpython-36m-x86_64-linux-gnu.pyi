import _sre as _mod__sre
import builtins as _mod_builtins
import datetime as _mod_datetime

def DateFromJulianDay():
    "\n\n    returns a 'datetime-like' object given Julian Day. Julian Day is a\n    fractional day with approximately 10 microsecond accuracy.\n\n    if calendar='standard' or 'gregorian' (default), Julian day follows Julian\n    Calendar on and before 1582-10-5, Gregorian calendar after  1582-10-15.\n\n    if calendar='proleptic_gregorian', Julian Day follows gregorian calendar.\n\n    if calendar='julian', Julian Day follows julian calendar.\n\n    If only_use_cftime_datetimes is set to True, then cftime.datetime\n    objects are returned for all calendars.  Otherwise the datetime object is a\n    'real' datetime object if the date falls in the Gregorian calendar\n    (i.e. calendar='proleptic_gregorian', or  calendar = 'standard'/'gregorian'\n    and the date is after 1582-10-15).  In all other cases a 'phony' datetime\n    objects are used, which are actually instances of cftime.datetime.\n    "
    pass

class Datetime360Day(datetime):
    'Datetime360Day(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the "360_day" calendar.\n    '
    __class__ = Datetime360Day
    def __init__(self, *args, **kwargs):
        'Datetime360Day(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the "360_day" calendar.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DatetimeAllLeap(datetime):
    'DatetimeAllLeap(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the "all_leap" ("366_day") calendar.\n    '
    __class__ = DatetimeAllLeap
    def __init__(self, *args, **kwargs):
        'DatetimeAllLeap(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the "all_leap" ("366_day") calendar.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DatetimeGregorian(datetime):
    'DatetimeGregorian(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the mixed Julian-Gregorian ("standard", "gregorian") calendar.\n\nThe last date of the Julian calendar is 1582-10-4, which is followed\nby 1582-10-15, using the Gregorian calendar.\n\nInstances using the date after 1582-10-15 can be compared to\ndatetime.datetime instances and used to compute time differences\n(datetime.timedelta) by subtracting a DatetimeGregorian instance from\na datetime.datetime instance or vice versa.\n    '
    __class__ = DatetimeGregorian
    def __init__(self, *args, **kwargs):
        'DatetimeGregorian(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the mixed Julian-Gregorian ("standard", "gregorian") calendar.\n\nThe last date of the Julian calendar is 1582-10-4, which is followed\nby 1582-10-15, using the Gregorian calendar.\n\nInstances using the date after 1582-10-15 can be compared to\ndatetime.datetime instances and used to compute time differences\n(datetime.timedelta) by subtracting a DatetimeGregorian instance from\na datetime.datetime instance or vice versa.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DatetimeJulian(datetime):
    'DatetimeJulian(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the "julian" calendar.\n    '
    __class__ = DatetimeJulian
    def __init__(self, *args, **kwargs):
        'DatetimeJulian(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the "julian" calendar.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DatetimeNoLeap(datetime):
    'DatetimeNoLeap(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the "noleap" ("365_day") calendar.\n    '
    __class__ = DatetimeNoLeap
    def __init__(self, *args, **kwargs):
        'DatetimeNoLeap(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut uses the "noleap" ("365_day") calendar.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DatetimeProlepticGregorian(datetime):
    "DatetimeProlepticGregorian(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut allows for dates that don't exist in the proleptic gregorian calendar.\n\nSupports timedelta operations by overloading + and -.\n\nHas strftime, timetuple, replace, __repr__, and __str__ methods. The\nformat of the string produced by __str__ is controlled by self.format\n(default %Y-%m-%d %H:%M:%S). Supports comparisons with other phony\ndatetime instances using the same calendar; comparison with\ndatetime.datetime instances is possible for cftime.datetime\ninstances using 'gregorian' and 'proleptic_gregorian' calendars.\n\nInstance variables are year,month,day,hour,minute,second,microsecond,dayofwk,dayofyr,\nformat, and calendar.\n    "
    __class__ = DatetimeProlepticGregorian
    def __init__(self, *args, **kwargs):
        "DatetimeProlepticGregorian(*args, **kwargs)\n\nPhony datetime object which mimics the python datetime object,\nbut allows for dates that don't exist in the proleptic gregorian calendar.\n\nSupports timedelta operations by overloading + and -.\n\nHas strftime, timetuple, replace, __repr__, and __str__ methods. The\nformat of the string produced by __str__ is controlled by self.format\n(default %Y-%m-%d %H:%M:%S). Supports comparisons with other phony\ndatetime instances using the same calendar; comparison with\ndatetime.datetime instances is possible for cftime.datetime\ninstances using 'gregorian' and 'proleptic_gregorian' calendars.\n\nInstance variables are year,month,day,hour,minute,second,microsecond,dayofwk,dayofyr,\nformat, and calendar.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

ISO8601_REGEX = _mod__sre.SRE_Pattern()
def JulianDayFromDate(date, calendar='standard'):
    "JulianDayFromDate(date, calendar='standard')\n\n    creates a Julian Day from a 'datetime-like' object.  Returns the fractional\n    Julian Day (approximately 10 microsecond accuracy).\n\n    if calendar='standard' or 'gregorian' (default), Julian day follows Julian\n    Calendar on and before 1582-10-5, Gregorian calendar after 1582-10-15.\n\n    if calendar='proleptic_gregorian', Julian Day follows gregorian calendar.\n\n    if calendar='julian', Julian Day follows julian calendar.\n    "
    pass

MINYEAR = 1
TIMEZONE_REGEX = _mod__sre.SRE_Pattern()
__builtins__ = {}
__doc__ = '\nPerforms conversions of netCDF time coordinate data to/from datetime objects.\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/cftime/_cftime.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'cftime._cftime'
__package__ = 'cftime'
__path__ = None
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
__version__ = '1.0.2.1'
_calendars = _mod_builtins.list()
def _date2index():
    "\n    _date2index(dates, nctime, calendar=None, select='exact')\n\n    Return indices of a netCDF time variable corresponding to the given dates.\n\n    @param dates: A datetime object or a sequence of datetime objects.\n    The datetime objects should not include a time-zone offset.\n\n    @param nctime: A netCDF time variable object. The nctime object must have a\n    C{units} attribute. The entries are assumed to be stored in increasing\n    order.\n\n    @param calendar: Describes the calendar used in the time calculation.\n    Valid calendars C{'standard', 'gregorian', 'proleptic_gregorian'\n    'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'}.\n    Default is C{'standard'}, which is a mixed Julian/Gregorian calendar\n    If C{calendar} is None, its value is given by C{nctime.calendar} or\n    C{standard} if no such attribute exists.\n\n    @param select: C{'exact', 'before', 'after', 'nearest'}\n    The index selection method. C{exact} will return the indices perfectly\n    matching the dates given. C{before} and C{after} will return the indices\n    corresponding to the dates just before or just after the given dates if\n    an exact match cannot be found. C{nearest} will return the indices that\n    correspond to the closest dates.\n    "
    pass

def _dateparse():
    'parse a string of the form time-units since yyyy-mm-dd hh:mm:ss,\n    return a datetime instance'
    pass

def _datesplit():
    "split a time string into two components, units and the remainder \n    after 'since'\n    "
    pass

_illegal_s = _mod__sre.SRE_Pattern()
def _parse_date():
    'Parses ISO 8601 dates into datetime objects\n\n    The timezone is parsed from the date string, assuming UTC\n    by default.\n\n    Adapted from pyiso8601 (http://code.google.com/p/pyiso8601/)\n    '
    pass

def _round_half_up():
    pass

_units = _mod_builtins.list()
calendar = '360_day'
def date2index(dates, nctime, calendar=None, select='exact'):
    "date2index(dates, nctime, calendar=None, select='exact')\n\n    Return indices of a netCDF time variable corresponding to the given dates.\n\n    **`dates`**: A datetime object or a sequence of datetime objects.\n    The datetime objects should not include a time-zone offset.\n\n    **`nctime`**: A netCDF time variable object. The nctime object must have a\n    `units` attribute.\n\n    **`calendar`**: describes the calendar used in the time calculations.\n    All the values currently defined in the\n    [CF metadata convention](http://cfconventions.org)\n    Valid calendars `'standard', 'gregorian', 'proleptic_gregorian'\n    'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'`.\n    Default is `'standard'`, which is a mixed Julian/Gregorian calendar.\n    If `calendar` is None, its value is given by `nctime.calendar` or\n    `standard` if no such attribute exists.\n\n    **`select`**: `'exact', 'before', 'after', 'nearest'`\n    The index selection method. `exact` will return the indices perfectly\n    matching the dates given. `before` and `after` will return the indices\n    corresponding to the dates just before or just after the given dates if\n    an exact match cannot be found. `nearest` will return the indices that\n    correspond to the closest dates.\n\n    returns an index (indices) of the netCDF time variable corresponding\n    to the given datetime object(s).\n    "
    pass

def date2num(dates, units, calendar='standard'):
    "date2num(dates,units,calendar='standard')\n\n    Return numeric time values given datetime objects. The units\n    of the numeric time values are described by the `units` argument\n    and the `calendar` keyword. The datetime objects must\n    be in UTC with no time-zone offset.  If there is a\n    time-zone offset in `units`, it will be applied to the\n    returned numeric values.\n\n    **`dates`**: A datetime object or a sequence of datetime objects.\n    The datetime objects should not include a time-zone offset.\n\n    **`units`**: a string of the form `<time units> since <reference time>`\n    describing the time units. `<time units>` can be days, hours, minutes,\n    seconds, milliseconds or microseconds. `<reference time>` is the time\n    origin. `months_since` is allowed *only* for the `360_day` calendar.\n\n    **`calendar`**: describes the calendar used in the time calculations.\n    All the values currently defined in the\n    [CF metadata convention](http://cfconventions.org)\n    Valid calendars `'standard', 'gregorian', 'proleptic_gregorian'\n    'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'`.\n    Default is `'standard'`, which is a mixed Julian/Gregorian calendar.\n\n    returns a numeric time value, or an array of numeric time values\n    with approximately 10 microsecond accuracy.\n        "
    pass

class datetime(_mod_builtins.object):
    'datetime(int year, int month, int day, int hour=0, int minute=0, int second=0, int microsecond=0, int dayofwk=-1, int dayofyr=1)\n\nThe base class implementing most methods of datetime classes that\nmimic datetime.datetime but support calendars other than the proleptic\nGregorial calendar.\n    '
    def __add__(self, value):
        'Return self+value.'
        return datetime()
    
    __class__ = datetime
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, intyear, intmonth, intday, inthour=0, intminute=0, intsecond=0, intmicrosecond=0, intdayofwk=-1, intdayofyr=1):
        'dayofyr set to 1 by default - otherwise time.strftime will complain'
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
    def __radd__(self, value):
        'Return value+self.'
        return datetime()
    
    def __reduce__(self):
        'datetime.__reduce__(self)\nspecial method that allows instance to be pickled'
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rsub__(self, value):
        'Return value-self.'
        return datetime()
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return datetime()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _to_real_datetime(self):
        'datetime._to_real_datetime(self)'
        pass
    
    @property
    def calendar(self):
        pass
    
    @property
    def datetime_compatible(self):
        pass
    
    @property
    def day(self):
        pass
    
    @property
    def dayofwk(self):
        pass
    
    @property
    def dayofyr(self):
        pass
    
    @property
    def format(self):
        pass
    
    @property
    def hour(self):
        pass
    
    @property
    def microsecond(self):
        pass
    
    @property
    def minute(self):
        pass
    
    @property
    def month(self):
        pass
    
    def replace(self):
        'datetime.replace(self, **kwargs)\nReturn datetime with new specified fields.'
        pass
    
    @property
    def second(self):
        pass
    
    def strftime(self):
        "datetime.strftime(self, format=None)\n\n        Return a string representing the date, controlled by an explicit format\n        string. For a complete list of formatting directives, see section\n        'strftime() and strptime() Behavior' in the base Python documentation.\n        "
        pass
    
    def timetuple(self):
        'datetime.timetuple(self)\n\n        Return a time.struct_time such as returned by time.localtime().\n        The DST flag is -1. d.timetuple() is equivalent to\n        time.struct_time((d.year, d.month, d.day, d.hour, d.minute,\n        d.second, d.weekday(), yday, dst)), where yday is the\n        day number within the current year starting with 1 for January 1st.\n        '
        pass
    
    @property
    def year(self):
        pass
    

datetime_python = _mod_datetime.datetime
day_units = _mod_builtins.list()
gregorian = real_datetime()
hr_units = _mod_builtins.list()
microsec_units = _mod_builtins.list()
millisec_units = _mod_builtins.list()
min_units = _mod_builtins.list()
month_units = _mod_builtins.list()
def num2date(times, units, calendar='standard'):
    "num2date(times,units,calendar='standard')\n\n    Return datetime objects given numeric time values. The units\n    of the numeric time values are described by the `units` argument\n    and the `calendar` keyword. The returned datetime objects represent\n    UTC with no time-zone offset, even if the specified\n    `units` contain a time-zone offset.\n\n    **`times`**: numeric time values.\n\n    **`units`**: a string of the form `<time units> since <reference time>`\n    describing the time units. `<time units>` can be days, hours, minutes,\n    seconds, milliseconds or microseconds. `<reference time>` is the time\n    origin. `months_since` is allowed *only* for the `360_day` calendar.\n\n    **`calendar`**: describes the calendar used in the time calculations.\n    All the values currently defined in the\n    [CF metadata convention](http://cfconventions.org)\n    Valid calendars `'standard', 'gregorian', 'proleptic_gregorian'\n    'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'`.\n    Default is `'standard'`, which is a mixed Julian/Gregorian calendar.\n\n    **`only_use_cftime_datetimes`**: if False (default), datetime.datetime\n    objects are returned from num2date where possible; if True dates which\n    subclass cftime.datetime are returned for all calendars.\n\n    returns a datetime instance, or an array of datetime instances with\n    approximately 10 microsecond accuracy.\n\n    ***Note***: The datetime instances returned are 'real' python datetime\n    objects if `calendar='proleptic_gregorian'`, or\n    `calendar='standard'` or `'gregorian'`\n    and the date is after the breakpoint between the Julian and\n    Gregorian calendars (1582-10-15). Otherwise, they are 'phony' datetime\n    objects which support some but not all the methods of 'real' python\n    datetime objects. The datetime instances\n    do not contain a time-zone offset, even if the specified `units`\n    contains one.\n    "
    pass

class real_datetime(_mod_datetime.datetime):
    'add dayofwk and dayofyr attributes to python datetime instance'
    __class__ = real_datetime
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'add dayofwk and dayofyr attributes to python datetime instance'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'cftime._cftime'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def combine(cls):
        'date, time -> datetime with same date and time fields'
        pass
    
    dayofwk = _mod_builtins.property()
    dayofyr = _mod_builtins.property()
    @classmethod
    def fromordinal(cls):
        'int -> date corresponding to a proleptic Gregorian ordinal.'
        pass
    
    @classmethod
    def fromtimestamp(cls):
        "timestamp[, tz] -> tz's local time from POSIX timestamp."
        pass
    
    @classmethod
    def now(cls, type, tz):
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        pass
    
    @classmethod
    def strptime(cls):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        pass
    
    @classmethod
    def today(cls):
        'Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).'
        pass
    
    @classmethod
    def utcfromtimestamp(cls):
        'Construct a naive UTC datetime from a POSIX timestamp.'
        pass
    
    @classmethod
    def utcnow(cls):
        'Return a new datetime representing UTC day and time.'
        pass
    

sec_units = _mod_builtins.list()
def time2index():
    "\n    time2index(times, nctime, calendar=None, select='exact')\n\n    Return indices of a netCDF time variable corresponding to the given times.\n\n    @param times: A numeric time or a sequence of numeric times.\n\n    @param nctime: A netCDF time variable object. The nctime object must have a\n    C{units} attribute. The entries are assumed to be stored in increasing\n    order.\n\n    @param calendar: Describes the calendar used in the time calculation.\n    Valid calendars C{'standard', 'gregorian', 'proleptic_gregorian'\n    'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'}.\n    Default is C{'standard'}, which is a mixed Julian/Gregorian calendar\n    If C{calendar} is None, its value is given by C{nctime.calendar} or\n    C{standard} if no such attribute exists.\n\n    @param select: C{'exact', 'before', 'after', 'nearest'}\n    The index selection method. C{exact} will return the indices perfectly\n    matching the times given. C{before} and C{after} will return the indices\n    corresponding to the times just before or just after the given times if\n    an exact match cannot be found. C{nearest} will return the indices that\n    correspond to the closest times.\n    "
    pass

timedelta = _mod_datetime.timedelta
class utime(_mod_builtins.object):
    '\nPerforms conversions of netCDF time coordinate\ndata to/from datetime objects.\n\nTo initialize: C{t = utime(unit_string,calendar=\'standard\')}\n\nwhere\n\nB{C{unit_string}} is a string of the form\nC{\'time-units since <time-origin>\'} defining the time units.\n\nValid time-units are days, hours, minutes and seconds (the singular forms\nare also accepted). An example unit_string would be C{\'hours\nsince 0001-01-01 00:00:00\'}. months is allowed as a time unit\n*only* for the 360_day calendar.\n\nThe B{C{calendar}} keyword describes the calendar used in the time calculations.\nAll the values currently defined in the U{CF metadata convention\n<http://cf-pcmdi.llnl.gov/documents/cf-conventions/1.1/cf-conventions.html#time-coordinate>}\nare accepted. The default is C{\'standard\'}, which corresponds to the mixed\nGregorian/Julian calendar used by the C{udunits library}. Valid calendars\nare:\n\nC{\'gregorian\'} or C{\'standard\'} (default):\n\nMixed Gregorian/Julian calendar as defined by udunits.\n\nC{\'proleptic_gregorian\'}:\n\nA Gregorian calendar extended to dates before 1582-10-15. That is, a year\nis a leap year if either (i) it is divisible by 4 but not by 100 or (ii)\nit is divisible by 400.\n\nC{\'noleap\'} or C{\'365_day\'}:\n\nGregorian calendar without leap years, i.e., all years are 365 days long.\nall_leap or 366_day Gregorian calendar with every year being a leap year,\ni.e., all years are 366 days long.\n\nC{\'360_day\'}:\n\nAll years are 360 days divided into 30 day months.\n\nC{\'julian\'}:\n\nProleptic Julian calendar, extended to dates after 1582-10-5. A year is a\nleap year if it is divisible by 4.\n\nThe C{L{num2date}} and C{L{date2num}} class methods can used to convert datetime\ninstances to/from the specified time units using the specified calendar.\n\nThe datetime instances returned by C{num2date} are \'real\' python datetime\nobjects if the date falls in the Gregorian calendar (i.e.\nC{calendar=\'proleptic_gregorian\', \'standard\'} or C{\'gregorian\'} and\nthe date is after 1582-10-15). Otherwise, they are \'phony\' datetime\nobjects which are actually instances of C{L{cftime.datetime}}.  This is\nbecause the python datetime module cannot handle the weird dates in some\ncalendars (such as C{\'360_day\'} and C{\'all_leap\'}) which don\'t exist in any real\nworld calendar.\n\n\nExample usage:\n\n>>> from cftime import utime\n>>> from datetime import  datetime\n>>> cdftime = utime(\'hours since 0001-01-01 00:00:00\')\n>>> date = datetime.now()\n>>> print date\n2016-10-05 08:46:27.245015\n>>>\n>>> t = cdftime.date2num(date)\n>>> print t\n17669840.7742\n>>>\n>>> date = cdftime.num2date(t)\n>>> print date\n2016-10-05 08:46:27.244996\n>>>\n\nThe resolution of the transformation operation is approximately a millisecond.\n\nWarning:  Dates between 1582-10-5 and 1582-10-15 do not exist in the\nC{\'standard\'} or C{\'gregorian\'} calendars.  An exception will be raised if you pass\na \'datetime-like\' object in that range to the C{L{date2num}} class method.\n\nWords of Wisdom from the British MetOffice concerning reference dates:\n\n"udunits implements the mixed Gregorian/Julian calendar system, as\nfollowed in England, in which dates prior to 1582-10-15 are assumed to use\nthe Julian calendar. Other software cannot be relied upon to handle the\nchange of calendar in the same way, so for robustness it is recommended\nthat the reference date be later than 1582. If earlier dates must be used,\nit should be noted that udunits treats 0 AD as identical to 1 AD."\n\n@ivar origin: datetime instance defining the origin of the netCDF time variable.\n@ivar calendar:  the calendar used (as specified by the C{calendar} keyword).\n@ivar unit_string:  a string defining the the netCDF time variable.\n@ivar units:  the units part of C{unit_string} (i.e. \'days\', \'hours\', \'seconds\').\n    '
    __class__ = utime
    __dict__ = {}
    def __init__(self, unit_string, calendar, only_use_cftime_datetimes):
        "\n@param unit_string: a string of the form\nC{'time-units since <time-origin>'} defining the time units.\n\nValid time-units are days, hours, minutes and seconds (the singular forms\nare also accepted). An example unit_string would be C{'hours\nsince 0001-01-01 00:00:00'}. months is allowed as a time unit\n*only* for the 360_day calendar.\n\n@keyword calendar: describes the calendar used in the time calculations.\nAll the values currently defined in the U{CF metadata convention\n<http://cf-pcmdi.llnl.gov/documents/cf-conventions/1.1/cf-conventions.html#time-coordinate>}\nare accepted. The default is C{'standard'}, which corresponds to the mixed\nGregorian/Julian calendar used by the C{udunits library}. Valid calendars\nare:\n - C{'gregorian'} or C{'standard'} (default):\n Mixed Gregorian/Julian calendar as defined by udunits.\n - C{'proleptic_gregorian'}:\n A Gregorian calendar extended to dates before 1582-10-15. That is, a year\n is a leap year if either (i) it is divisible by 4 but not by 100 or (ii)\n it is divisible by 400.\n - C{'noleap'} or C{'365_day'}:\n Gregorian calendar without leap years, i.e., all years are 365 days long.\n - C{'all_leap'} or C{'366_day'}:\n Gregorian calendar with every year being a leap year, i.e.,\n all years are 366 days long.\n -C{'360_day'}:\n All years are 360 days divided into 30 day months.\n -C{'julian'}:\n Proleptic Julian calendar, extended to dates after 1582-10-5. A year is a\n leap year if it is divisible by 4.\n\n@keyword only_use_cftime_datetimes: if False (default), datetime.datetime\nobjects are returned from num2date where possible; if True dates which subclass\ncftime.datetime are returned for all calendars.\n\n@returns: A class instance which may be used for converting times from netCDF\nunits to datetime objects.\n        "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'cftime._cftime'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def date2num(self, date):
        "\n        Returns C{time_value} in units described by L{unit_string}, using\n        the specified L{calendar}, given a 'datetime-like' object.\n\n        The datetime object must represent UTC with no time-zone offset.\n        If there is a time-zone offset implied by L{unit_string}, it will\n        be applied to the returned numeric values.\n\n        Resolution is approximately a millisecond.\n\n        If C{calendar = 'standard'} or C{'gregorian'} (indicating\n        that the mixed Julian/Gregorian calendar is to be used), an\n        exception will be raised if the 'datetime-like' object describes\n        a date between 1582-10-5 and 1582-10-15.\n\n        Works for scalars, sequences and numpy arrays.\n        Returns a scalar if input is a scalar, else returns a numpy array.\n        "
        pass
    
    def num2date(self, time_value):
        "\n        Return a 'datetime-like' object given a C{time_value} in units\n        described by L{unit_string}, using L{calendar}.\n\n        dates are in UTC with no offset, even if L{unit_string} contains\n        a time zone offset from UTC.\n\n        Resolution is approximately a millisecond.\n\n        Works for scalars, sequences and numpy arrays.\n        Returns a scalar if input is a scalar, else returns a numpy array.\n\n        The datetime instances returned by C{num2date} are 'real' python datetime\n        objects if the date falls in the Gregorian calendar (i.e.\n        C{calendar='proleptic_gregorian'}, or C{calendar = 'standard'/'gregorian'} and\n        the date is after 1582-10-15). Otherwise, they are 'phony' datetime\n        objects which are actually instances of cftime.datetime.  This is\n        because the python datetime module cannot handle the weird dates in some\n        calendars (such as C{'360_day'} and C{'all_leap'}) which\n        do not exist in any real world calendar.\n        "
        pass
    

