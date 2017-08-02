#!/usr/bin/env python

"""
Goal: generate data at S/N = {5,10,20,40} 
with uniform FWHM
distribution between 2 and 6 pixe              
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
    o.add_option('-s', '--snr', dest='snr', default= 50, type='float',
        help='SNR, default: 5')
    o.add_option('-b', '--beta', dest='beta', default= 2.5, type='float',
        help='Dimensionless parameter of Moffat profile, default: 2.5')
    
    o.add_option('--fmin', dest='fmin', default=2., type='float',
        help='Minimum fwhm in experiment, default: 2.')
    o.add_option('--fmax', dest='fmax', default=6., type='float',
        help='Maximum fwhm in experiment, default: 6.')
    o.add_option('--size', dest='size', default=17, type='int',
        help='size of the postage_stamp')
    o.add_option('--sample', dest='sample', default=100000, type='int',
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
    
    
    flux = snr ** 2.   #for poisson noise
    
    fwhm = np.random.uniform(fmin, fmax, sample)

    #np.savetxt("fwhm_f5.txt" , fwhm)
    fwhm = np.loadtxt("fwhm_f5.txt")

    xx = np.loadtxt("xc_f5.txt")
    yy = np.loadtxt("yc_f5.txt")   

    F = h5py.File('datap_snr%d.h5'%(snr))                                         #saving 
    dset = F.create_dataset("MyDataset" , (sample , size, size) , 'f8')           #saving

    for i in range(sample):
      xc = np.array([xx[i],yy[i]])
      data_lambda = flux * profile.makeMoffat(size , fwhm[i] , beta , xc)         #lambda of poisson distribution
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
