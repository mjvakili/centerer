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
import h5py


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
    
    #f = np.random.uniform(fmin, fmax, sample)
    f = np.loadtxt("f_snr5.txt")
    sigma = 0.478/(f*snr)
    
    #xx = np.random.uniform(xmin, xmax, sample)
    #yy = np.random.uniform(ymin, ymax, sample)

    #np.savetxt("xc_snr5.txt"  , np.array(xx)  ,fmt='%.12f')
    xx = np.loadtxt("xc_snr5.txt")
    #np.savetxt("yc_snr5.txt"  , np.array(yy)  ,fmt='%.12f')
    yy = np.loadtxt("yc_snr5.txt")   
    #np.savetxt("f_snr5.txt"   ,  np.array(f)  ,fmt='%.12f')
    """F = h5py.File('data_snr5.h5' , 'r')
    DATA = F["MyDataset"][:]"""
    if opts.method.startswith('poly'):
       cent = []
       erx  = []
       ery  = []
       flag = []
       fwhm = []
       A = centererr.poly.design(2)

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])          
          data = centererr.profile.makeMoffat(size , f[i] , beta , 0.0 , xc)
          data += np.random.normal(0, sigma[i] , data.shape)
          
          xs = centererr.poly.poly_centroid(data , A)
          #cen = centererr.poly.BP(data)
          #cent.append(cen[0])
          erx.append((xs[0] - xc[0])**2.)
          ery.append((xs[1] - xc[1])**2.)
          fwhm.append(f[i])
          if ((xs[0]>.5)|(xs[0]<-.5)|(xs[1]>.5)|(xs[1]<-.5)|(xs[0].imag!=0.)|(xs[1].imag!=0.)):
          
            flag.append(i)
       #np.savetxt("center1_s40_00.txt" , np.array(cent))
       np.savetxt("erx1_s5_00s.txt"  , np.array(erx)  ,fmt='%.12f')
       np.savetxt("ery1_s5_00s.txt"  , np.array(ery)  ,fmt='%.12f')
       np.savetxt("flag1_s5_00s.txt" , np.array(flag) , fmt = '%.12f')
       np.savetxt("fwhm1_s5_00s.txt" , np.array(fwhm) , fmt = '%.12f')

    
    elif opts.method.startswith('spoly'):
       #cent = []
       erx = []
       ery = []
       flag = []
       fwhm = []
       A = centererr.spoly.design(2)
       F = h5py.File('data_snr40.h5')
       dset = F.create_dataset("MyDataset" , (100000 , 17 , 17) , 'f8')
       
       for i in range(sample):
        
        
		         
        xc =  np.array([xx[i],yy[i]])          
        data = centererr.profile.makeMoffat(size , f[i] , beta , 0.0 , xc)
        
        data += np.random.normal(0, sigma[i] , data.shape)
        #data = DATA[i]                                       #loading
        bp = np.where(data==data.max())
        dset[i] = data                                        #saving 
        
        if ([bp[1][0] , bp[0][0]] == [8,8]):
          
          xs = centererr.spoly.spoly_centroid(data , A , 1.2 , sigma[i])
          
          erx.append((xs[0] - xc[0])**2.)
          ery.append((xs[1] - xc[1])**2.)
          fwhm.append(f[i])
          if ((xs[0]>.5)|(xs[0]<-.5)|(xs[1]>.5)|(xs[1]<-.5)|(xs[0].imag!=0.)|(xs[1].imag!=0.)):
          
            flag.append(i)
       F.close() 
       #np.savetxt("center5_s40_00.txt" , np.array(cent))
       np.savetxt("erx5_s5_00tb.txt"  , np.array(erx)  , fmt='%.12f')
       np.savetxt("ery5_s5_00tb.txt"  , np.array(ery)  , fmt='%.12f')
       np.savetxt("flag5_s5_00tb.txt" , np.array(flag) , fmt = '%.12f')
       np.savetxt("fwhm5_s5_00tb.txt" , np.array(fwhm) , fmt = '%.12f')

    elif opts.method.startswith('sdss'):

       erx = []
       ery = []
       flag = []
       fwhm = []
       #cent = []

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])                  # true centroid
          data = centererr.profile.makeMoffat(size , f[i], beta  , 0.0 , xc)
          data += np.random.normal(0, sigma[i] , data.shape)
          #cen = centererr.sdss.BP(data , 2.)
          xs = centererr.sdss.sdss_centroid(data , 1.2 , sigma[i])
          #cent.append(cen[0])
          erx.append((xs[0] - xc[0])**2.)
          ery.append((xs[1] - xc[1])**2.)
          fwhm.append(f[i])
          if ((xs[0]>.5)|(xs[0]<-.5)|(xs[1]>.5)|(xs[1]<-.5)|(xs[0].imag!=0.)|(xs[1].imag!=0.)):
          
            flag.append(i)
       #np.savetxt("center2_s5_00.txt", np.array(cent))   
       np.savetxt("erx2_s20_00.txt"   , np.array(erx)  , fmt='%.12f')
       np.savetxt("ery2_s20_00.txt"   , np.array(ery)  , fmt='%.12f')
       np.savetxt("flag2_s20_00.txt"  , np.array(flag) , fmt = '%.12f')
       np.savetxt("fwhm2_s20_00.txt"  , np.array(fwhm) , fmt = '%.12f')
       
    elif opts.method.startswith('fitting'):
       
       erx = []
       ery = []
       flag = []
       fwhm = []
       

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])                  # true centroid
          data = centererr.profile.makeMoffat(size , f[i] , beta , 0.0 , xc)
          data += np.random.normal(0, sigma[i] , data.shape)
          
          xs = centererr.fitting.fitting_centroid(data , sigma[i] , f[i] , 2.5)
          
          erx.append((xs[0]  - xc[0])**2.)
          ery.append((xs[1]  - xc[1])**2.)
          fwhm.append(f[i])
          
       np.savetxt("erx3_s10_00.txt"   , np.array(erx)   , fmt = '%.12f')
       np.savetxt("ery3_s10_00.txt"   , np.array(ery)   , fmt = '%.12f')
       np.savetxt("flag3_s10_00.txt" , np.array(flag) , fmt = '%.12f')
       np.savetxt("fwhm3_s10_00.txt" , np.array(fwhm) , fmt = '%.12f')
       
    
    elif opts.method.startswith('efitting'):
       
       er = []
       flag = []
       fwhm = []
       

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])                  # true centroid
          data = centererr.profile.makeMoffat(size , f[i] , beta , 0.2 , xc)
          data += np.random.normal(0, sigma[i] , data.shape)
          
          xs = centererr.efitting.fitting_centroid(data)
          
          er.append(((xs[0]  - xc[0])**2. + (xs[1]  -xc[1])**2.)**.5)
          fwhm.append(f[i])
          
       np.savetxt("er4_s10_02.txt" , np.array(er) ,fmt='%.8f')
       np.savetxt("flag4_s10_02.txt" , np.array(flag) , fmt = '%.8f')
       np.savetxt("fwhm4_s10_02.txt" , np.array(fwhm) , fmt = '%.8f')
