__doc__ = "This module '_wrffortran' is auto-generated with f2py (version:2).\nFunctions:\n  b = testfunc(a,b,c,errstat,errmsg,nx=shape(a,0),ny=shape(a,1),nz=shape(a,2))\n  pi = dcomputepi(pi,pressure,nx=shape(pi,0),ny=shape(pi,1),nz=shape(pi,2))\n  tk = dcomputetk(tk,pressure,theta,nx=len(tk))\n  out2d = dinterp3dz(data3d,out2d,zdata,levels,missingval,nx=shape(data3d,0),ny=shape(data3d,1),nz=shape(data3d,2),nlev=shape(out2d,2))\n  out2d = dinterp3dz_2dlev(data3d,out2d,zdata,levs2d,missingval,nx=shape(data3d,0),ny=shape(data3d,1),nz=shape(data3d,2))\n  znew = dzstag(znew,z,terrain,nx=shape(znew,0),ny=shape(znew,1),nz=shape(znew,2),nxz=shape(z,0),nyz=shape(z,1),nzz=shape(z,2))\n  v2d = dinterp2dxy(v3d,v2d,xy,nx=shape(v3d,0),ny=shape(v3d,1),nz=shape(v3d,2),nxy=shape(v2d,0))\n  v_out = dinterp1d(v_in,v_out,z_in,z_out,vmsg,nz_in=len(v_in),nz_out=len(v_out))\n  sea_level_pressure = dcomputeseaprs(z,t,p,q,sea_level_pressure,t_sea_level,t_surf,level,errstat,errmsg,nx=shape(z,0),ny=shape(z,1),nz=shape(z,2))\n  a = dfilter2d(a,b,it,missing,cenweight,nx=shape(a,0),ny=shape(a,1))\n  a = filter2d(a,b,it,missing,cenweight,nx=shape(a,0),ny=shape(a,1))\n  rh = dcomputerh(qv,p,t,rh,nx=len(qv))\n  ii,jj = dgetijlatlong(lat_array,long_array,lat,longitude,ii,jj,imsg,nx=shape(lat_array,0),ny=shape(lat_array,1))\n  uvmet = dcomputeuvmet(u,v,uvmet,longca,longcb,flong,flat,cen_long,cone,rpd,istag,is_msg_val,umsg,vmsg,uvmetmsg,nx=shape(v,0),ny=shape(u,1),nxp1=shape(u,0),nyp1=shape(v,1))\n  td = dcomputetd(td,pressure,qv_in,nx=len(td))\n  iclw = dcomputeiclw(iclw,pressure,qc_in,nx=shape(iclw,0),ny=shape(iclw,1),nz=shape(pressure,2))\n  tvirtual = tvirtual(temp,ratmix)\n  tonpsadiabat = tonpsadiabat(thte,prs,psadithte,psadiprs,psaditmk,gamma,errstat,errmsg)\n  dlookup_table(psadithte,psadiprs,psaditmk,fname,errstat,errmsg)\n  pf = dpfcalc(prs,sfp,ter_follow,mix=shape(prs,1),mjy=shape(prs,2),mkzh=shape(prs,0))\n  cape,cin = dcapecalc3d(prs,tmk,qvp,ght,ter,sfp,cape,cin,prsf,prs_new,tmk_new,qvp_new,ght_new,cmsg,ter_follow,psafile,errstat,errmsg,mix=shape(prs,0),mjy=shape(prs,1),mkzh=shape(prs,2))\n  cape,cin = dcapecalc2d(prs,tmk,qvp,ght,ter,sfp,cape,cin,prsf,prs_new,tmk_new,qvp_new,ght_new,cmsg,ter_follow,psafile,errstat,errmsg,mix=shape(prs,0),mjy=shape(prs,1),mkzh=shape(prs,2))\n  lowc,midc,highc = dcloudfrac(pres,rh,lowc,midc,highc,nz=shape(pres,2),ns=shape(pres,1),ew=shape(pres,0))\n  lowc,midc,highc = dcloudfrac2(vert,rh,vert_inc_w_height,low_thresh,mid_thresh,high_thresh,msg,lowc,midc,highc,nz=shape(vert,2),ns=shape(vert,1),ew=shape(vert,0))\n  ctt = wrfcttcalc(prs,tk,qci,qcw,qvp,ght,ter,ctt,pf,haveqci,fill_nocloud,missing,opt_thresh,nz=shape(prs,2),ns=shape(prs,1),ew=shape(prs,0))\n  dbz = calcdbz(prs,tmk,qvp,qra,qsn,qgr,sn0,ivarint,iliqskin,dbz,nx=shape(prs,0),ny=shape(prs,1),nz=shape(prs,2))\n  sreh = dcalrelhl(u,v,ght,ter,lat,top,sreh,miy=shape(u,0),mjx=shape(u,1),mkzh=shape(u,2))\n  uh = dcalcuh(zp,mapfct,dx,dy,uhmnhgt,uhmxhgt,us,vs,w,uh,tem1,tem2,nx=shape(zp,0),ny=shape(zp,1),nz=shape(us,2),nzp1=shape(zp,2))\n  olat,olon = rotatecoords(ilat,ilon,olat,olon,lat_np,lon_np,lon_0,direction)\n  loc = dlltoij(map_proj,truelat1,truelat2,stdlon,lat1,lon1,pole_lat,pole_lon,knowni,knownj,dx,dy,latinc,loninc,lat,lon,loc,errstat,errmsg)\n  loc = dijtoll(map_proj,truelat1,truelat2,stdlon,lat1,lon1,pole_lat,pole_lon,knowni,knownj,dx,dy,latinc,loninc,ai,aj,loc,errstat,errmsg)\n  av = dcomputeabsvort(av,u,v,msfu,msfv,msft,cor,dx,dy,nx=shape(av,0),ny=shape(av,1),nz=shape(av,2),nxp1=shape(u,0),nyp1=shape(v,1))\n  pv = dcomputepv(pv,u,v,theta,prs,msfu,msfv,msft,cor,dx,dy,nx=shape(pv,0),ny=shape(pv,1),nz=shape(pv,2),nxp1=shape(u,0),nyp1=shape(v,1))\n  eth = deqthecalc(qvp,tmk,prs,eth,miy=shape(qvp,0),mjx=shape(qvp,1),mkzh=shape(qvp,2))\n  twb = wetbulbcalc(prs,tmk,qvp,twb,psafile,errstat,errmsg,nx=shape(prs,0),ny=shape(prs,1),nz=shape(prs,2))\n  omg = omgcalc(qvp,tmk,www,prs,omg,mx=shape(qvp,0),my=shape(qvp,1),mz=shape(qvp,2))\n  tv = virtual_temp(temp,ratmix,tv,nx=shape(temp,0),ny=shape(temp,1),nz=shape(temp,2))\n  pw = dcomputepw(p,tv,qv,ht,pw,nx=shape(p,0),ny=shape(p,1),nz=shape(p,2),nzh=shape(ht,2))\n  out = wrf_monotonic(out,in,lvprs,cor,idir,delta,icorsw,ew=shape(out,0),ns=shape(out,1),nz=shape(out,2))\n  wrf_intrp_value = wrf_intrp_value(wvalp0,wvalp1,vlev,vcp0,vcp1,icase,errstat)\n  dataout = wrf_vintrp(datain,dataout,pres,tk,qvp,ght,terrain,sfp,smsfp,vcarray,interp_levels,icase,extrap,vcor,logp,tempout,rmsg,errstat,errmsg,numlevels=shape(dataout,2),ew=shape(datain,0),ns=shape(datain,1),nz=shape(datain,2))\n  wspd = dcomputewspd(wspd,u,v,n=len(wspd))\n  wdir = dcomputewdir(wdir,u,v,n=len(wdir))\n  fomp_enabled = fomp_enabled()\n  fomp_set_num_threads(num_threads)\n  fomp_get_num_threads = fomp_get_num_threads()\n  fomp_get_max_threads = fomp_get_max_threads()\n  fomp_get_thread_num = fomp_get_thread_num()\n  fomp_get_num_procs = fomp_get_num_procs()\n  fomp_in_parallel = fomp_in_parallel()\n  fomp_set_dynamic(dynamic_threads)\n  fomp_get_dynamic = fomp_get_dynamic()\n  fomp_set_nested(nested)\n  fomp_get_nested = fomp_get_nested()\n  fomp_set_schedule(kind,modifier)\n  kind,modifier = fomp_get_schedule()\n  fomp_get_thread_limit = fomp_get_thread_limit()\n  fomp_set_max_active_levels(max_levels)\n  fomp_get_max_active_levels = fomp_get_max_active_levels()\n  fomp_get_level = fomp_get_level()\n  fomp_get_ancestor_thread_num = fomp_get_ancestor_thread_num(level)\n  fomp_get_team_size = fomp_get_team_size(level)\n  fomp_get_active_level = fomp_get_active_level()\n  fomp_in_final = fomp_in_final()\n  svar = fomp_init_lock()\n  nvar = fomp_init_nest_lock()\n  fomp_destroy_lock(svar)\n  fomp_destroy_nest_lock(nvar)\n  fomp_set_lock(svar)\n  fomp_set_nest_lock(nvar)\n  fomp_unset_lock(svar)\n  fomp_unset_nest_lock(nvar)\n  fomp_test_lock = fomp_test_lock(svar)\n  fomp_test_nest_lock = fomp_test_nest_lock(nvar)\n  fomp_get_wtime = fomp_get_wtime()\n  fomp_get_wtick = fomp_get_wtick()\nFortran 90/95 modules:\n  wrf_constants --- errlen,algerr,wrf_earth_radius,t_base,pi,rad_per_deg,deg_per_rad,default_fill,default_fill_int8,default_fill_int16,default_fill_int32,default_fill_int64,default_fill_float,default_fill_double,default_fill_char,p1000mb,rd,rv,cp,g,ussalr,celkel,celkel_triple,ezero,eslcon1,eslcon2,eps,gamma,cpmd,rgasmd,gammamd,tlclc1,tlclc2,tlclc3,tlclc4,thtecon1,thtecon2,thtecon3,abscoefi,abscoef,gamma_seven,rhowat,rho_r,rho_s,rho_g,alpha,sclht,expon,exponi  omp_constants --- fomp_sched_kind,fomp_lock_kind,fomp_nest_lock_kind,fomp_sched_static,fomp_sched_dynamic,fomp_sched_guided,fomp_sched_auto."
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/wrf/_wrffortran.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'wrf._wrffortran'
__package__ = 'wrf'
__version__ = b'$Revision: $'
def calcdbz():
    "dbz = calcdbz(prs,tmk,qvp,qra,qsn,qgr,sn0,ivarint,iliqskin,dbz,[nx,ny,nz])\n\nWrapper for ``calcdbz``.\n\nParameters\n----------\nprs : input rank-3 array('d') with bounds (nx,ny,nz)\ntmk : input rank-3 array('d') with bounds (nx,ny,nz)\nqvp : in/output rank-3 array('d') with bounds (nx,ny,nz)\nqra : in/output rank-3 array('d') with bounds (nx,ny,nz)\nqsn : in/output rank-3 array('d') with bounds (nx,ny,nz)\nqgr : in/output rank-3 array('d') with bounds (nx,ny,nz)\nsn0 : input int\nivarint : input int\niliqskin : input int\ndbz : input rank-3 array('d') with bounds (nx,ny,nz)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(prs,0)\nny : input int, optional\n    Default: shape(prs,1)\nnz : input int, optional\n    Default: shape(prs,2)\n\nReturns\n-------\ndbz : rank-3 array('d') with bounds (nx,ny,nz)\n"
    pass

