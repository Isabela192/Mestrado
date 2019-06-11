
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

__builtins__ = {}
__doc__ = '\npyart.retrieve._kdp_proc\n========================\n\nCython routines for specific differential phase retrievals.\n\n.. autosummary::\n    :toctree: generated/\n\n    lowpass_maesaka_term\n    lowpass_maesaka_jac\n\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pyart/retrieve/_kdp_proc.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pyart.retrieve._kdp_proc'
__package__ = 'pyart.retrieve'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def lowpass_maesaka_jac():
    "\n    Compute the Jacobian of the filter cost functional.\n\n    Compute the Jacobian of the low-pass filter cost functional similar to\n    equation (18) in Maesaka et al. (2012). This function does not currently\n    support radars with variable range resolution.\n\n    Parameters\n    ----------\n    d2kdr2 : 2D array of float64\n       Second-order derivative of the control variable k with respect to range.\n       The control variable k is proportional to the square root of specific\n       differential phase.\n    dr : float\n       The range resolution in meters.\n    Clpf : float\n       The low-pass filter (radial smoothness) constraint weight.\n    finite_order :  str, 'low' or 'high'\n       The finite difference accuracy used to compute the second-order range\n       derivative of the control variable k.\n    dJlpfdk : 2D array of float64\n       The Jacobian of the low-pass filter cost functional with respect to the\n       control variable k.  Updated in place.\n\n    "
    pass

def lowpass_maesaka_term():
    "\n    Compute the filter term.\n\n    Compute the low-pass filter term found in Maesaka et al. (2012). This term\n    represents the second-order derivative of the control variable k with\n    respect to range. This subroutine does not currently support radars with\n    variable range resolution.\n\n    Parameters\n    ----------\n    k : 2D array of float64\n        Control variable k defined in Maesaka et al. (2012). This variable is\n        proportional to the square root of specific differential phase.\n    dr : float\n        The range resolution in meters.\n    finite_order : str, 'low' or 'high'\n        The finite difference accuracy to use when computing the second-order\n        range derivative of the control variable k.\n    d2kdr2 : 2D array of float64\n        Second-order derivative of k with respect to range. Updated in place.\n\n    "
    pass

