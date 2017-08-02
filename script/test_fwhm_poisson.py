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
    o.add_option('-s', '--snr', dest='snr', default= 5.0, type='float',
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

    fwhm = np.loadtxt("fwhm_f5.txt")

    xx = np.loadtxt("xc_f5.txt")
    yy = np.loadtxt("yc_f5.txt")   

    F = h5py.File('datap_snr%d.h5'%(snr), 'r')                                         #saving 
    dset = F["MyDataset"]        #saving
    print dset

    import poisson_flux_fitting, psfpoly, spolynom,  moment

    er1, er2, er3, er4 = [], [], [], []

    for i in range(sample):

      print i

      xc = np.array([xx[i],yy[i]])
      data = dset[i]                                                             #saving
   
      offsets1 = poisson_flux_fitting.fitting_centroid(data, flux, fwhm[i], beta) 
     
      #print "offset1" , offsets1 , np.array([xx[i] , yy[i]])
      
      offsets2 = psfpoly.find_centroid(data, fwhm[i], 0)

      #print "offset2" , offsets2 , np.array([xx[i] , yy[i]])
      
      offsets3 = spolynom.find_centroid(data, 2.8, 0.01)
     
      #print "offset3" , offsets3 , np.array([xx[i] , yy[i]])
 
      offsets4 = moment.find_cen(data)
     
      #print "offset4" , offsets4 , np.array([xx[i] , yy[i]])
      
      #print fwhm[i]
      

      er1.append(offsets1[0] - xx[i])
      er2.append(offsets2[1] - xx[i])
      er3.append(offsets3[1] - xx[i])
      er4.append(offsets4[1] - xx[i])


    np.savetxt("results/erx_fitting_snr_"+str(10*snr)+".txt" , np.array(er1))	
    np.savetxt("results/erx_psfpoly_snr_"+str(10*snr)+".txt" , np.array(er2))	
    np.savetxt("results/erx_spoly_snr_"+str(10*snr)+".txt" , np.array(er3))	
    np.savetxt("results/erx_moment_snr_"+str(10*snr)+".txt" , np.array(er4))	

 
    F.close() 
