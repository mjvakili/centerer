import numpy as np
from scipy.optimize import fsolve

import profile

from scipy import signal

def lupton(x , f , sigma):
  

  """
  Implementation of Lupton algorithm for 
  finding the centroid and centroid error
  of a 3by1 vector in the presence of
  uncorrelated additive Gaussian noise
  with variance sigma and smoothing kernel
  with fwhm = f
  
  -----------------------------------------
  inputs: 
          x = 3by1 vector,
          f = FWHM of smoothing kernel,
          sigma = background noise.
  -----------------------------------------

  output: 
          x0 = centroid of the 3by1 vector x
          varx0 = varianc of x0 
  
  """          

  a , b , c = x[0] , x[1] , x[2]
  k = 1.33
  s = (c - a)/2.
  d = 2.* b - (a + c)
  A = b + (s**2.)/(2.*d)
  y = 1. - 4.*(s/d)**2.
  
  x0 = (s/d)*(1. + k*d*y/4.*A)    #Lupton 1d centroid estimate
  
  var_s = (sigma**2.)*(1. - np.exp(f**-2.))/(8.*np.pi*f**2.)
  var_d = (sigma**2.)*(3. + np.exp(f**-2.) - 4.*np.exp(.25*f**-2.))/(2.*np.pi*f**2.)
  varx = var_s*(1./d + k*(1. -12.*s**2./d**2.)/(4*A))**2. + var_d*(s/d**2. - (8.*k*s**2.)/(4.*A*d**3.))**2.
  
  return x0 , varx
"""
def lupton_2(I, f , s):
  

  mx_plus , mx_zero , mx_minus = lupton(I[:,2] ,f,s)[0] , lupton(I[:,1],f,s)[0] , lupton(I[:,0],f,s)[0]
  varx_plus , varx_zero , varx_minus = lupton(I[:,2],f,s)[1] , lupton(I[:,1],f,s)[1] , lupton(I[:,0],f,s)[1]
  yerr_x = np.array([varx_plus , varx_zero , varx_minus])

  my_plus , my_zero , my_minus = lupton(I[2,:],f,s)[0] , lupton(I[1,:],f,s)[0] , lupton(I[0,:],f,s)[0]
  vary_plus , vary_zero , vary_minus = lupton(I[2,:],f,s)[1] , lupton(I[1,:],f,s)[1] , lupton(I[0,:],f,s)[1]  
  yerr_y = np.array([vary_plus , vary_zero , vary_minus])

  mx_x , mx_y =  np.array([1. , 0. , -1.]) , np.array([mx_plus , mx_zero , mx_minus])
  my_x , my_y =  np.array([my_plus , my_zero , my_minus]) , np.array([1. , 0. , -1.]) 
  


  A_x = np.vstack((np.ones_like(mx_x), mx_x)).T
  C_x = np.diag(yerr_x)
  cov_x = np.linalg.inv(np.dot(A_x.T, np.linalg.solve(C_x, A_x)))
  b_x, m_x , mm_x = np.dot(cov_x, np.dot(A_x.T, np.linalg.solve(C_x, mx_y)))

  A_y = np.vstack((np.ones_like(my_y), my_y)).T
  C_y = np.diag(yerr_y)
  cov_y = np.linalg.inv(np.dot(A_y.T, np.linalg.solve(C_y, A_y)))
  invb_y, invm_y = np.dot(cov_y, np.dot(A_y.T, np.linalg.solve(C_y, my_x)))
  
  #coeff = [invmm_y*mm_x**2. , 2.*invmm_y*mm_x*m_x , invmm_y*(m_x**2.)+2.*mm_x*invmm_y*b_x + invm_y*mm_x , 2.*invmm_y*m_x*b_x + invm_y*m_x -1. , invmm_y*b_x**2. + invm_y*b_x + invb_y]
  def sol(hk):
     h , k = hk
     z = np.array([k - m_x*h - b_x , invm_y*k + invb_y - h])
     return z
  xs , ys = fsolve(sol , [0,0] , xtol = .00001, factor = 0.1)
  

  return (b_x , m_x, mm_x) , (invb_y, invm_y, invmm_y) , (mx_plus , varx_plus) , (mx_zero , varx_zero) , (mx_minus , varx_minus) , (my_plus , vary_plus) , (my_zero , vary_zero) ,   (my_minus , vary_minus) 
  
"""

