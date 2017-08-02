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
    
    
    xmin , xmax = size/2 , size/2 + 1
    ymin , ymax = size/2 , size/2 + 1
    
    Xp = np.linspace(xmin , xmax ,  sample)
    Yp = np.linspace(ymin , ymax ,  sample)
    sigma = .478/(fwhm*snr)
    xv, yv = np.meshgrid(Xp, Yp)

    xv = xv.flatten()
    yv = yv.flatten()

    A = centererr.poly.design(2) 
    if opts.method.startswith('poly'):
       e1 , e2 = [] , []
       for i in range(sample*sample):
          
          er1  , er2 = [] , []
          flag = []
          noise = []
          
          for j in np.arange(50):   
            xc =  np.array([xv[i],yv[i]])          
            data = centererr.profile.makeMoffat(size , fwhm , beta , ell , xc)
            data += np.random.normal(0, sigma , data.shape)
            
            xs1 = centererr.spoly.spoly_centroid(data , A , 1.2 , sigma)
            #cen1 = centererr.spoly.BP(data , fwhm)

            xs2 = centererr.sdss.sdss_centroid(data , 1.2  , sigma)
            #cen2 = centererr.sdss.BP(data , fwhm)
            

            er1.append(((xs1[0]- xc[0])**2. + (xs1[1] -xc[1])**2.)**.5)
            er2.append(((xs2[0]- xc[0])**2. + (xs2[1] -xc[1])**2.)**.5)
            
          e1.append(np.mean(er1))
          e2.append(np.mean(er2))   

       cx , cy = xv , yv
       points = np.zeros((xv.shape[0],2))
       points[:,0] = cx
       points[:,1] = cy

       values = np.array(e1)
       vals = np.array(e2)

#print points.shape
#print values.shape
#point = points[vals<.7]
#vals = vals[vals<.7]
#print cx
       grid_x, grid_y = np.mgrid[cx.min():cx.max():20j, cy.min():cy.max():20j]

       grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
       grid_z1 = griddata(points, vals, (grid_x, grid_y), method='nearest')
#grid_z2 = griddata(points, values, (grid_x, grid_y), method='nearest')
       from mpl_toolkits.axes_grid1 import make_axes_locatable
       import matplotlib.cm as cm
       p.subplot(1,2,1)
       ax = p.gca()
       im=ax.imshow(grid_z0.T, extent=(cx.min(),cx.max(),cy.min(),cy.max()) ,interpolation = "None", origin='lower', cmap = cm.Greys , vmin = min(values.min() , vals.min()) , vmax = max(values.max() , vals.max()))
       p.title("3by3 modified polynomial")
       #ax.set_xlim(7.5 , 9.5)
       #ax.set_ylim(7.5 , 9.5)    
       labels = [item.get_text() for item in ax.get_xticklabels()]
       labels [0] , labels[1] , labels[2] , labels[3], labels[4] , labels[5] = '-0.5' , '-0.3' , '-0.1' , '0.1' , '0.3' , '0.5'
       
       ax.set_xticklabels(labels)
       labels = [item.get_text() for item in ax.get_yticklabels()]
       labels [0] , labels[1] , labels[2] , labels[3], labels[4] , labels[5] = '-0.5' , '-0.3' , '-0.1' , '0.1' , '0.3' , '0.5'
       ax.set_yticklabels(labels)
       
       divider = make_axes_locatable(ax)
       cax = divider.append_axes("right", size="5%", pad=0.05)

       p.colorbar(im, cax=cax)
       p.subplot(1,2,2)
       ax = p.gca()
       im = ax.imshow(grid_z1.T, extent=(cx.min(),cx.max(),cy.min(),cy.max()), interpolation = "None" ,origin='lower', cmap = cm.Greys, vmin = min(values.min() , vals.min()) , vmax = max(values.max() , vals.max()) )
       p.title("3by3 sdss")
       #p.xticks(())
       #p.yticks(())
       labels = [item.get_text() for item in ax.get_xticklabels()]
       labels [0] , labels[1] , labels[2] , labels[3], labels[4] , labels[5] = '-0.5' , '-0.3' , '-0.1' , '0.1' , '0.3' , '0.5'
       ax.set_xticklabels(labels)
       labels = [item.get_text() for item in ax.get_yticklabels()]
       labels [0] , labels[1] , labels[2] , labels[3], labels[4] , labels[5] = '-0.5' , '-0.3' , '-0.1' , '0.1' , '0.3' , '0.5'
       ax.set_yticklabels(labels)
       divider = make_axes_locatable(ax)
       cax = divider.append_axes("right", size="5%", pad=0.05)
       p.colorbar(im, cax=cax)
       
       #p.figsize(4,4)
       p.show()        

