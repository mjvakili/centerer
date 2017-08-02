#!/usr/bin/env python

"""
Goal: generate data at FWHM = {2,2.8,4,5.6} pixels 
with log-uniform SNR distribution between 5 and 100             
"""
import numpy as np
import sys
import h5py
import profile

if __name__ == '__main__':
    from optparse import OptionParser
    o = OptionParser()
    #o.set_usage('%prog [options]')
    #o.set_description(__doc__)

    o.add_option('-m', '--method', dest='method', default='poly',
        help='Set the centroiding method, polynomial or sdss or fitting, or efitting, default: polynomial')
    o.add_option('-f', '--fwhm', dest='fwhm', default= 2.0, type='float',
        help='FWHM, default: w')
    o.add_option('-b', '--beta', dest='beta', default= 2.5, type='float',
        help='Dimensionless parameter of Moffat profile, default: 2.5')
    
    o.add_option('--smin', dest='smin', default=5., type='float',
        help='Minimum S/N in experiment, default: 5.')
    o.add_option('--smax', dest='smax', default=150., type='float',
        help='Maximum S/N in experiment, default: 150.')
    o.add_option('--size', dest='size', default=17, type='int',
        help='size of the postage_stamp')
    o.add_option('--sample', dest='sample', default=100000, type='int',
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
    
    
    xmin , xmax = size/2 , size/2 + 1
    ymin , ymax = size/2 , size/2 + 1
    
    #snr = 10.**(np.random.uniform(np.log10(smin), np.log10(smax), sample))  #creating S/Ns
    #np.savetxt("snr.txt" , np.array(snr)  ,fmt='%.12f')                     #saving S/Ns
    snr = np.loadtxt("snr.txt")                                            #loading S/Ns

    xx = np.loadtxt("xc_f5.txt")
    yy = np.loadtxt("yc_f5.txt")   

    F = h5py.File('datap_fwhm%f.h5'%(fwhm))                                         #saving 
    dset = F.create_dataset("MyDataset" , (sample , size, size) , 'f8')           #saving

    for i in range(sample):
      xc = np.array([xx[i],yy[i]])
      flux = snr[i] ** 2. 
      data_lambda = flux * profile.makeMoffat(size , fwhm, beta , xc)         #lambda of poisson distribution
      data = np.random.poisson(lam = data_lambda)                                 #generating data as a random draw from poisson with mean = lambda

      #import matplotlib.pyplot as plt
      #from matplotlib import gridspec
      #fig = plt.figure(1, figsize=(16,8))
      #gs = gridspec.GridSpec(1,2)#, height_ratios=[1, 1], width_ratios=[1,1])  
      #ax = plt.subplot(gs[0]) 
      #ax.imshow(data_lambda, interpolation = "None", origin = "lower")
      #ax = plt.subplot(gs[1]) 
      #ax.imshow(data, interpolation = "None", origin = "lower")
      #plt.show()

      #import poisson_fitting
      
      #offsets = poisson_fitting.fitting_centroid(data, flux, fwhm[i], beta) 
      #print "offsets" , offsets
      #print xc
      dset[i] = data                                                              #saving
   
      #import psfpoly

      #offsets = psfpoly.find_centroid(data, flux, 0.00)
      #print "offsets" , offsets
      #print xc
 
    F.close() 