def dcalcuh():
    "uh = dcalcuh(zp,mapfct,dx,dy,uhmnhgt,uhmxhgt,us,vs,w,uh,tem1,tem2,[nx,ny,nz,nzp1])\n\nWrapper for ``dcalcuh``.\n\nParameters\n----------\nzp : input rank-3 array('d') with bounds (nx,ny,nzp1)\nmapfct : input rank-2 array('d') with bounds (nx,ny)\ndx : input float\ndy : input float\nuhmnhgt : input float\nuhmxhgt : input float\nus : input rank-3 array('d') with bounds (nx,ny,nz)\nvs : input rank-3 array('d') with bounds (nx,ny,nz)\nw : input rank-3 array('d') with bounds (nx,ny,nzp1)\nuh : input rank-2 array('d') with bounds (nx,ny)\ntem1 : in/output rank-3 array('d') with bounds (nx,ny,nz)\ntem2 : in/output rank-3 array('d') with bounds (nx,ny,nz)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(zp,0)\nny : input int, optional\n    Default: shape(zp,1)\nnz : input int, optional\n    Default: shape(us,2)\nnzp1 : input int, optional\n    Default: shape(zp,2)\n\nReturns\n-------\nuh : rank-2 array('d') with bounds (nx,ny)\n"
    pass

def dcalrelhl():
    "sreh = dcalrelhl(u,v,ght,ter,lat,top,sreh,[miy,mjx,mkzh])\n\nWrapper for ``dcalrelhl``.\n\nParameters\n----------\nu : input rank-3 array('d') with bounds (miy,mjx,mkzh)\nv : input rank-3 array('d') with bounds (miy,mjx,mkzh)\nght : input rank-3 array('d') with bounds (miy,mjx,mkzh)\nter : input rank-2 array('d') with bounds (miy,mjx)\nlat : input rank-2 array('d') with bounds (miy,mjx)\ntop : input float\nsreh : input rank-2 array('d') with bounds (miy,mjx)\n\nOther Parameters\n----------------\nmiy : input int, optional\n    Default: shape(u,0)\nmjx : input int, optional\n    Default: shape(u,1)\nmkzh : input int, optional\n    Default: shape(u,2)\n\nReturns\n-------\nsreh : rank-2 array('d') with bounds (miy,mjx)\n"
    pass

