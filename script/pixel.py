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
from scipy import signal
import matplotlib.pyplot as p
import centererr
import numpy as np
import sys
import matplotlib
from matplotlib import pyplot
import scipy
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


    #xmin , xmax = size/2 , size/2 + 1
    #ymin , ymax = size/2 , size/2 + 1
    
    #Xp = np.linspace(xmin , xmax ,  sample)
    #Yp = np.linspace(ymin , ymax ,  sample)
    sigma = .478/(fwhm*snr)
    #xv, yv = np.meshgrid(Xp, Yp)

    #xv = xv.flatten()
    #yv = yv.flatten()

    A = centererr.poly.design(2) 
    if opts.method.startswith('poly'):
       #e1 , e2 = [] , []
       for i in range(sample*sample):
          
          er1  , er2 = [] , []
          flag = []
          noise = []
          
          for j in np.arange(1):   
            #xc =  np.array([xv[i],yv[i]])          
            dataa = centererr.profile.makeMoffat(size , fwhm , beta , ell , [8.65 , 8.15])
            data = dataa + np.random.normal(0, sigma , dataa.shape)
            kernel = centererr.profile.makeGaussian(7 , 1.2 , 0 , np.array([3.5,3.5]))
  
            smoothed_image = signal.convolve2d(data , kernel , mode = "same")
            xs1 = centererr.spoly.spoly_centroid(data , A , 1.2 , sigma)
            bp = centererr.poly.BP(data)
            print bp
            x  , y = bp[1] , bp[0]

            xs2 = centererr.sdss.sdss_centroid(data , 1.2  , sigma)
            #cen2 = centererr.sdss.BP(data , fwhm)
            xs3 = centererr.poly.poly_centroid(data , A)
            print xs1
            print xs2
            print xs3
            #p.imshow(dataa , interpolation = "none" , origin = "lower")
            
            #p.xticks(())
            #p.yticks(())
            #p.show()
            p.imshow(data , interpolation = "none" , origin = "lower")
            p.xticks(())
            p.yticks(())
            p.colorbar()
            p.show()
            p.imshow(smoothed_image[y-2:y+3 , x-2:x+3] , interpolation = "none" , origin = "lower")
            p.xticks(())
            p.yticks(())
            p.colorbar()
            p.show()
            p.imshow(data[y-2:y+3 , x-2:x+3] , interpolation = "none" , origin = "lower")
            p.text(8.65-(x-2+.5) , 8.15-(y-2+.5) , "t")
            p.text(xs3[0]-(x-2+.5) , xs3[1]-(y-2+.5) , "p")
            p.text(xs2[0]-(x-2+.5) , xs2[1]-(y-2+.5) , "s")
            p.text(xs1[0]-(x-2+.5) , xs1[1]-(y-2+.5) , "m")
            p.colorbar()
            p.xticks(())
            p.yticks(())
            p.show()


