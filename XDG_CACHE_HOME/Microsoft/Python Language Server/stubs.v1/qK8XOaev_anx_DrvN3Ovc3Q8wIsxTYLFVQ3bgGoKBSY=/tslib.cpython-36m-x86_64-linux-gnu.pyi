import builtins as _mod_builtins
import pandas._libs.tslibs.nattype as _mod_pandas__libs_tslibs_nattype
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime
import pandas._libs.tslibs.timedeltas as _mod_pandas__libs_tslibs_timedeltas
import pandas._libs.tslibs.timestamps as _mod_pandas__libs_tslibs_timestamps
import pytz as _mod_pytz
import pytz.tzinfo as _mod_pytz_tzinfo

NaT = _mod_pandas__libs_tslibs_nattype.NaTType()
OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
Timedelta = _mod_pandas__libs_tslibs_timedeltas.Timedelta
Timestamp = _mod_pandas__libs_tslibs_timestamps.Timestamp
UTC = _mod_pytz.UTC()
__builtins__ = {}
__doc__ = None
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pandas/_libs/tslib.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslib'
__package__ = 'pandas._libs'
__test__ = _mod_builtins.dict()
def _localize_pydatetime():
    '\n    Take a datetime/Timestamp in UTC and localizes to timezone tz.\n    '
    pass

def _test_parse_iso8601():
    '\n    TESTING ONLY: Parse string into Timestamp using iso8601 parser. Used\n    only for testing, actual construction uses `convert_str_to_tsobject`\n    '
    pass

def array_to_datetime():
    pass

def array_with_unit_to_datetime():
    '\n    convert the ndarray according to the unit\n    if errors:\n      - raise: return converted values or raise OutOfBoundsDatetime\n          if out of range on the conversion or\n          ValueError for other conversions (e.g. a string)\n      - ignore: return non-convertible values as the same unit\n      - coerce: NaT for non-convertibles\n\n    '
    pass

def format_array_from_datetime():
    '\n    return a np object array of the string formatted values\n\n    Parameters\n    ----------\n    values : a 1-d i8 array\n    tz : the timezone (or None)\n    format : optional, default is None\n          a strftime capable string\n    na_rep : optional, default is None\n          a nat format\n\n    '
    pass

iNaT = -9223372036854775808
def ints_to_pydatetime():
    "\n    Convert an i8 repr to an ndarray of datetimes, date, time or Timestamp\n\n    Parameters\n    ----------\n    arr  : array of i8\n    tz   : str, default None\n         convert to this timezone\n    freq : str/Offset, default None\n         freq to convert\n    box  : {'datetime', 'timestamp', 'date', 'time'}, default 'datetime'\n         If datetime, convert to datetime.datetime\n         If date, convert to datetime.date\n         If time, convert to datetime.time\n         If Timestamp, convert to pandas.Timestamp\n\n    Returns\n    -------\n    result : array of dtype specified by box\n    "
    pass

def ints_to_pytimedelta():
    pass

def monthrange():
    pass

nat_strings = _mod_builtins.set()
def normalize_date():
    '\n    Normalize datetime.datetime value to midnight. Returns datetime.date as a\n    datetime.datetime at midnight\n\n    Returns\n    -------\n    normalized : datetime.datetime or Timestamp\n    '
    pass

def parse_datetime_string():
    'parse datetime string, only returns datetime.\n    Also cares special handling matching time patterns.\n\n    Returns\n    -------\n    datetime\n    '
    pass

def tz_convert_single():
    '\n    Convert the val (in i8) from timezone1 to timezone2\n\n    This is a single timezone version of tz_convert\n\n    Parameters\n    ----------\n    val : int64\n    tz1 : string / timezone object\n    tz2 : string / timezone object\n\n    Returns\n    -------\n    int64 converted\n\n    '
    pass