def dcapecalc2d():
    "cape,cin = dcapecalc2d(prs,tmk,qvp,ght,ter,sfp,cape,cin,prsf,prs_new,tmk_new,qvp_new,ght_new,cmsg,ter_follow,psafile,errstat,errmsg,[mix,mjy,mkzh])\n\nWrapper for ``dcapecalc2d``.\n\nParameters\n----------\nprs : input rank-3 array('d') with bounds (mix,mjy,mkzh)\ntmk : input rank-3 array('d') with bounds (mix,mjy,mkzh)\nqvp : input rank-3 array('d') with bounds (mix,mjy,mkzh)\nght : input rank-3 array('d') with bounds (mix,mjy,mkzh)\nter : input rank-2 array('d') with bounds (mix,mjy)\nsfp : input rank-2 array('d') with bounds (mix,mjy)\ncape : input rank-3 array('d') with bounds (mix,mjy,mkzh)\ncin : input rank-3 array('d') with bounds (mix,mjy,mkzh)\nprsf : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\nprs_new : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\ntmk_new : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\nqvp_new : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\nght_new : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\ncmsg : input float\nter_follow : input int\npsafile : input string(len=-1)\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nOther Parameters\n----------------\nmix : input int, optional\n    Default: shape(prs,0)\nmjy : input int, optional\n    Default: shape(prs,1)\nmkzh : input int, optional\n    Default: shape(prs,2)\n\nReturns\n-------\ncape : rank-3 array('d') with bounds (mix,mjy,mkzh)\ncin : rank-3 array('d') with bounds (mix,mjy,mkzh)\n"
    pass

def dcapecalc3d():
    "cape,cin = dcapecalc3d(prs,tmk,qvp,ght,ter,sfp,cape,cin,prsf,prs_new,tmk_new,qvp_new,ght_new,cmsg,ter_follow,psafile,errstat,errmsg,[mix,mjy,mkzh])\n\nWrapper for ``dcapecalc3d``.\n\nParameters\n----------\nprs : input rank-3 array('d') with bounds (mix,mjy,mkzh)\ntmk : input rank-3 array('d') with bounds (mix,mjy,mkzh)\nqvp : input rank-3 array('d') with bounds (mix,mjy,mkzh)\nght : input rank-3 array('d') with bounds (mix,mjy,mkzh)\nter : input rank-2 array('d') with bounds (mix,mjy)\nsfp : input rank-2 array('d') with bounds (mix,mjy)\ncape : input rank-3 array('d') with bounds (mix,mjy,mkzh)\ncin : input rank-3 array('d') with bounds (mix,mjy,mkzh)\nprsf : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\nprs_new : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\ntmk_new : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\nqvp_new : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\nght_new : in/output rank-3 array('d') with bounds (mkzh,mix,mjy)\ncmsg : input float\nter_follow : input int\npsafile : input string(len=-1)\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nOther Parameters\n----------------\nmix : input int, optional\n    Default: shape(prs,0)\nmjy : input int, optional\n    Default: shape(prs,1)\nmkzh : input int, optional\n    Default: shape(prs,2)\n\nReturns\n-------\ncape : rank-3 array('d') with bounds (mix,mjy,mkzh)\ncin : rank-3 array('d') with bounds (mix,mjy,mkzh)\n"
    pass

def dcloudfrac():
    "lowc,midc,highc = dcloudfrac(pres,rh,lowc,midc,highc,[nz,ns,ew])\n\nWrapper for ``dcloudfrac``.\n\nParameters\n----------\npres : input rank-3 array('d') with bounds (ew,ns,nz)\nrh : input rank-3 array('d') with bounds (ew,ns,nz)\nlowc : input rank-2 array('d') with bounds (ew,ns)\nmidc : input rank-2 array('d') with bounds (ew,ns)\nhighc : input rank-2 array('d') with bounds (ew,ns)\n\nOther Parameters\n----------------\nnz : input int, optional\n    Default: shape(pres,2)\nns : input int, optional\n    Default: shape(pres,1)\new : input int, optional\n    Default: shape(pres,0)\n\nReturns\n-------\nlowc : rank-2 array('d') with bounds (ew,ns)\nmidc : rank-2 array('d') with bounds (ew,ns)\nhighc : rank-2 array('d') with bounds (ew,ns)\n"
    pass

def dcloudfrac2():
    "lowc,midc,highc = dcloudfrac2(vert,rh,vert_inc_w_height,low_thresh,mid_thresh,high_thresh,msg,lowc,midc,highc,[nz,ns,ew])\n\nWrapper for ``dcloudfrac2``.\n\nParameters\n----------\nvert : input rank-3 array('d') with bounds (ew,ns,nz)\nrh : input rank-3 array('d') with bounds (ew,ns,nz)\nvert_inc_w_height : input int\nlow_thresh : input float\nmid_thresh : input float\nhigh_thresh : input float\nmsg : input float\nlowc : input rank-2 array('d') with bounds (ew,ns)\nmidc : input rank-2 array('d') with bounds (ew,ns)\nhighc : input rank-2 array('d') with bounds (ew,ns)\n\nOther Parameters\n----------------\nnz : input int, optional\n    Default: shape(vert,2)\nns : input int, optional\n    Default: shape(vert,1)\new : input int, optional\n    Default: shape(vert,0)\n\nReturns\n-------\nlowc : rank-2 array('d') with bounds (ew,ns)\nmidc : rank-2 array('d') with bounds (ew,ns)\nhighc : rank-2 array('d') with bounds (ew,ns)\n"
    pass

def dcomputeabsvort():
    "av = dcomputeabsvort(av,u,v,msfu,msfv,msft,cor,dx,dy,[nx,ny,nz,nxp1,nyp1])\n\nWrapper for ``dcomputeabsvort``.\n\nParameters\n----------\nav : input rank-3 array('d') with bounds (nx,ny,nz)\nu : input rank-3 array('d') with bounds (nxp1,ny,nz)\nv : input rank-3 array('d') with bounds (nx,nyp1,nz)\nmsfu : input rank-2 array('d') with bounds (nxp1,ny)\nmsfv : input rank-2 array('d') with bounds (nx,nyp1)\nmsft : input rank-2 array('d') with bounds (nx,ny)\ncor : input rank-2 array('d') with bounds (nx,ny)\ndx : input float\ndy : input float\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(av,0)\nny : input int, optional\n    Default: shape(av,1)\nnz : input int, optional\n    Default: shape(av,2)\nnxp1 : input int, optional\n    Default: shape(u,0)\nnyp1 : input int, optional\n    Default: shape(v,1)\n\nReturns\n-------\nav : rank-3 array('d') with bounds (nx,ny,nz)\n"
    pass

