import builtins as _mod_builtins
import datetime as _mod_datetime

class RslFile(_mod_builtins.object):
    '\n    RslFile(filename)\n\n    A object for accessing Radar data and parameter using the RSL library.\n\n    Parameters\n    ----------\n    filename : str\n        Radar file to read.\n\n    Attributes\n    ----------\n    month : int\n        Date, month (1-12).\n    day : int\n        Date, day (1-31).\n    year : int\n        Date, year (eg. 1993).\n    hour : int\n        Time, hour (0-23).\n    minute : int\n        Time, minute (0-59).\n    sec : float\n        Time, second + fractions of second.\n    nvolumes : int\n        Number of volume slots in the file.\n    number : int\n        Arbitrary number for this radar site.\n    latd, latm, lats : int\n        Latitude degrees, minutes and seconds for the site.\n    lond, lonm, lons : int\n        Longitude degrees, minutes and seconds for the site.\n    height : int\n        Height of site in meters above sea level.\n    spulse : int\n        Length of short pulse in ns.\n    lpulse : int\n        Length of long pulse in ns.\n    scan_mode : int\n        Scan mode, 0 for PPI, 1 for RHI.\n    vcp : int\n        Volume coverage pattern, WSR-88D only.\n\n    '
    __class__ = RslFile
    def __init__(self, *args, **kwargs):
        '\n    RslFile(filename)\n\n    A object for accessing Radar data and parameter using the RSL library.\n\n    Parameters\n    ----------\n    filename : str\n        Radar file to read.\n\n    Attributes\n    ----------\n    month : int\n        Date, month (1-12).\n    day : int\n        Date, day (1-31).\n    year : int\n        Date, year (eg. 1993).\n    hour : int\n        Time, hour (0-23).\n    minute : int\n        Time, minute (0-59).\n    sec : float\n        Time, second + fractions of second.\n    nvolumes : int\n        Number of volume slots in the file.\n    number : int\n        Arbitrary number for this radar site.\n    latd, latm, lats : int\n        Latitude degrees, minutes and seconds for the site.\n    lond, lonm, lons : int\n        Longitude degrees, minutes and seconds for the site.\n    height : int\n        Height of site in meters above sea level.\n    spulse : int\n        Length of short pulse in ns.\n    lpulse : int\n        Length of long pulse in ns.\n    scan_mode : int\n        Scan mode, 0 for PPI, 1 for RHI.\n    vcp : int\n        Volume coverage pattern, WSR-88D only.\n\n    '
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
    
    def available_moments(self):
        '\n        available_moments()\n\n        Return a list of available volume moments.\n        '
        pass
    
    @property
    def day(self):
        pass
    
    def get_radar_header(self):
        '\n        get_radar_headers()\n\n        Return a dictionary of radar header parameters.\n        '
        pass
    
    def get_volume(self):
        '\n        get_volume(volume_number)\n\n        Return a _RslVolume for a given volume number.\n\n        Parameters\n        ----------\n        volume_number : int\n            Volume number to retrieve\n\n        Returns\n        -------\n        volume : _RslVolume\n            _RslVolume object containing requested volume.\n\n        '
        pass
    
    def get_volume_array(self):
        '\n        get_volume_array(volume_number)\n\n        Return the three-dimensional data contained in a given volume.\n\n        Parameters\n        ----------\n        volume_number : int\n\n        Returns\n        -------\n        volume : array (nsweep, nrays, nbins), float32\n            Array containing  data for the given volume.\n\n        '
        pass
    
    @property
    def height(self):
        pass
    
    @property
    def hour(self):
        pass
    
    @property
    def latd(self):
        pass
    
    @property
    def latm(self):
        pass
    
    @property
    def lats(self):
        pass
    
    @property
    def lond(self):
        pass
    
    @property
    def lonm(self):
        pass
    
    @property
    def lons(self):
        pass
    
    @property
    def lpulse(self):
        pass
    
    @property
    def minute(self):
        pass
    
    @property
    def month(self):
        pass
    
    @property
    def number(self):
        pass
    
    @property
    def nvolumes(self):
        pass
    
    @property
    def scan_mode(self):
        pass
    
    @property
    def sec(self):
        pass
    
    @property
    def spulse(self):
        pass
    
    @property
    def vcp(self):
        pass
    
    @property
    def year(self):
        pass
    