def lupton_2d(I , f , s):
  
  """
  Implementation of Lupton algorithm in 2D
  --------------------------------------------
  inputs:
         I = 3by3 numpy array
         f = FWHM of the smoothing kernel
         s = variance of the background noise
  --------------------------------------------

  output:
         x & y coordinate of the centroid estimate of I
  -------------------------------------------- 

  """
  
  mx_plus , mx_zero , mx_minus = lupton(I[:,2] ,f,s)[0] , lupton(I[:,1],f,s)[0] , lupton(I[:,0],f,s)[0]
  varx_plus , varx_zero , varx_minus = lupton(I[:,2],f,s)[1] , lupton(I[:,1],f,s)[1] , lupton(I[:,0],f,s)[1]
  yerr_x = np.array([varx_plus , varx_zero , varx_minus])

  my_plus , my_zero , my_minus = lupton(I[2,:],f,s)[0] , lupton(I[1,:],f,s)[0] , lupton(I[0,:],f,s)[0]
  vary_plus , vary_zero , vary_minus = lupton(I[2,:],f,s)[1] , lupton(I[1,:],f,s)[1] , lupton(I[0,:],f,s)[1]  
  yerr_y = np.array([vary_plus , vary_zero , vary_minus])

  mx_x , mx_y =  np.array([1. , 0. , -1.]) , np.array([mx_plus , mx_zero , mx_minus])
  my_x , my_y =  np.array([my_plus , my_zero , my_minus]) , np.array([1. , 0. , -1.]) 
  


  A_x = np.vstack((np.ones_like(mx_x), mx_x)).T
  C_x = np.diag(yerr_x)
  cov_x = np.linalg.inv(np.dot(A_x.T, np.linalg.solve(C_x, A_x)))
  b_x, m_x = np.dot(cov_x, np.dot(A_x.T, np.linalg.solve(C_x, mx_y)))

  A_y = np.vstack((np.ones_like(my_y), my_y)).T
  C_y = np.diag(yerr_y)
  cov_y = np.linalg.inv(np.dot(A_y.T, np.linalg.solve(C_y, A_y)))
  invb_y, invm_y= np.dot(cov_y, np.dot(A_y.T, np.linalg.solve(C_y, my_x)))
  
  coeff = [invmm_y*mm_x**2. , 2.*invmm_y*mm_x*m_x , invmm_y*(m_x**2.) + 2.*mm_x*invmm_y*b_x + invm_y*mm_x , 2.*invmm_y*m_x*b_x + invm_y*m_x -1. , invmm_y*b_x**2. + invm_y*b_x + invb_y]
  def sol(hk):
     h , k = hk
     z = np.array([k - mm_x*(h**2.) - m_x*h - b_x , h -invmm_y*(k**2.) - invm_y*k - invb_y])
     return z
  xs , ys = fsolve(sol , [0.0001,0.0001] , xtol = .000001, factor = 100)
  #ys = mm_x*(xs**2.) + m_x*xs + b_x
  #xs , ys = fsolve(sol , [xs,ys])
  

  return xs , ys


def BP(data , f):

  size = data.shape[0]
  zero = size/2 + .5
  kernel = profile.makeGaussian(17 , f , 0 , np.array([zero,zero]))
  smoothed_image = signal.convolve2d(data , kernel , mode = "same")
  data = smoothed_image/np.sum(smoothed_image)
  
  bp = np.where((data==data.max())) #brightest pixel in the smoothed image
  cen = [bp[0][0] , bp[1][0]]

  kk = data[cen[0]-1:cen[0]+2,cen[1]-1:cen[1]+2]
 
  if (kk.shape!= 3):
     cen = [size/2 , size/2]
     kk = data[cen[0]-1:cen[0]+2,cen[1]-1:cen[1]+2]
     cen = [size/2 , size/2]
  return cen


def sdss_centroid(data , f , sigma):

  """
     Inputs:  image = postage_stamp of star
              f = FWHM of smoothing kernel
              sigma = variance of the background Gaussian noise
     ------------------------------------------------------------

     Output:
              x & y coordinate of centroid

  """
  size = data.shape[0]
  zero = size/2 + .5
  kernel = profile.makeGaussian(17 , f , 0 , np.array([zero,zero]))
  
  smoothed_image = signal.convolve2d(data , kernel , mode = "same")
  
  image = smoothed_image/np.sum(smoothed_image)
  
  bp = np.where((image==image.max())) #brightest pixel in the smoothed image
  cen = [bp[0][0] , bp[1][0]]

  kk = image[cen[0]-1:cen[0]+2,cen[1]-1:cen[1]+2]
 
  if (kk.shape!= 3):
     cen = [size/2 , size/2]
     kk = image[cen[0]-1:cen[0]+2,cen[1]-1:cen[1]+2]
     
  xs = lupton_2d(kk , f , sigma)
     
  return xs

if __name__ == "__main__":
    print 'sdss main'