def dcomputeiclw():
    "iclw = dcomputeiclw(iclw,pressure,qc_in,[nx,ny,nz])\n\nWrapper for ``dcomputeiclw``.\n\nParameters\n----------\niclw : input rank-2 array('d') with bounds (nx,ny)\npressure : input rank-3 array('d') with bounds (nx,ny,nz)\nqc_in : input rank-3 array('d') with bounds (nx,ny,nz)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(iclw,0)\nny : input int, optional\n    Default: shape(iclw,1)\nnz : input int, optional\n    Default: shape(pressure,2)\n\nReturns\n-------\niclw : rank-2 array('d') with bounds (nx,ny)\n"
    pass

def dcomputepi():
    "pi = dcomputepi(pi,pressure,[nx,ny,nz])\n\nWrapper for ``dcomputepi``.\n\nParameters\n----------\npi : input rank-3 array('d') with bounds (nx,ny,nz)\npressure : input rank-3 array('d') with bounds (nx,ny,nz)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(pi,0)\nny : input int, optional\n    Default: shape(pi,1)\nnz : input int, optional\n    Default: shape(pi,2)\n\nReturns\n-------\npi : rank-3 array('d') with bounds (nx,ny,nz)\n"
    pass

def dcomputepv():
    "pv = dcomputepv(pv,u,v,theta,prs,msfu,msfv,msft,cor,dx,dy,[nx,ny,nz,nxp1,nyp1])\n\nWrapper for ``dcomputepv``.\n\nParameters\n----------\npv : input rank-3 array('d') with bounds (nx,ny,nz)\nu : input rank-3 array('d') with bounds (nxp1,ny,nz)\nv : input rank-3 array('d') with bounds (nx,nyp1,nz)\ntheta : input rank-3 array('d') with bounds (nx,ny,nz)\nprs : input rank-3 array('d') with bounds (nx,ny,nz)\nmsfu : input rank-2 array('d') with bounds (nxp1,ny)\nmsfv : input rank-2 array('d') with bounds (nx,nyp1)\nmsft : input rank-2 array('d') with bounds (nx,ny)\ncor : input rank-2 array('d') with bounds (nx,ny)\ndx : input float\ndy : input float\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(pv,0)\nny : input int, optional\n    Default: shape(pv,1)\nnz : input int, optional\n    Default: shape(pv,2)\nnxp1 : input int, optional\n    Default: shape(u,0)\nnyp1 : input int, optional\n    Default: shape(v,1)\n\nReturns\n-------\npv : rank-3 array('d') with bounds (nx,ny,nz)\n"
    pass

def dcomputepw():
    "pw = dcomputepw(p,tv,qv,ht,pw,[nx,ny,nz,nzh])\n\nWrapper for ``dcomputepw``.\n\nParameters\n----------\np : input rank-3 array('d') with bounds (nx,ny,nz)\ntv : input rank-3 array('d') with bounds (nx,ny,nz)\nqv : input rank-3 array('d') with bounds (nx,ny,nz)\nht : input rank-3 array('d') with bounds (nx,ny,nzh)\npw : input rank-2 array('d') with bounds (nx,ny)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(p,0)\nny : input int, optional\n    Default: shape(p,1)\nnz : input int, optional\n    Default: shape(p,2)\nnzh : input int, optional\n    Default: shape(ht,2)\n\nReturns\n-------\npw : rank-2 array('d') with bounds (nx,ny)\n"
    pass

def dcomputerh():
    "rh = dcomputerh(qv,p,t,rh,[nx])\n\nWrapper for ``dcomputerh``.\n\nParameters\n----------\nqv : input rank-1 array('d') with bounds (nx)\np : input rank-1 array('d') with bounds (nx)\nt : input rank-1 array('d') with bounds (nx)\nrh : input rank-1 array('d') with bounds (nx)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: len(qv)\n\nReturns\n-------\nrh : rank-1 array('d') with bounds (nx)\n"
    pass

def dcomputeseaprs():
    "sea_level_pressure = dcomputeseaprs(z,t,p,q,sea_level_pressure,t_sea_level,t_surf,level,errstat,errmsg,[nx,ny,nz])\n\nWrapper for ``dcomputeseaprs``.\n\nParameters\n----------\nz : input rank-3 array('d') with bounds (nx,ny,nz)\nt : input rank-3 array('d') with bounds (nx,ny,nz)\np : input rank-3 array('d') with bounds (nx,ny,nz)\nq : input rank-3 array('d') with bounds (nx,ny,nz)\nsea_level_pressure : input rank-2 array('d') with bounds (nx,ny)\nt_sea_level : in/output rank-2 array('d') with bounds (nx,ny)\nt_surf : in/output rank-2 array('d') with bounds (nx,ny)\nlevel : in/output rank-2 array('i') with bounds (nx,ny)\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(z,0)\nny : input int, optional\n    Default: shape(z,1)\nnz : input int, optional\n    Default: shape(z,2)\n\nReturns\n-------\nsea_level_pressure : rank-2 array('d') with bounds (nx,ny)\n"
    pass

def dcomputetd():
    "td = dcomputetd(td,pressure,qv_in,[nx])\n\nWrapper for ``dcomputetd``.\n\nParameters\n----------\ntd : input rank-1 array('d') with bounds (nx)\npressure : input rank-1 array('d') with bounds (nx)\nqv_in : input rank-1 array('d') with bounds (nx)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: len(td)\n\nReturns\n-------\ntd : rank-1 array('d') with bounds (nx)\n"
    pass

def dcomputetk():
    "tk = dcomputetk(tk,pressure,theta,[nx])\n\nWrapper for ``dcomputetk``.\n\nParameters\n----------\ntk : input rank-1 array('d') with bounds (nx)\npressure : input rank-1 array('d') with bounds (nx)\ntheta : input rank-1 array('d') with bounds (nx)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: len(tk)\n\nReturns\n-------\ntk : rank-1 array('d') with bounds (nx)\n"
    pass

def dcomputeuvmet():
    "uvmet = dcomputeuvmet(u,v,uvmet,longca,longcb,flong,flat,cen_long,cone,rpd,istag,is_msg_val,umsg,vmsg,uvmetmsg,[nx,ny,nxp1,nyp1])\n\nWrapper for ``dcomputeuvmet``.\n\nParameters\n----------\nu : input rank-2 array('d') with bounds (nxp1,ny)\nv : input rank-2 array('d') with bounds (nx,nyp1)\nuvmet : input rank-3 array('d') with bounds (nx,ny,2)\nlongca : in/output rank-2 array('d') with bounds (nx,ny)\nlongcb : in/output rank-2 array('d') with bounds (nx,ny)\nflong : input rank-2 array('d') with bounds (nx,ny)\nflat : input rank-2 array('d') with bounds (nx,ny)\ncen_long : input float\ncone : input float\nrpd : input float\nistag : input int\nis_msg_val : input int\numsg : input float\nvmsg : input float\nuvmetmsg : input float\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(v,0)\nny : input int, optional\n    Default: shape(u,1)\nnxp1 : input int, optional\n    Default: shape(u,0)\nnyp1 : input int, optional\n    Default: shape(v,1)\n\nReturns\n-------\nuvmet : rank-3 array('d') with bounds (nx,ny,2)\n"
    pass

