import builtins as _mod_builtins

__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '\nUtility functions for finding peaks in signals.\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/scipy/signal/_peak_finding_utils.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.signal._peak_finding_utils'
__package__ = 'scipy.signal'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _argmaxima1d():
    '\n    Find indices of local maxima in a 1D array.\n\n    This function finds all local maxima in a 1D array and returns their\n    indices. For maxima who are wider than one sample the index of the center\n    sample is returned (rounded down in case the number of samples is even).\n\n    Parameters\n    ----------\n    x : ndarray\n        The array to search for local maxima.\n\n    Returns\n    -------\n    maxima : ndarray\n        Indices of local maxima in `x`.\n\n    See Also\n    --------\n    argrelmax\n\n    Notes\n    -----\n    - Compared to `argrelmax` this function is significantly faster and can\n      detect maxima that are more than one sample wide. However this comes at\n      the cost of being only applicable to 1D arrays.\n    - A maxima is defined as one or more samples of equal value that are\n      surrounded on both sides by atleast one smaller sample.\n\n    .. versionadded:: 1.1.0\n    '
    pass

def _peak_prominences():
    "\n    Calculate the prominence of each peak in a signal.\n\n    Parameters\n    ----------\n    x : ndarray\n        A signal with peaks.\n    peaks : ndarray\n        Indices of peaks in `x`.\n    wlen : np.intp\n        A window length in samples (see `peak_prominences`) which is rounded up\n        to the nearest odd integer. If smaller than 2 the entire signal `x` is\n        used.\n\n    Returns\n    -------\n    prominences : ndarray\n        The calculated prominences for each peak in `peaks`.\n    left_bases, right_bases : ndarray\n        The peaks' bases as indices in `x` to the left and right of each peak.\n\n    Raises\n    ------\n    ValueError\n        If an index in `peaks` doesn't point to a local maximum in `x`.\n\n    Notes\n    -----\n    This is the inner function to `peak_prominences`.\n\n    .. versionadded:: 1.1.0\n    "
    pass

def _peak_widths():
    "\n    Calculate the width of each each peak in a signal.\n\n    Parameters\n    ----------\n    x : ndarray\n        A signal with peaks.\n    peaks : ndarray\n        Indices of peaks in `x`.\n    rel_height : np.float64\n        Chooses the relative height at which the peak width is measured as a\n        percentage of its prominence (see `peak_widths`).\n    prominences : ndarray\n        Prominences of each peak in `peaks` as returned by `peak_prominences`.\n    left_bases, right_bases : ndarray\n        Left and right bases of each peak in `peaks` as returned by\n        `peak_prominences`.\n\n    Returns\n    -------\n    widths : ndarray\n        The widths for each peak in samples.\n    width_heights : ndarray\n        The height of the contour lines at which the `widths` where evaluated.\n    left_ips, right_ips : ndarray\n        Interpolated positions of left and right intersection points of a\n        horizontal line at the respective evaluation height.\n\n    Raises\n    ------\n    ValueError\n        If the supplied prominence data doesn't satisfy the condition\n        ``0 <= left_base <= peak <= right_base < x.shape[0]`` for each peak or\n        if `peaks`, `left_bases` and `right_bases` don't share the same shape.\n\n    Notes\n    -----\n    This is the inner function to `peak_widths`.\n\n    .. versionadded:: 1.1.0\n    "
    pass

def _select_by_peak_distance():
    "\n    Evaluate which peaks fulfill the distance condition.\n\n    Parameters\n    ----------\n    peaks : ndarray\n        Indices of peaks in `vector`.\n    priority : ndarray\n        An array matching `peaks` used to determine priority of each peak. A\n        peak with a higher priority value is kept over one with a lower one.\n    distance : np.float64\n        Minimal distance that peaks must be spaced.\n\n    Returns\n    -------\n    keep : ndarray[bool]\n        A boolean mask evaluating to true where `peaks` fulfill the distance\n        condition.\n\n    Notes\n    -----\n    Declaring the input arrays as C-contiguous doesn't seem to have performance\n    advantages.\n\n    .. versionadded:: 1.1.0\n    "
    pass