_RSL_VERSION_STR = b'v1.49'
class _RslRay(_mod_builtins.object):
    '\n    A object for accessing RSL Ray data and header information\n\n    This class should not be initalized from within Python.  _RslRay object are\n    returned from the :py:func:`_RslSweep.get_ray` method.\n\n    Attributes\n    ----------\n    month : int\n        Date for this ray, month (1-12).\n    day : int\n        Date for this ray, day (1-31).\n    year : int\n        Date for this ray, year (eg. 1993).\n    hour : int\n        Time for this ray, hour (0-23).\n    minute : int\n        Time for this ray, minute (0-59).\n    sec : float\n        Time for this ray, second + fractor of second.\n    unam_rng : float\n        Unambiguous range in km.\n    azimuth : float\n        Mean azimuth angle in degrees for the ray, must be positive.\n        0 for north, 90 for east, 270 for west.\n    ray_num : int\n        Ray number within a scan.\n    elev : float\n        Elevation angle in degrees.\n    elev_num : int\n        Elevation number within the volume scan.\n    range_bin1 : int\n        Range to first gate in meters.\n    gate_size : int\n        Gate size in meters.\n    vel_res : float\n        Doppler velocity resolution.\n    sweep_rate : float\n        Sweep rate, full sweeps / minute.\n    prf : int\n        Pulse repetition frequency in Hz.\n    prf2 : int\n        Second pulse repition frequenct for dual PRF data.\n    azim_rate : float\n        Sweep rate in degrees / second.\n    fix_angle : float\n        Elevation angle for the sweep in degrees.\n    pitch : float\n        Pitch angle.\n    roll : float\n        Roll angle.\n    heading : float\n        Heading.\n    pitch_rate : float\n        Pitch rate in angle / sec.\n    roll_rate : float\n        Roll rate in angle / sec.\n    heading_rate : float\n        Heading rate in angle / sec.\n    lat : float\n        Latitude in degrees.\n    lon : float\n        Longitude in degrees.\n    alt : int\n        Altitude in meters.\n    rvs : float\n        Radial velocity correction in meters / second.\n    vel_east : float\n        Platform velocity to the east in meters / second.  Negative values for\n        velocity to the west.\n    vel_north : float\n        Platform velocity to the north in meters / second.  Negative values for\n        velocity to the south.\n    vel_up : float\n        Platform velocity upward in meters / second.  Negative values for\n        velocity downward.\n    pulse_count : int\n        Pulses used in a single dwell time.\n    pulse_width : float\n        Pulse width in microseconds.\n    beam_width : float\n        Beamwidth in degrees.\n    frequency : float\n        Carrier frequency in GHz.\n    wavelength : float\n        Wavelength in meters.\n    nyq_vel : float\n        Nyquist velocity in meters / second.\n    nbins : int\n        Number of array elements in ray data.\n\n    '
    __class__ = _RslRay
    def __init__(self, *args, **kwargs):
        '\n    A object for accessing RSL Ray data and header information\n\n    This class should not be initalized from within Python.  _RslRay object are\n    returned from the :py:func:`_RslSweep.get_ray` method.\n\n    Attributes\n    ----------\n    month : int\n        Date for this ray, month (1-12).\n    day : int\n        Date for this ray, day (1-31).\n    year : int\n        Date for this ray, year (eg. 1993).\n    hour : int\n        Time for this ray, hour (0-23).\n    minute : int\n        Time for this ray, minute (0-59).\n    sec : float\n        Time for this ray, second + fractor of second.\n    unam_rng : float\n        Unambiguous range in km.\n    azimuth : float\n        Mean azimuth angle in degrees for the ray, must be positive.\n        0 for north, 90 for east, 270 for west.\n    ray_num : int\n        Ray number within a scan.\n    elev : float\n        Elevation angle in degrees.\n    elev_num : int\n        Elevation number within the volume scan.\n    range_bin1 : int\n        Range to first gate in meters.\n    gate_size : int\n        Gate size in meters.\n    vel_res : float\n        Doppler velocity resolution.\n    sweep_rate : float\n        Sweep rate, full sweeps / minute.\n    prf : int\n        Pulse repetition frequency in Hz.\n    prf2 : int\n        Second pulse repition frequenct for dual PRF data.\n    azim_rate : float\n        Sweep rate in degrees / second.\n    fix_angle : float\n        Elevation angle for the sweep in degrees.\n    pitch : float\n        Pitch angle.\n    roll : float\n        Roll angle.\n    heading : float\n        Heading.\n    pitch_rate : float\n        Pitch rate in angle / sec.\n    roll_rate : float\n        Roll rate in angle / sec.\n    heading_rate : float\n        Heading rate in angle / sec.\n    lat : float\n        Latitude in degrees.\n    lon : float\n        Longitude in degrees.\n    alt : int\n        Altitude in meters.\n    rvs : float\n        Radial velocity correction in meters / second.\n    vel_east : float\n        Platform velocity to the east in meters / second.  Negative values for\n        velocity to the west.\n    vel_north : float\n        Platform velocity to the north in meters / second.  Negative values for\n        velocity to the south.\n    vel_up : float\n        Platform velocity upward in meters / second.  Negative values for\n        velocity downward.\n    pulse_count : int\n        Pulses used in a single dwell time.\n    pulse_width : float\n        Pulse width in microseconds.\n    beam_width : float\n        Beamwidth in degrees.\n    frequency : float\n        Carrier frequency in GHz.\n    wavelength : float\n        Wavelength in meters.\n    nyq_vel : float\n        Nyquist velocity in meters / second.\n    nbins : int\n        Number of array elements in ray data.\n\n    '
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
    
    @property
    def alt(self):
        pass
    
    @property
    def azim_rate(self):
        pass
    
    @property
    def azimuth(self):
        pass
    
    @property
    def beam_width(self):
        pass
    
    @property
    def day(self):
        pass
    
    @property
    def elev(self):
        pass
    
    @property
    def elev_num(self):
        pass
    
    @property
    def fix_angle(self):
        pass
    
    @property
    def frequency(self):
        pass
    
    @property
    def gate_size(self):
        pass
    
    def get_data(self):
        '\n        get_data()\n\n        Return the one-dimensional data contained in the ray.\n        '
        pass
    
    def get_datetime(self):
        '\n        get_datetime()\n\n        Return a datetime describing the date and time of the ray.\n        '
        pass
    
    @property
    def heading(self):
        pass
    
    @property
    def heading_rate(self):
        pass
    
    @property
    def hour(self):
        pass
    
    @property
    def lat(self):
        pass
    
    @property
    def lon(self):
        pass
    
    @property
    def minute(self):
        pass
    
    @property
    def month(self):
        pass
    
    @property
    def nbins(self):
        pass
    
    @property
    def nyq_vel(self):
        pass
    
    @property
    def pitch(self):
        pass
    
    @property
    def pitch_rate(self):
        pass
    
    @property
    def prf(self):
        pass
    
    @property
    def prf2(self):
        pass
    
    @property
    def pulse_count(self):
        pass
    
    @property
    def pulse_width(self):
        pass
    
    @property
    def range_bin1(self):
        pass
    
    @property
    def ray_num(self):
        pass
    
    @property
    def roll(self):
        pass
    
    @property
    def roll_rate(self):
        pass
    
    @property
    def rvc(self):
        pass
    
    @property
    def sec(self):
        pass
    
    @property
    def sweep_rate(self):
        pass
    
    @property
    def unam_rng(self):
        pass
    
    @property
    def vel_east(self):
        pass
    
    @property
    def vel_north(self):
        pass
    
    @property
    def vel_res(self):
        pass
    
    @property
    def vel_up(self):
        pass
    
    @property
    def wavelength(self):
        pass
    
    @property
    def year(self):
        pass
    