def dcomputewdir():
    "wdir = dcomputewdir(wdir,u,v,[n])\n\nWrapper for ``dcomputewdir``.\n\nParameters\n----------\nwdir : input rank-1 array('d') with bounds (n)\nu : input rank-1 array('d') with bounds (n)\nv : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(wdir)\n\nReturns\n-------\nwdir : rank-1 array('d') with bounds (n)\n"
    pass

def dcomputewspd():
    "wspd = dcomputewspd(wspd,u,v,[n])\n\nWrapper for ``dcomputewspd``.\n\nParameters\n----------\nwspd : input rank-1 array('d') with bounds (n)\nu : input rank-1 array('d') with bounds (n)\nv : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(wspd)\n\nReturns\n-------\nwspd : rank-1 array('d') with bounds (n)\n"
    pass

def deqthecalc():
    "eth = deqthecalc(qvp,tmk,prs,eth,[miy,mjx,mkzh])\n\nWrapper for ``deqthecalc``.\n\nParameters\n----------\nqvp : input rank-3 array('d') with bounds (miy,mjx,mkzh)\ntmk : input rank-3 array('d') with bounds (miy,mjx,mkzh)\nprs : input rank-3 array('d') with bounds (miy,mjx,mkzh)\neth : input rank-3 array('d') with bounds (miy,mjx,mkzh)\n\nOther Parameters\n----------------\nmiy : input int, optional\n    Default: shape(qvp,0)\nmjx : input int, optional\n    Default: shape(qvp,1)\nmkzh : input int, optional\n    Default: shape(qvp,2)\n\nReturns\n-------\neth : rank-3 array('d') with bounds (miy,mjx,mkzh)\n"
    pass

def dfilter2d():
    "a = dfilter2d(a,b,it,missing,cenweight,[nx,ny])\n\nWrapper for ``dfilter2d``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (nx,ny)\nb : in/output rank-2 array('d') with bounds (nx,ny)\nit : input int\nmissing : input float\ncenweight : input float\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(a,0)\nny : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\na : rank-2 array('d') with bounds (nx,ny)\n"
    pass

def dgetijlatlong():
    "ii,jj = dgetijlatlong(lat_array,long_array,lat,longitude,ii,jj,imsg,[nx,ny])\n\nWrapper for ``dgetijlatlong``.\n\nParameters\n----------\nlat_array : input rank-2 array('d') with bounds (nx,ny)\nlong_array : input rank-2 array('d') with bounds (nx,ny)\nlat : input float\nlongitude : input float\nii : input int\njj : input int\nimsg : input int\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(lat_array,0)\nny : input int, optional\n    Default: shape(lat_array,1)\n\nReturns\n-------\nii : int\njj : int\n"
    pass

def dijtoll():
    "loc = dijtoll(map_proj,truelat1,truelat2,stdlon,lat1,lon1,pole_lat,pole_lon,knowni,knownj,dx,dy,latinc,loninc,ai,aj,loc,errstat,errmsg)\n\nWrapper for ``dijtoll``.\n\nParameters\n----------\nmap_proj : input int\ntruelat1 : in/output rank-0 array(float,'d')\ntruelat2 : in/output rank-0 array(float,'d')\nstdlon : input float\nlat1 : input float\nlon1 : input float\npole_lat : input float\npole_lon : input float\nknowni : input float\nknownj : input float\ndx : input float\ndy : input float\nlatinc : input float\nloninc : input float\nai : input float\naj : input float\nloc : input rank-1 array('d') with bounds (2)\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nReturns\n-------\nloc : rank-1 array('d') with bounds (2)\n"
    pass

def dinterp1d():
    "v_out = dinterp1d(v_in,v_out,z_in,z_out,vmsg,[nz_in,nz_out])\n\nWrapper for ``dinterp1d``.\n\nParameters\n----------\nv_in : input rank-1 array('d') with bounds (nz_in)\nv_out : input rank-1 array('d') with bounds (nz_out)\nz_in : input rank-1 array('d') with bounds (nz_in)\nz_out : input rank-1 array('d') with bounds (nz_out)\nvmsg : input float\n\nOther Parameters\n----------------\nnz_in : input int, optional\n    Default: len(v_in)\nnz_out : input int, optional\n    Default: len(v_out)\n\nReturns\n-------\nv_out : rank-1 array('d') with bounds (nz_out)\n"
    pass

def dinterp2dxy():
    "v2d = dinterp2dxy(v3d,v2d,xy,[nx,ny,nz,nxy])\n\nWrapper for ``dinterp2dxy``.\n\nParameters\n----------\nv3d : input rank-3 array('d') with bounds (nx,ny,nz)\nv2d : input rank-2 array('d') with bounds (nxy,nz)\nxy : input rank-2 array('d') with bounds (2,nxy)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(v3d,0)\nny : input int, optional\n    Default: shape(v3d,1)\nnz : input int, optional\n    Default: shape(v3d,2)\nnxy : input int, optional\n    Default: shape(v2d,0)\n\nReturns\n-------\nv2d : rank-2 array('d') with bounds (nxy,nz)\n"
    pass

def dinterp3dz():
    "out2d = dinterp3dz(data3d,out2d,zdata,levels,missingval,[nx,ny,nz,nlev])\n\nWrapper for ``dinterp3dz``.\n\nParameters\n----------\ndata3d : input rank-3 array('d') with bounds (nx,ny,nz)\nout2d : input rank-3 array('d') with bounds (nx,ny,nlev)\nzdata : input rank-3 array('d') with bounds (nx,ny,nz)\nlevels : input rank-1 array('d') with bounds (nlev)\nmissingval : input float\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(data3d,0)\nny : input int, optional\n    Default: shape(data3d,1)\nnz : input int, optional\n    Default: shape(data3d,2)\nnlev : input int, optional\n    Default: shape(out2d,2)\n\nReturns\n-------\nout2d : rank-3 array('d') with bounds (nx,ny,nlev)\n"
    pass

def dinterp3dz_2dlev():
    "out2d = dinterp3dz_2dlev(data3d,out2d,zdata,levs2d,missingval,[nx,ny,nz])\n\nWrapper for ``dinterp3dz_2dlev``.\n\nParameters\n----------\ndata3d : input rank-3 array('d') with bounds (nx,ny,nz)\nout2d : input rank-2 array('d') with bounds (nx,ny)\nzdata : input rank-3 array('d') with bounds (nx,ny,nz)\nlevs2d : input rank-2 array('d') with bounds (nx,ny)\nmissingval : input float\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(data3d,0)\nny : input int, optional\n    Default: shape(data3d,1)\nnz : input int, optional\n    Default: shape(data3d,2)\n\nReturns\n-------\nout2d : rank-2 array('d') with bounds (nx,ny)\n"
    pass

