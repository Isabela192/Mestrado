
## You are using the Python ARM Radar Toolkit (Py-ART), an open source
## library for working with weather radar data. Py-ART is partly
## supported by the U.S. Department of Energy as part of the Atmospheric
## Radiation Measurement (ARM) Climate Research Facility, an Office of
## Science user facility.
##
## If you use this software to prepare a publication, please cite:
##
##     JJ Helmus and SM Collis, JORS 2016, doi: 10.5334/jors.119

__doc__ = "This module '_echo_steiner' is auto-generated with f2py (version:2).\nFunctions:\n  conv_rad = convective_radius(ze_bkg,area_relation)\n  peak = peakedness(ze_bkg,peak_relation)\n  sclass = classify(ze,x,y,z,dx,dy,intense,bkg_rad,work_level,area_relation,peak_relation,use_intense,fill_value,nx=shape(ze,2),ny=shape(ze,1),nz=shape(ze,0))\n."
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/pyart/retrieve/_echo_steiner.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pyart.retrieve._echo_steiner'
__package__ = 'pyart.retrieve'
__version__ = b'$Revision: $'
def classify():
    "sclass = classify(ze,x,y,z,dx,dy,intense,bkg_rad,work_level,area_relation,peak_relation,use_intense,fill_value,[nx,ny,nz])\n\nWrapper for ``classify``.\n\nParameters\n----------\nze : input rank-3 array('d') with bounds (nz,ny,nx)\nx : input rank-1 array('d') with bounds (nx)\ny : input rank-1 array('d') with bounds (ny)\nz : input rank-1 array('d') with bounds (nz)\ndx : input float\ndy : input float\nintense : input float\nbkg_rad : input float\nwork_level : input float\narea_relation : input string(len=16)\npeak_relation : input string(len=16)\nuse_intense : input int\nfill_value : input float\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(ze,2)\nny : input int, optional\n    Default: shape(ze,1)\nnz : input int, optional\n    Default: shape(ze,0)\n\nReturns\n-------\nsclass : rank-2 array('i') with bounds (ny,nx)\n"
    pass

def convective_radius():
    'conv_rad = convective_radius(ze_bkg,area_relation)\n\nWrapper for ``convective_radius``.\n\nParameters\n----------\nze_bkg : input float\narea_relation : input string(len=16)\n\nReturns\n-------\nconv_rad : float\n'
    pass

def peakedness():
    'peak = peakedness(ze_bkg,peak_relation)\n\nWrapper for ``peakedness``.\n\nParameters\n----------\nze_bkg : input float\npeak_relation : input string(len=16)\n\nReturns\n-------\npeak : float\n'
    pass

