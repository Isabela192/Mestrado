__doc__ = "This module '_slsqp' is auto-generated with f2py (version:2).\nFunctions:\n  slsqp(m,meq,x,xl,xu,f,c,g,a,acc,iter,mode,w,jw,la=len(c),n=len(x),l_w=len(w),l_jw=len(jw))\n."
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/scipy/optimize/_slsqp.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.optimize._slsqp'
__package__ = 'scipy.optimize'
__version__ = b'$Revision: $'
def slsqp(m, meq, x, xl, xu, f, c, g, a, acc, iter, mode, w, jw, la=None, n=None, l_w=None, l_jw=None):
    "slsqp(m,meq,x,xl,xu,f,c,g,a,acc,iter,mode,w,jw,[la,n,l_w,l_jw])\n\nWrapper for ``slsqp``.\n\nParameters\n----------\nm : input int\nmeq : input int\nx : in/output rank-1 array('d') with bounds (n)\nxl : input rank-1 array('d') with bounds (n)\nxu : input rank-1 array('d') with bounds (n)\nf : input float\nc : input rank-1 array('d') with bounds (la)\ng : input rank-1 array('d') with bounds (n + 1)\na : input rank-2 array('d') with bounds (la,n + 1)\nacc : in/output rank-0 array(float,'d')\niter : in/output rank-0 array(int,'i')\nmode : in/output rank-0 array(int,'i')\nw : input rank-1 array('d') with bounds (l_w)\njw : input rank-1 array('i') with bounds (l_jw)\n\nOther Parameters\n----------------\nla : input int, optional\n    Default: len(c)\nn : input int, optional\n    Default: len(x)\nl_w : input int, optional\n    Default: len(w)\nl_jw : input int, optional\n    Default: len(jw)\n"
    pass