def dlltoij():
    "loc = dlltoij(map_proj,truelat1,truelat2,stdlon,lat1,lon1,pole_lat,pole_lon,knowni,knownj,dx,dy,latinc,loninc,lat,lon,loc,errstat,errmsg)\n\nWrapper for ``dlltoij``.\n\nParameters\n----------\nmap_proj : input int\ntruelat1 : in/output rank-0 array(float,'d')\ntruelat2 : in/output rank-0 array(float,'d')\nstdlon : input float\nlat1 : input float\nlon1 : input float\npole_lat : input float\npole_lon : input float\nknowni : input float\nknownj : input float\ndx : input float\ndy : input float\nlatinc : input float\nloninc : input float\nlat : in/output rank-0 array(float,'d')\nlon : in/output rank-0 array(float,'d')\nloc : input rank-1 array('d') with bounds (2)\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nReturns\n-------\nloc : rank-1 array('d') with bounds (2)\n"
    pass

def dlookup_table(psadithte, psadiprs, psaditmk, fname, errstat, errmsg):
    "dlookup_table(psadithte,psadiprs,psaditmk,fname,errstat,errmsg)\n\nWrapper for ``dlookup_table``.\n\nParameters\n----------\npsadithte : in/output rank-1 array('d') with bounds (150)\npsadiprs : in/output rank-1 array('d') with bounds (150)\npsaditmk : in/output rank-2 array('d') with bounds (150,150)\nfname : input string(len=-1)\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n"
    pass

def dpfcalc():
    "pf = dpfcalc(prs,sfp,ter_follow,[mix,mjy,mkzh])\n\nWrapper for ``dpfcalc``.\n\nParameters\n----------\nprs : input rank-3 array('d') with bounds (mkzh,mix,mjy)\nsfp : input rank-2 array('d') with bounds (mix,mjy)\nter_follow : input int\n\nOther Parameters\n----------------\nmix : input int, optional\n    Default: shape(prs,1)\nmjy : input int, optional\n    Default: shape(prs,2)\nmkzh : input int, optional\n    Default: shape(prs,0)\n\nReturns\n-------\npf : rank-3 array('d') with bounds (mkzh,mix,mjy)\n"
    pass

def dzstag():
    "znew = dzstag(znew,z,terrain,[nx,ny,nz,nxz,nyz,nzz])\n\nWrapper for ``dzstag``.\n\nParameters\n----------\nznew : input rank-3 array('d') with bounds (nx,ny,nz)\nz : input rank-3 array('d') with bounds (nxz,nyz,nzz)\nterrain : input rank-2 array('d') with bounds (nxz,nyz)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(znew,0)\nny : input int, optional\n    Default: shape(znew,1)\nnz : input int, optional\n    Default: shape(znew,2)\nnxz : input int, optional\n    Default: shape(z,0)\nnyz : input int, optional\n    Default: shape(z,1)\nnzz : input int, optional\n    Default: shape(z,2)\n\nReturns\n-------\nznew : rank-3 array('d') with bounds (nx,ny,nz)\n"
    pass

def filter2d():
    "a = filter2d(a,b,it,missing,cenweight,[nx,ny])\n\nWrapper for ``filter2d``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (nx,ny)\nb : in/output rank-2 array('f') with bounds (nx,ny)\nit : input int\nmissing : input float\ncenweight : input float\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(a,0)\nny : input int, optional\n    Default: shape(a,1)\n\nReturns\n-------\na : rank-2 array('f') with bounds (nx,ny)\n"
    pass

def fomp_destroy_lock(svar):
    "fomp_destroy_lock(svar)\n\nWrapper for ``fomp_destroy_lock``.\n\nParameters\n----------\nsvar : in/output rank-0 array(int,'i')\n"
    pass

def fomp_destroy_nest_lock(nvar):
    "fomp_destroy_nest_lock(nvar)\n\nWrapper for ``fomp_destroy_nest_lock``.\n\nParameters\n----------\nnvar : in/output rank-0 array(long,'q')\n"
    pass

def fomp_enabled():
    'fomp_enabled = fomp_enabled()\n\nWrapper for ``fomp_enabled``.\n\nReturns\n-------\nfomp_enabled : int\n'
    pass

def fomp_get_active_level():
    'fomp_get_active_level = fomp_get_active_level()\n\nWrapper for ``fomp_get_active_level``.\n\nReturns\n-------\nfomp_get_active_level : int\n'
    pass

def fomp_get_ancestor_thread_num():
    'fomp_get_ancestor_thread_num = fomp_get_ancestor_thread_num(level)\n\nWrapper for ``fomp_get_ancestor_thread_num``.\n\nParameters\n----------\nlevel : input int\n\nReturns\n-------\nfomp_get_ancestor_thread_num : int\n'
    pass

def fomp_get_dynamic():
    'fomp_get_dynamic = fomp_get_dynamic()\n\nWrapper for ``fomp_get_dynamic``.\n\nReturns\n-------\nfomp_get_dynamic : int\n'
    pass

def fomp_get_level():
    'fomp_get_level = fomp_get_level()\n\nWrapper for ``fomp_get_level``.\n\nReturns\n-------\nfomp_get_level : int\n'
    pass

def fomp_get_max_active_levels():
    'fomp_get_max_active_levels = fomp_get_max_active_levels()\n\nWrapper for ``fomp_get_max_active_levels``.\n\nReturns\n-------\nfomp_get_max_active_levels : int\n'
    pass

def fomp_get_max_threads():
    'fomp_get_max_threads = fomp_get_max_threads()\n\nWrapper for ``fomp_get_max_threads``.\n\nReturns\n-------\nfomp_get_max_threads : int\n'
    pass

def fomp_get_nested():
    'fomp_get_nested = fomp_get_nested()\n\nWrapper for ``fomp_get_nested``.\n\nReturns\n-------\nfomp_get_nested : int\n'
    pass

def fomp_get_num_procs():
    'fomp_get_num_procs = fomp_get_num_procs()\n\nWrapper for ``fomp_get_num_procs``.\n\nReturns\n-------\nfomp_get_num_procs : int\n'
    pass

def fomp_get_num_threads():
    'fomp_get_num_threads = fomp_get_num_threads()\n\nWrapper for ``fomp_get_num_threads``.\n\nReturns\n-------\nfomp_get_num_threads : int\n'
    pass

def fomp_get_schedule():
    'kind,modifier = fomp_get_schedule()\n\nWrapper for ``fomp_get_schedule``.\n\nReturns\n-------\nkind : int\nmodifier : int\n'
    pass

