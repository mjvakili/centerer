#!/usr/bin/env python



"""
Goal: This code tests centroiding of a set of 
normalized moffat profiles with a given SNR and beta
in a given range of full width at half maxima,
using four different models:
SDSS method, Polynomial method, 
and round PSF fitting method, 
and elliptical PSF fitting.

Dependencies: numpy
              
Author: Mohammadjavad Vakili (July and August 2014)
"""

import centererr
import numpy as np
import sys



if __name__ == '__main__':
    from optparse import OptionParser
    o = OptionParser()
    #o.set_usage('%prog [options]')
    #o.set_description(__doc__)

    o.add_option('-m', '--method', dest='method', default='poly',
        help='Set the centroiding method, polynomial or sdss or fitting, or efitting, default: polynomial')
    o.add_option('-s', '--snr', dest='snr', default= 150, type='float',
        help='SNR, default: 150')
    o.add_option('-b', '--beta', dest='beta', default= 2.5, type='float',
        help='Dimensionless parameter of Moffat profile, default: 2.5')
    
    o.add_option('--fmin', dest='fmin', default=2., type='float',
        help='Minimum fwhm in experiment, default: 2.')
    o.add_option('--fmax', dest='fmax', default=5.6, type='float',
        help='Maximum fwhm in experiment, default: 5.6')
    o.add_option('--size', dest='size', default=17, type='int',
        help='size of the postage_stamp')
    o.add_option('--sample', dest='sample', default=20000, type='int',
        help='number of stars in experiment')
    opts, args = o.parse_args(sys.argv[1:])


    #ifn=args[0]
    
    if not (opts.size is None):
        size = opts.size
    
    if not (opts.snr is None):
        snr = opts.snr

    if not (opts.fmin is None):
        fmin = opts.fmin

    if not (opts.fmax is None):
        fmax = opts.fmax

    if not (opts.sample is None):
        sample = opts.sample

    if not (opts.beta is None):
        beta = opts.beta
    
    
    xmin , xmax = size/2 , size/2 + 1
    ymin , ymax = size/2 , size/2 + 1
    
    f = np.random.uniform( fmin , fmax , sample)
    sigma = 0.478/(f*snr)
    
    xx = np.random.uniform(xmin, xmax, sample)
    yy = np.random.uniform(ymin, ymax, sample)

    
    if opts.method.startswith('poly'):

       er = []
       flag = []
       fwhm = []
       A = centererr.poly.design(2)

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])          
          data = centererr.profile.makeMoffat(size , f[i] , beta , 0.2 , xc)
          data += np.random.normal(0, sigma[i] , data.shape)
          
          xs = centererr.poly.poly_centroid(data , A)
          cen = centererr.poly.BP(data)
          er.append(((xs[0] + cen[0] + .5 - xc[0])**2. + (xs[1] + cen[1] + .5 -xc[1])**2.)**.5)
          fwhm.append(f[i])
          if ((xs[0]>.5)|(xs[0]<-.5)|(xs[1]>.5)|(xs[1]<-.5)|(xs[0].imag!=0.)|(xs[1].imag!=0.)):
          
            flag.append(i)
       
       np.savetxt("er1_s10_02.txt" , np.array(er) ,fmt='%.8f')
       np.savetxt("flag1_s10_02.txt" , np.array(flag) , fmt = '%.8f')
       np.savetxt("fwhm1_s10_02.txt" , np.array(fwhm) , fmt = '%.8f')


    elif opts.method.startswith('sdss'):

       er = []
       flag = []
       fwhm = []
       

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])                  # true centroid
          data = centererr.profile.makeMoffat(size , f[i], beta  , 0.2 , xc)
          data += np.random.normal(0, sigma[i] , data.shape)
          cen = centererr.sdss.BP(data , f[i])
          xs = centererr.sdss.sdss_centroid(data , f[i] , sigma[i])
          
          er.append(((xs[0] + cen[0] + .5 - xc[0])**2. + (xs[1] + cen[1] + .5 -xc[1])**2.)**.5)
          fwhm.append(f[i])
          if ((xs[0]>.5)|(xs[0]<-.5)|(xs[1]>.5)|(xs[1]<-.5)|(xs[0].imag!=0.)|(xs[1].imag!=0.)):
          
            flag.append(i)
          
       np.savetxt("er2_s10_02.txt" , np.array(er) ,fmt='%.8f')
       np.savetxt("flag2_s10_02.txt" , np.array(flag) , fmt = '%.8f')
       np.savetxt("fwhm2_s10_02.txt" , np.array(fwhm) , fmt = '%.8f')
       
    elif opts.method.startswith('fitting'):
       
       er = []
       flag = []
       fwhm = []
       

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])                  # true centroid
          data = centererr.profile.makeMoffat(size , f[i] , beta , 0.2 , xc)
          data += np.random.normal(0, sigma[i] , data.shape)
          
          xs = centererr.fitting.fitting_centroid(data)
          
          er.append(((xs[0]  - xc[0])**2. + (xs[1]  -xc[1])**2.)**.5)
          fwhm.append(f[i])
          
       np.savetxt("er3_s10_02.txt" , np.array(er) ,fmt='%.8f')
       np.savetxt("flag3_s10_02.txt" , np.array(flag) , fmt = '%.8f')
       np.savetxt("fwhm3_s10_02.txt" , np.array(fwhm) , fmt = '%.8f')
       
    
    elif opts.method.startswith('efitting'):
       
       er = []
       flag = []
       fwhm = []
       

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])                  # true centroid
          data = centererr.profile.makeMoffat(size , f[i] , beta , 0.1 , xc)
          data += np.random.normal(0, sigma[i] , data.shape)
          
          xs = centererr.efitting.fitting_centroid(data)
          
          er.append(((xs[0]  - xc[0])**2. + (xs[1]  -xc[1])**2.)**.5)
          fwhm.append(f[i])
          
       np.savetxt("er4_s10_01.txt" , np.array(er) ,fmt='%.8f')
       np.savetxt("flag4_s10_01.txt" , np.array(flag) , fmt = '%.8f')
       np.savetxt("fwhm4_s10_01.txt" , np.array(fwhm) , fmt = '%.8f')
