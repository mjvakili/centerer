#!/usr/bin/env python



"""
Goal: This code tests centroiding of a set of 
normalized moffat profiles with a given FWHM and beta
in a given range of signal-to-noise-ratios,
using three different models:
SDSS method, Polynomial method, 
and PSF fitting method.

Dependencies: numpy, profile.py,
              poly.py, sdss.py
Author: Mohammadjavad Vakili (July and August 2014)
"""
import profile
import matplotlib.pyplot as p
import centererr
import numpy as np
import sys
import matplotlib
from matplotlib import pyplot
import scipy
import matplotlib.cm as cm
from scipy import interpolate
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
s = matplotlib.font_manager.FontProperties()
s.set_family('serif')
s.set_size(14)
from matplotlib import rc
rc('text', usetex=False)
rc('font', family='serif')
s = matplotlib.font_manager.FontProperties()
s.set_family('serif')

from matplotlib.colors import LogNorm
p.rcParams['text.latex.preamble'] = [r"\usepackage{lmodern}"]
params = {'text.usetex' : True, 'font.size' : 20 , 'font.family' : 'lmodern' , 'text.latex.unicode' : True, }
p.rcParams.update(params)
from scipy.interpolate import griddata


if __name__ == '__main__':
    from optparse import OptionParser
    o = OptionParser()
    #o.set_usage('%prog [options]')
    #o.set_description(__doc__)

    o.add_option('-m', '--method', dest='method', default='poly',
        help='Set the centroiding method, polynomial or sdss or fitting, or efitting, default: polynomial')
    o.add_option('-f', '--fwhm', dest='fwhm', default= 2., type='float',
        help='FWHM of the moffat profile, default: 2')
    o.add_option('-b', '--beta', dest='beta', default= 2.5, type='float',
        help='Dimensionless parameter of Moffat profile, default: 2.5')
    o.add_option('-e', '--ell', dest='ell', default= 0.0, type='float',
        help='Ellipticity of the Moffat profile, default: 0.0')
    o.add_option('--s', dest='snr', default=50., type='float',
        help='S/N in experiment, default: 50.0')
    o.add_option('--size', dest='size', default=17, type='int',
        help='size of the postage_stamp')
    o.add_option('--sample', dest='sample', default=20, type='int',
        help='number of stars in experiment')
    opts, args = o.parse_args(sys.argv[1:])


    #ifn=args[0]
    
    if not (opts.size is None):
        size = opts.size
    
    if not (opts.fwhm is None):
        fwhm = opts.fwhm

    if not (opts.snr is None):
        snr = opts.snr

    if not (opts.sample is None):
        sample = opts.sample

    if not (opts.beta is None):
        beta = opts.beta
    if not (opts.ell is None):
        ell = opts.ell
    
    
    xmin , xmax = size/2 , size/2 + 1
    ymin , ymax = size/2 , size/2 + 1
    
    Xp = np.linspace(xmin , xmax ,  sample)
    Yp = np.linspace(ymin , ymax ,  sample)
    sigma = .478/(fwhm*snr)
    xv, yv = np.meshgrid(Xp, Yp)
    ell = .1
    xv = xv.flatten()
    yv = yv.flatten()
    from scipy import signal
    A = centererr.poly.design(2) 
    if opts.method.startswith('poly'):
       
       xc = np.array([8.3 , 8.3])         
       data = centererr.profile.makeMoffat(size , fwhm , beta , ell , xc)
       data += np.random.normal(0, sigma , data.shape)
       kernel = centererr.profile.makeGaussian(17 , fwhm , 0 , np.array([8.5,8.5]))
  
       data = signal.convolve2d(data , kernel , mode = "same")     
       xs1 = centererr.spoly.spoly_centroid(data , A , fwhm , sigma)
       cen1 = centererr.spoly.BP(data , fwhm)

       xs2 = centererr.sdss.sdss_centroid(data , fwhm  , sigma)
       cen2 = centererr.sdss.BP(data , fwhm)
       print xs2
       w = centererr.sdss.lupton_2(data[cen1[0]-1:cen1[0]+2,cen1[1]-1:cen1[1]+2] , fwhm , sigma)
       xx = np.linspace(cen2[0]-7 , cen2[0]+7 , 100)
       y =  np.linspace(cen2[1]-7 , cen2[1]+7 , 100)
       yy = w[0][0] + w[0][1]*(xx-cen2[0]) + w[0][2]*(xx-cen2[0])**2. + cen2[1]
       zz = w[1][0] + w[1][1]*(y-cen2[1]) + w[1][2]*(y-cen2[1])**2. + cen2[0] 
       xxx  = np.array([w[2][0] , w[3][0] , w[4][0]]) + cen2[1]
       yyy  = np.array([ 1 , 0 , -1]) + cen2[0]  
       exxx = np.array([w[2][1] , w[3][1] , w[4][1]])
       xxxx  = np.array([w[5][0] , w[6][0] , w[7][0]]) + cen2[0]
       yyyy  = np.array([ 1 , 0 , -1]) + cen2[1]  
       exxxx = np.array([w[5][1] , w[6][1] , w[7][1]])
       fig = p.figure()  
       p.imshow(data , interpolation = "None" , origin = "lower")
       p.plot(xc[0] - .5 , xc[1] - .5  , "k*")
       p.plot(xx , yy , "k--")
       p.plot(zz , y , "k--")
       p.plot(xs2[0] + cen2[0] , xs2[1]+ cen2[1] , "k^")
       p.errorbar(yyy, xxx , yerr= (.4)*exxx, fmt='k.')
       p.errorbar(xxxx , yyyy , xerr = (.4)*exxx, fmt='k.')
       p.plot(xs1[0] + cen1[0] , xs1[1]+ cen1[1] , "ko")
       p.xlim((1.5 , 14.5))
       p.ylim((1.5 , 14.5))
       p.xticks(())
       p.yticks(())
       fig.set_size_inches(10,10)
       p.show()
       #p.savefig("10025.pdf" , dpi=10)          
       
            

