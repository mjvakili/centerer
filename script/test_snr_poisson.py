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
    
    snr = np.loadtxt("snr.txt")                                            #loading S/Ns

    xx = np.loadtxt("xc_f5.txt")
    yy = np.loadtxt("yc_f5.txt")   

    F = h5py.File('datap_fwhm%f.h5'%(fwhm), 'r')                                         #saving 
    dset = F["MyDataset"]          
    print dset

    import poisson_flux_fitting, psfpoly, spolynom,  moment

    er1, er2, er3, er4 = [], [], [], []

    for i in range(sample):
      
      print i

      flux = snr[i] ** 2. 
      data = dset[i]

      offsets1 = poisson_flux_fitting.fitting_centroid(data, fwhm, beta) 
      offsets2 = psfpoly.find_centroid(data, fwhm, 0)
      offsets3 = spolynom.find_centroid(data, 2.8, np.mean(data))
      offsets4 = moment.find_cen(data)
     

      er1.append(offsets1[0] - xx[i])
      er2.append(offsets2[1] - xx[i])
      er3.append(offsets3[1] - xx[i])
      er4.append(offsets4[1] - xx[i])

      #print er1[i], er2[i], er3[i]

    np.savetxt("results/erx_fitting_"+str(10*fwhm)+".txt" , np.array(er1))	
    np.savetxt("results/erx_psfpoly_"+str(10*fwhm)+".txt" , np.array(er2))	
    np.savetxt("results/erx_spoly_"+str(10*fwhm)+".txt" , np.array(er3))	
    np.savetxt("results/erx_moment_"+str(10*fwhm)+".txt" , np.array(er4))	

      
 
    F.close() 