class _RslSweep(_mod_builtins.object):
    '\n    A object for accessing RSL Sweep data and header information.\n\n    This class should not be initalized from within Python.  _RslSweep objects\n    are returned from the :py:func:`_RslVolume.get_sweep` method.\n\n    Attributes\n    ----------\n    sweep_num : int\n        Interger sweep number.\n    elev : float\n        Mean elevation angle for thr sweep.  -999.0 for RHI sweeps.\n    azimuth : float\n        Azumuth for the sweep.  -999.0 for PPI scans.\n    beam_width : float\n        Beam width in degrees.  Can also be found in _RslRay objects.\n    vert_half_bw : float\n        Vertical beam width divided by 2.\n    horz_half_bw : float\n        Horizontal beam width divided by 2.\n    nrays : int\n        Number of rays in the sweep.\n\n    '
    __class__ = _RslSweep
    def __init__(self, *args, **kwargs):
        '\n    A object for accessing RSL Sweep data and header information.\n\n    This class should not be initalized from within Python.  _RslSweep objects\n    are returned from the :py:func:`_RslVolume.get_sweep` method.\n\n    Attributes\n    ----------\n    sweep_num : int\n        Interger sweep number.\n    elev : float\n        Mean elevation angle for thr sweep.  -999.0 for RHI sweeps.\n    azimuth : float\n        Azumuth for the sweep.  -999.0 for PPI scans.\n    beam_width : float\n        Beam width in degrees.  Can also be found in _RslRay objects.\n    vert_half_bw : float\n        Vertical beam width divided by 2.\n    horz_half_bw : float\n        Horizontal beam width divided by 2.\n    nrays : int\n        Number of rays in the sweep.\n\n    '
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
    
    @property
    def azimuth(self):
        pass
    
    @property
    def beam_width(self):
        pass
    
    @property
    def elev(self):
        pass
    
    def get_data(self):
        '\n        get_data()\n\n        Return the two-dimensional data contained in the sweep.\n\n        If a given ray has few bins than the first ray, the missing bins\n        will be filled with 131072.0\n        '
        pass
    
    def get_ray(self):
        '\n        get_ray(ray_number)\n\n        Return a _RslRay for a given ray.\n\n        Parameters\n        ----------\n        ray_number : int\n            Ray number to retrieve\n\n        Returns\n        -------\n        ray : _RslRay\n            _RslRay object containing the requested ray.\n\n        '
        pass
    
    @property
    def horz_half_bw(self):
        pass
    
    @property
    def nrays(self):
        pass
    
    @property
    def sweep_num(self):
        pass
    
    @property
    def vert_half_bw(self):
        pass
    