def fomp_get_team_size():
    'fomp_get_team_size = fomp_get_team_size(level)\n\nWrapper for ``fomp_get_team_size``.\n\nParameters\n----------\nlevel : input int\n\nReturns\n-------\nfomp_get_team_size : int\n'
    pass

def fomp_get_thread_limit():
    'fomp_get_thread_limit = fomp_get_thread_limit()\n\nWrapper for ``fomp_get_thread_limit``.\n\nReturns\n-------\nfomp_get_thread_limit : int\n'
    pass

def fomp_get_thread_num():
    'fomp_get_thread_num = fomp_get_thread_num()\n\nWrapper for ``fomp_get_thread_num``.\n\nReturns\n-------\nfomp_get_thread_num : int\n'
    pass

def fomp_get_wtick():
    'fomp_get_wtick = fomp_get_wtick()\n\nWrapper for ``fomp_get_wtick``.\n\nReturns\n-------\nfomp_get_wtick : float\n'
    pass

def fomp_get_wtime():
    'fomp_get_wtime = fomp_get_wtime()\n\nWrapper for ``fomp_get_wtime``.\n\nReturns\n-------\nfomp_get_wtime : float\n'
    pass

def fomp_in_final():
    'fomp_in_final = fomp_in_final()\n\nWrapper for ``fomp_in_final``.\n\nReturns\n-------\nfomp_in_final : int\n'
    pass

def fomp_in_parallel():
    'fomp_in_parallel = fomp_in_parallel()\n\nWrapper for ``fomp_in_parallel``.\n\nReturns\n-------\nfomp_in_parallel : int\n'
    pass

def fomp_init_lock():
    'svar = fomp_init_lock()\n\nWrapper for ``fomp_init_lock``.\n\nReturns\n-------\nsvar : int\n'
    pass

def fomp_init_nest_lock():
    'nvar = fomp_init_nest_lock()\n\nWrapper for ``fomp_init_nest_lock``.\n\nReturns\n-------\nnvar : long\n'
    pass

def fomp_set_dynamic(dynamic_threads):
    'fomp_set_dynamic(dynamic_threads)\n\nWrapper for ``fomp_set_dynamic``.\n\nParameters\n----------\ndynamic_threads : input int\n'
    pass

def fomp_set_lock(svar):
    "fomp_set_lock(svar)\n\nWrapper for ``fomp_set_lock``.\n\nParameters\n----------\nsvar : in/output rank-0 array(int,'i')\n"
    pass

def fomp_set_max_active_levels(max_levels):
    'fomp_set_max_active_levels(max_levels)\n\nWrapper for ``fomp_set_max_active_levels``.\n\nParameters\n----------\nmax_levels : input int\n'
    pass

def fomp_set_nest_lock(nvar):
    "fomp_set_nest_lock(nvar)\n\nWrapper for ``fomp_set_nest_lock``.\n\nParameters\n----------\nnvar : in/output rank-0 array(long,'q')\n"
    pass

def fomp_set_nested(nested):
    'fomp_set_nested(nested)\n\nWrapper for ``fomp_set_nested``.\n\nParameters\n----------\nnested : input int\n'
    pass

def fomp_set_num_threads(num_threads):
    'fomp_set_num_threads(num_threads)\n\nWrapper for ``fomp_set_num_threads``.\n\nParameters\n----------\nnum_threads : input int\n'
    pass

def fomp_set_schedule(kind, modifier):
    'fomp_set_schedule(kind,modifier)\n\nWrapper for ``fomp_set_schedule``.\n\nParameters\n----------\nkind : input int\nmodifier : input int\n'
    pass

def fomp_test_lock():
    "fomp_test_lock = fomp_test_lock(svar)\n\nWrapper for ``fomp_test_lock``.\n\nParameters\n----------\nsvar : in/output rank-0 array(int,'i')\n\nReturns\n-------\nfomp_test_lock : int\n"
    pass

def fomp_test_nest_lock():
    "fomp_test_nest_lock = fomp_test_nest_lock(nvar)\n\nWrapper for ``fomp_test_nest_lock``.\n\nParameters\n----------\nnvar : in/output rank-0 array(long,'q')\n\nReturns\n-------\nfomp_test_nest_lock : int\n"
    pass

def fomp_unset_lock(svar):
    "fomp_unset_lock(svar)\n\nWrapper for ``fomp_unset_lock``.\n\nParameters\n----------\nsvar : in/output rank-0 array(int,'i')\n"
    pass

def fomp_unset_nest_lock(nvar):
    "fomp_unset_nest_lock(nvar)\n\nWrapper for ``fomp_unset_nest_lock``.\n\nParameters\n----------\nnvar : in/output rank-0 array(long,'q')\n"
    pass

def omgcalc():
    "omg = omgcalc(qvp,tmk,www,prs,omg,[mx,my,mz])\n\nWrapper for ``omgcalc``.\n\nParameters\n----------\nqvp : input rank-3 array('d') with bounds (mx,my,mz)\ntmk : input rank-3 array('d') with bounds (mx,my,mz)\nwww : input rank-3 array('d') with bounds (mx,my,mz)\nprs : input rank-3 array('d') with bounds (mx,my,mz)\nomg : input rank-3 array('d') with bounds (mx,my,mz)\n\nOther Parameters\n----------------\nmx : input int, optional\n    Default: shape(qvp,0)\nmy : input int, optional\n    Default: shape(qvp,1)\nmz : input int, optional\n    Default: shape(qvp,2)\n\nReturns\n-------\nomg : rank-3 array('d') with bounds (mx,my,mz)\n"
    pass

def omp_constants():
    "'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n"
    pass

def rotatecoords():
    'olat,olon = rotatecoords(ilat,ilon,olat,olon,lat_np,lon_np,lon_0,direction)\n\nWrapper for ``rotatecoords``.\n\nParameters\n----------\nilat : input float\nilon : input float\nolat : input float\nolon : input float\nlat_np : input float\nlon_np : input float\nlon_0 : input float\ndirection : input int\n\nReturns\n-------\nolat : float\nolon : float\n'
    pass

def testfunc():
    "b = testfunc(a,b,c,errstat,errmsg,[nx,ny,nz])\n\nWrapper for ``testfunc``.\n\nParameters\n----------\na : input rank-3 array('d') with bounds (nx,ny,nz)\nb : input rank-3 array('d') with bounds (nx,ny,nz)\nc : input string(len=-1)\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(a,0)\nny : input int, optional\n    Default: shape(a,1)\nnz : input int, optional\n    Default: shape(a,2)\n\nReturns\n-------\nb : rank-3 array('d') with bounds (nx,ny,nz)\n"
    pass

def tonpsadiabat():
    "tonpsadiabat = tonpsadiabat(thte,prs,psadithte,psadiprs,psaditmk,gamma,errstat,errmsg)\n\nWrapper for ``tonpsadiabat``.\n\nParameters\n----------\nthte : input float\nprs : input float\npsadithte : input rank-1 array('d') with bounds (150)\npsadiprs : input rank-1 array('d') with bounds (150)\npsaditmk : input rank-2 array('d') with bounds (150,150)\ngamma : input float\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nReturns\n-------\ntonpsadiabat : float\n"
    pass

