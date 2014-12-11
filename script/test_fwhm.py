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
    o.add_option('-f', '--fwhm', dest='fwhm', default= 2., type='float',
        help='FWHM of the moffat profile, default: 2')
    o.add_option('-b', '--beta', dest='beta', default= 2.5, type='float',
        help='Dimensionless parameter of Moffat profile, default: 2.5')
    
    o.add_option('--smin', dest='smin', default=5., type='float',
        help='Minimum S/N in experiment, default: 10.0')
    o.add_option('--smax', dest='smax', default=150, type='float',
        help='Maximum S/N in experiment, default: 150.0')
    o.add_option('--size', dest='size', default=17, type='int',
        help='size of the postage_stamp')
    o.add_option('--sample', dest='sample', default=20000, type='int',
        help='number of stars in experiment')
    opts, args = o.parse_args(sys.argv[1:])


    #ifn=args[0]
    
    if not (opts.size is None):
        size = opts.size
    
    if not (opts.fwhm is None):
        fwhm = opts.fwhm

    if not (opts.smin is None):
        smin = opts.smin

    if not (opts.smax is None):
        smax = opts.smax

    if not (opts.sample is None):
        sample = opts.sample

    if not (opts.beta is None):
        beta = opts.beta
    
    
    xmin , xmax = size/2   , size/2 + 1
    ymin , ymax = size/2   , size/2 + 1
    
    #sigmamin = .478/(fwhm*smax*((1.-0)/(1.+0))**.5)
    #sigmamax = .478/(fwhm*smin*((1.-0)/(1.+0))**.5)
    
    #snr = 10.**(np.random.uniform(np.log10(smin), np.log10(smax), sample))    #creating S/Ns
    #np.savetxt("snr.txt" , np.array(snr)  ,fmt='%.12f')                 #saving S/Ns
    snr = np.loadtxt("snr.txt")                                            #loading S/Ns
    
    sigma = .478/(fwhm*snr)                                                   #always stays here
    
    #xx = np.random.uniform(xmin, xmax, sample)                                #creating xs for all experiments
    #np.savetxt("xc_f5.txt"  , np.array(xx)  ,fmt='%.12f')                   #saving xs for all experiments
    xx = np.loadtxt("xc_f5.txt")                                            #loading xs
    
    #yy = np.random.uniform(ymin, ymax, sample)                                #creating ys for all
    #np.savetxt("yc_f5.txt"  , np.array(yy)  ,fmt='%.12f')                   #saving ys for all
    yy = np.loadtxt("yc_f5.txt")                                            #loading ys
    
    F = h5py.File('data_f%d.h5'%(10*fwhm) , 'r')                   #loading file
    DATA = F["MyDataset"][:]                                    #loading file
    #print DATA
    
    if opts.method.startswith('poly'):

       erx = []
       ery = []
       flag = []
       #noise = []
       #cent = []
       #A = centererr.poly.design(2)

       for i in range(sample):
          
          xc    =  np.array([xx[i],yy[i]])          
          data = DATA[i]
              
          xs = centererr.polynomial.find_centroid(data , sigma[i])
          #cen = centererr.poly.BP(data)
          #cent.append(cen[0])
          erx.append((xs[1] - xc[0])**2.)
          ery.append((xs[0] - xc[1])**2.)

          #if ((xs[0]>.5)|(xs[0]<-.5)|(xs[1]>.5)|(xs[1]<-.5)|(xs[0].imag!=0.)|(xs[1].imag!=0.)):
          
          #  flag.append(i)
       #np.savetxt("center1_20_00.txt" , np.array(cent) , fmt='%.12f')
       np.savetxt("erx1_f%d_00r.txt"%(10*fwhm) , np.array(erx) ,fmt='%.12f')
       np.savetxt("ery1_f%d_00r.txt"%(10*fwhm) , np.array(ery) ,fmt='%.12f')
       #np.savetxt("flag1_f%d_00r.txt"%(fwhm) , np.array(flag) , fmt = '%.12f')
       #np.savetxt("noise1_80_00.txt" , np.array(noise) , fmt = '%.12f')
       F.close()
    elif opts.method.startswith('spoly'):
   
 

       erx = []
       ery = []
       #flag = []
       #noise = []
       #cent = []
       #F = h5py.File('data_f56.h5')                                                   #saving
       #dset = F.create_dataset("MyDataset" , (100000 , 17 , 17) , 'f8')               #saving 
       #A = centererr.spoly.design(2)

       for i in range(sample):
          
          xc =  np.array([xx[i],yy[i]])  
          data  = DATA[i]                                                      #loading        
          #data = centererr.profile.makeMoffat(size , fwhm , beta , xc)  #saving
          #data += np.random.normal(0, sigma[i] , data.shape)                  #saving               
          #dset[i] = data                                                      #saving
          xs = centererr.spolynom.find_centroid(data , 1.2, sigma[i])
          #ce = centererr.spoly.BP(data , 2.)
          #cent.append(ce[0])
          erx.append((xs[1] - xc[0])**2.) 
          ery.append((xs[0] - xc[1])**2.)
          #noise.append(snr[i])
          #if ((xs[0]>.5)|(xs[0]<-.5)|(xs[1]>.5)|(xs[1]<-.5)|(xs[0].imag!=0.)|(xs[1].imag!=0.)):
          
          #  flag.append(i)
       F.close()
       #np.savetxt("center5_60_00.txt" , np.array(cent))
       np.savetxt("erx5_f%d_00r.txt"%(10*fwhm)  ,   np.array(erx)  ,fmt='%.12f')# ,fmt='%.8f')
       np.savetxt("ery5_f%d_00r.txt"%(10*fwhm)  ,   np.array(ery)  ,fmt='%.12f')# ,fmt='%.8f')
       #np.savetxt("flag55_f%d_00r.txt"%(fwhm) ,   np.array(flag) ,fmt='%.12f')# , fmt = '%.8f')
       #np.savetxt("noise5_20_00.txt",   np.array(noise),fmt='%.12f')# , fmt = '%.8f')



    elif opts.method.startswith('sdss'):

       erx = []
       ery = []
       #cent = []
       #flag = []
       #noise = []
       

       for i in range(sample):
          data = DATA[i]  #loading the data
          #print data
          xc =  np.array([xx[i],yy[i]])                      # true centroid
          
          #data = centererr.profile.makeMoffat(size , fwhm, beta  , 0. , xc)
          #data += np.random.normal(0, sigma[i] , data.shape)
          #cen = centererr.sdss.BP(data , 2.)                 # have to choose the width of the kernel here       
          xs = centererr.sdss.sdss_centroid(data , 1.2 , sigma[i])  #have to choose the width of the kernel here
          
          erx.append((xs[0] - xc[0])**2.)
          ery.append((xs[1] - xc[1])**2.)
          #noise.append(snr[i])
          #cent.append(cen[0])
          #if ((xs[0]>.5)|(xs[0]<-.5)|(xs[1]>.5)|(xs[1]<-.5)|(xs[0].imag!=0.)|(xs[1].imag!=0.)):
          
          #  flag.append(i)
       #np.savetxt("center2_20_00.txt" , np.array(cent))   
       np.savetxt("erx2_f%d_00r.txt"%(10*fwhm) , np.array(erx)     ,fmt='%.12f')
       np.savetxt("ery2_f%d_00r.txt"%(10*fwhm) , np.array(ery)     ,fmt='%.12f')
       #np.savetxt("flag2_80_00.txt" , np.array(flag)   ,fmt='%.12f')
       #np.savetxt("noise2_80_00.txt" , np.array(noise) ,fmt='%.12f')
       F.close()
    elif opts.method.startswith('fitting'):
       
       erx = []
       ery = [] 
       #flag = []
       #noise = []
       

       for i in range(sample):
          data = DATA[i]
          #print data
          xc =  np.array([xx[i],yy[i]])                  # true centroid
          #data = centererr.profile.makeMoffat(size , fwhm , beta ,xc)
          #data += np.random.normal(0, sigma[i] , data.shape)
          
          xs = centererr.fitting.fitting_centroid(data , sigma[i] , fwhm , 2.5)
          #print xs
          #print xc
          erx.append((xs[0]  - xc[0])**2.)
          ery.append((xs[1]  - xc[1])**2.)
          #noise.append(snr[i])
          
       np.savetxt("erx3_f%d_00r.txt"%(10*fwhm)   , np.array(erx)   , fmt='%.12f')
       np.savetxt("ery3_f%d_00r.txt"%(10*fwhm)  , np.array(ery)   , fmt='%.12f')
       #np.savetxt("noise3_60_00.txt" , np.array(noise) , fmt = '%.12f')
       #np.savetxt("flag3_60_00.txt"  , np.array(flag)  , fmt = '%.12f')
       F.close()
    elif opts.method.startswith('efitting'):
       
       erx = []
       ery = []
       flag = []
       #noise = []
       

       for i in range(sample):
          data = DATA[i]
          xc =  np.array([xx[i],yy[i]])                  # true centroid
          #data = centererr.profile.makeMoffat(size , fwhm , beta , 0.2 , xc)
          #data += np.random.normal(0, sigma[i] , data.shape)
          
          xs = centererr.efitting.fitting_centroid(data , sigma[i] , fwhm , 2.5)
          print xs[0]
          erx.append((xs[0]  - xc[0])**2.) 
          ery.append((xs[1]  - xc[1])**2.)
          #noise.append(sigma[i])
          
       np.savetxt("erx4_56_00r.txt" , np.array(erx) ,fmt='%.8f')
       np.savetxt("ery4_56_00r.txt" , np.array(ery) ,fmt='%.8f')
       #np.savetxt("noise4_56_02.txt" , np.array(noise) , fmt = '%.8f')
       #np.savetxt("flag4_56_02.txt" , np.array(flag) , fmt = '%.8f')