class _RslVolume(_mod_builtins.object):
    '\n    A object for accessing RSL Volume data and header information.\n\n    This class should not be initalized from within Python.  _RslVolume\n    objects are returned from the :py:func:`RslFile.get_volume` and other\n    functions/methods.\n\n    Attributes\n    ----------\n    nsweeps : int\n        Sweep number.\n    calibr_const : float\n        Calibration constant.\n\n    '
    __class__ = _RslVolume
    def __init__(self, *args, **kwargs):
        '\n    A object for accessing RSL Volume data and header information.\n\n    This class should not be initalized from within Python.  _RslVolume\n    objects are returned from the :py:func:`RslFile.get_volume` and other\n    functions/methods.\n\n    Attributes\n    ----------\n    nsweeps : int\n        Sweep number.\n    calibr_const : float\n        Calibration constant.\n\n    '
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
    
    @property
    def calibr_const(self):
        pass
    
    def get_azimuth_and_elev_array(self):
        '\n        get_azimuth_and_elev_array()\n\n        Return azimuth and elevation array for each sweep and ray.\n        '
        pass
    
    def get_data(self):
        '\n        get_data()\n\n        Return the two-dimensional data contained in the volume.\n\n        If a given ray has few bins than the first ray, the missing bins\n        will be filled with 131072.0\n        '
        pass
    
    def get_instr_params(self):
        '\n        get_instr_params()\n\n        Return instrumental parameter for the volume.\n\n        Returns\n        -------\n        pm_data : array, (nsweeps)\n            Array of prt modes.\n        nv_data : array, (total_rays)\n            Array of nyquist velocities.\n        pr_data : array, (total_rays)\n            Array of pulse repetition frequency in Hz.\n        ur_data : array, (total_rays)\n            Array of unambiguous ranges, in km.\n\n        '
        pass
    
    def get_nray_array(self):
        '\n        get_nray_array()\n\n        Return an array of the number of rays for each sweep.\n        '
        pass
    
    def get_sweep(self):
        '\n        get_sweep(sweep_numer)\n\n        Return a _RslSweep for a given sweep number.\n\n        Parameters\n        ----------\n        sweep_number : int\n            Sweep number to retrieve\n\n        Returns\n        -------\n        sweep : _RslSweep\n            _RslSweep object containing the requested sweep.\n\n        '
        pass
    
    def get_sweep_azimuths(self):
        '\n        get_sweep_azimuths()\n\n        Return azimuth array for each sweep.\n        '
        pass
    
    def get_sweep_elevs(self):
        '\n        get_sweep_elevs()\n\n        Return elevation array for each sweep.\n        '
        pass
    
    def get_sweep_fix_angles(self):
        '\n        get_sweep_fix_angles()\n\n        Return array of fix angle for each sweep.\n\n        Angles determined from the first ray in each sweep.\n        '
        pass
    
    def is_range_bins_uniform(self):
        '\n        is_range_bins_uniform()\n\n        Return True is the locations of the range bin are identical for all\n        rays, False if locations change in one or more rays.\n        '
        pass
    
    @property
    def nsweeps(self):
        pass
    
    def total_rays(self):
        '\n        total_rays()\n\n        Return the total number of rays present in all sweeps of the volume.\n        '
        pass
    