def tvirtual():
    'tvirtual = tvirtual(temp,ratmix)\n\nWrapper for ``tvirtual``.\n\nParameters\n----------\ntemp : input float\nratmix : input float\n\nReturns\n-------\ntvirtual : float\n'
    pass

def virtual_temp():
    "tv = virtual_temp(temp,ratmix,tv,[nx,ny,nz])\n\nWrapper for ``virtual_temp``.\n\nParameters\n----------\ntemp : input rank-3 array('d') with bounds (nx,ny,nz)\nratmix : input rank-3 array('d') with bounds (nx,ny,nz)\ntv : input rank-3 array('d') with bounds (nx,ny,nz)\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(temp,0)\nny : input int, optional\n    Default: shape(temp,1)\nnz : input int, optional\n    Default: shape(temp,2)\n\nReturns\n-------\ntv : rank-3 array('d') with bounds (nx,ny,nz)\n"
    pass

def wetbulbcalc():
    "twb = wetbulbcalc(prs,tmk,qvp,twb,psafile,errstat,errmsg,[nx,ny,nz])\n\nWrapper for ``wetbulbcalc``.\n\nParameters\n----------\nprs : input rank-3 array('d') with bounds (nx,ny,nz)\ntmk : input rank-3 array('d') with bounds (nx,ny,nz)\nqvp : input rank-3 array('d') with bounds (nx,ny,nz)\ntwb : input rank-3 array('d') with bounds (nx,ny,nz)\npsafile : input string(len=-1)\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nOther Parameters\n----------------\nnx : input int, optional\n    Default: shape(prs,0)\nny : input int, optional\n    Default: shape(prs,1)\nnz : input int, optional\n    Default: shape(prs,2)\n\nReturns\n-------\ntwb : rank-3 array('d') with bounds (nx,ny,nz)\n"
    pass

def wrf_constants():
    "'i'-scalar\n'i'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'b'-scalar\n'h'-scalar\n'i'-scalar\n'q'-scalar\n'f'-scalar\n'd'-scalar\n'c'-array(1)\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n'd'-scalar\n"
    pass

def wrf_intrp_value():
    "wrf_intrp_value = wrf_intrp_value(wvalp0,wvalp1,vlev,vcp0,vcp1,icase,errstat)\n\nWrapper for ``wrf_intrp_value``.\n\nParameters\n----------\nwvalp0 : input float\nwvalp1 : input float\nvlev : input float\nvcp0 : input float\nvcp1 : input float\nicase : input int\nerrstat : in/output rank-0 array(int,'i')\n\nReturns\n-------\nwrf_intrp_value : float\n"
    pass

def wrf_monotonic():
    "out = wrf_monotonic(out,in,lvprs,cor,idir,delta,icorsw,[ew,ns,nz])\n\nWrapper for ``wrf_monotonic``.\n\nParameters\n----------\nout : input rank-3 array('d') with bounds (ew,ns,nz)\nin : in/output rank-3 array('d') with bounds (ew,ns,nz)\nlvprs : input rank-3 array('d') with bounds (ew,ns,nz)\ncor : input rank-2 array('d') with bounds (ew,ns)\nidir : input int\ndelta : input float\nicorsw : input int\n\nOther Parameters\n----------------\new : input int, optional\n    Default: shape(out,0)\nns : input int, optional\n    Default: shape(out,1)\nnz : input int, optional\n    Default: shape(out,2)\n\nReturns\n-------\nout : rank-3 array('d') with bounds (ew,ns,nz)\n"
    pass

def wrf_vintrp():
    "dataout = wrf_vintrp(datain,dataout,pres,tk,qvp,ght,terrain,sfp,smsfp,vcarray,interp_levels,icase,extrap,vcor,logp,tempout,rmsg,errstat,errmsg,[numlevels,ew,ns,nz])\n\nWrapper for ``wrf_vintrp``.\n\nParameters\n----------\ndatain : input rank-3 array('d') with bounds (ew,ns,nz)\ndataout : input rank-3 array('d') with bounds (ew,ns,numlevels)\npres : input rank-3 array('d') with bounds (ew,ns,nz)\ntk : input rank-3 array('d') with bounds (ew,ns,nz)\nqvp : input rank-3 array('d') with bounds (ew,ns,nz)\nght : input rank-3 array('d') with bounds (ew,ns,nz)\nterrain : input rank-2 array('d') with bounds (ew,ns)\nsfp : input rank-2 array('d') with bounds (ew,ns)\nsmsfp : input rank-2 array('d') with bounds (ew,ns)\nvcarray : input rank-3 array('d') with bounds (ew,ns,nz)\ninterp_levels : input rank-1 array('d') with bounds (numlevels)\nicase : input int\nextrap : input int\nvcor : input int\nlogp : input int\ntempout : in/output rank-2 array('d') with bounds (ew,ns)\nrmsg : input float\nerrstat : in/output rank-0 array(int,'i')\nerrmsg : in/output rank-0 array(string(len=-1),'c')\n\nOther Parameters\n----------------\nnumlevels : input int, optional\n    Default: shape(dataout,2)\new : input int, optional\n    Default: shape(datain,0)\nns : input int, optional\n    Default: shape(datain,1)\nnz : input int, optional\n    Default: shape(datain,2)\n\nReturns\n-------\ndataout : rank-3 array('d') with bounds (ew,ns,numlevels)\n"
    pass

def wrfcttcalc():
    "ctt = wrfcttcalc(prs,tk,qci,qcw,qvp,ght,ter,ctt,pf,haveqci,fill_nocloud,missing,opt_thresh,[nz,ns,ew])\n\nWrapper for ``wrfcttcalc``.\n\nParameters\n----------\nprs : input rank-3 array('d') with bounds (ew,ns,nz)\ntk : input rank-3 array('d') with bounds (ew,ns,nz)\nqci : input rank-3 array('d') with bounds (ew,ns,nz)\nqcw : input rank-3 array('d') with bounds (ew,ns,nz)\nqvp : input rank-3 array('d') with bounds (ew,ns,nz)\nght : input rank-3 array('d') with bounds (ew,ns,nz)\nter : input rank-2 array('d') with bounds (ew,ns)\nctt : input rank-2 array('d') with bounds (ew,ns)\npf : in/output rank-3 array('d') with bounds (ew,ns,nz)\nhaveqci : input int\nfill_nocloud : input int\nmissing : input float\nopt_thresh : input float\n\nOther Parameters\n----------------\nnz : input int, optional\n    Default: shape(prs,2)\nns : input int, optional\n    Default: shape(prs,1)\new : input int, optional\n    Default: shape(prs,0)\n\nReturns\n-------\nctt : rank-2 array('d') with bounds (ew,ns)\n"
    pass

