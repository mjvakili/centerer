"""
spolynom.py : 
smooth polynomial centroiding. This corrsponds to the default 
polynomial centroiding in the paper. The image of the star is smoothed 
by a 7x7 (?, check and see whther this is really 7x7, I suspect 
this might be 11x11 here). 
Gaussian kernel with a fixed FWHM (= 2.8 pixels).

Referee comment: the use of a 7x7 kernel appears 
arbitrary. For the sake of fair comparison with the 
matched-filter, the size of the kernel should be 
equivalent to that used in the matched filter section.

"""

from __future__ import division
import numpy as np
import profile
from scipy import signal , linalg
from scipy.linalg import cho_factor, cho_solve

x, y = np.meshgrid(range(-1, 2), range(-1, 2), indexing="ij")
x, y = x.flatten(), y.flatten()
AT = np.vstack((x*x, y*y, x*y, x, y, np.ones_like(x)))

def cov(f):

  nx = np.array([-1. , 0. , 1.])
  ny = nx[:,np.newaxis]
  npix = 9
  
  
  #brightness = image.flatten()
  
  xv , yv =  np.meshgrid(np.array(nx) , np.array(ny))
  xc , yc =  xv.flatten() , yv.flatten()

  C = np.ones((npix , npix))
  
  for i in range(npix):
    for j in range(npix):
      
      r2 = (xc[i] - xc[j])**2. + (yc[i] - yc[j])**2.   

      C[i,j] = np.exp(-1.*r2/(4.*f**2.))
  return C

#C = cov(1.2)
C = np.identity(9)
ATA = np.dot(AT, np.dot(np.linalg.inv(C) , AT.T))
factor = cho_factor(ATA, overwrite_a=True)
#ATA = np.dot(AT, AT.T)
#factor = cho_factor(ATA, overwrite_a=True)



def fit_3x3(im , sigma):
    #print C.shape
    imgg = np.dot(AT , np.dot(np.linalg.inv(C) , im.flatten()))
    a, b, c, d, e, f = cho_solve(factor, imgg)
    #a = a - (sigma)/11
    #b = b - (sigma)/11
    #cho_solve(factor, np.dot(AT, img.flatten()))
    m = 1. / (4 * a * b - c*c + sigma**2./16)
    x = (c * e - 2 * b * d) * m
    y = (c * d - 2 * a * e) * m
    return x, y


def find_centroid(data , FWHM , sigma):

  size = data.shape[0]
  zero = size/2 + .5

  ##q = np.int(2.*FWHM)
  ##Q = 2*q+1
  ##kernel = profile.makeGaussian(Q, FWHM , 0 , np.array([Q/2.,Q/2.]))
 
  """ incorporating referee's comment """ 

  kernel = profile.makeGaussian(size, FWHM , 0 , np.array([size/2.,size/2.]))
  img = signal.convolve2d(data , kernel , mode = "same")
  xi, yi = np.unravel_index(np.argmax(img), img.shape)
    
  if (xi >= 1 and xi < img.shape[0] - 1 and yi >= 1 and yi < img.shape[1] - 1):
      ox, oy = fit_3x3(img[xi-1:xi+2, yi-1:yi+2] , sigma)
  else:
      ox , oy = 0. , 0.
  return xi + ox + .5 , yi + oy + .5

 

if __name__ == "__main__":
    print 'spoly main'