__builtins__ = {}
__doc__ = '\npyart.io._rsl_interface\n=======================\n\nCython wrapper around the NASA TRMM RSL library.\n\n.. autosummary::\n    :toctree: generated/\n\n    copy_volume\n    create_volume\n    _label_volume\n\n.. autosummary::\n    :toctree: generated/\n    :template: dev_template.rst\n\n    RslFile\n    _RslVolume\n    _RslSweep\n    _RslRay\n\n\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pyart/io/_rsl_interface.cpython-36m-x86_64-linux-gnu.so'
## You are using the Python ARM Radar Toolkit (Py-ART), an open source
## library for working with weather radar data. Py-ART is partly
## supported by the U.S. Department of Energy as part of the Atmospheric
## Radiation Measurement (ARM) Climate Research Facility, an Office of
## Science user facility.
##
## If you use this software to prepare a publication, please cite:
##
##     JJ Helmus and SM Collis, JORS 2016, doi: 10.5334/jors.119


__name__ = 'pyart.io._rsl_interface'
__package__ = 'pyart.io'
__test__ = _mod_builtins.dict()
def _label_volume():
    '\n    _label_volume(volume, radar)\n\n    Add labels for dealiasing to a _RslVolume object from a radar object.\n\n    This function does not set all parameter in the _RslVolume suitable for\n    writing out the volume, rather it set those parameters which must be set\n    prior to using :py:func:`pyart.correct._fourdd_interface.fourdd_dealias`.\n\n    Parameters\n    ----------\n    volume : _RslVolume\n        Volume object to which parameters will be set as needed prior to\n        dealiasing.  Object is manipulated in-place.\n    radar : Radar\n        Radar object from which parameters are taken.\n\n    '
    pass

def copy_volume():
    '\n    copy_volume(volume)\n\n    Return a copy of a _RslVolume object.\n\n    Parameters\n    ----------\n    volume : _RslVolume\n        _RslVolume object to create a copy of.\n\n    Returns\n    -------\n    nvolume : _RslVolume\n        Copy of volume.\n\n    '
    pass

def create_volume():
    '\n    create_volume(arr, rays_per_sweep, vol_num=1)\n\n    Create a _RslVolume object from a 2D float32 array.\n\n    No headers parameters except nsweeps, nrays and nbins are not set in the\n    resulting _RslVolume object.\n\n    Parameters\n    ----------\n    arr : array, 2D, float32\n        Two dimensional float32 array.\n    rays_per_sweep: array, 1D, int32\n        Array listing number of rays in each sweep.\n    vol_num : int\n        Volume number used to set f and invf in the header.  The default is\n        for velocity fields.  Useful values are 0 for reflectivity and\n        1 for velocity.\n\n    Returns\n    -------\n    volumes : _RslVolume\n        _RslVolume containing array data.\n\n    '
    pass

datetime = _mod_datetime.datetime
timedelta = _mod_datetime.timedelta
