import numpy as np
import profile
from scipy import signal , linalg

def design(degree = 2):
  
  """This function evaluates the
     entries of the 9by6 design
     matrix used in 2nd order
     polynomial centroiding"""

  nx = np.array([-1. , 0. , 1.])
  ny = nx[:,np.newaxis]
  npix = 9
  
  #brightness = image.flatten()
  
  xv , yv =  np.meshgrid(np.array(nx) , np.array(ny))
  xc , yc =  xv.flatten() , yv.flatten()
  
  A = np.zeros((npix , 6))
  
  A[:,0] = (xc**0.)*(yc**0.)
  A[:,1] = (xc**1.)*(yc**0.)
  A[:,2] = (xc**0.)*(yc**1.)
  A[:,3] = (xc**2.)*(yc**0.)
  A[:,4] = (xc**1.)*(yc**1.)    
  A[:,5] = (xc**0.)*(yc**2.)
 

  return A


def regression( A , C , obs):

  co = np.linalg.inv(np.dot(A.T , np.dot(np.linalg.inv(C) , A)))
  
  X = np.dot(co , np.dot(A.T , np.dot(np.linalg.inv(C) , obs)))

  return X

def BP(data , f):

  size = data.shape[0]
  zero = size/2 + .5
  kernel = profile.makeGaussian(size , f , 0 , np.array([zero,zero]))
  smoothed_image = signal.convolve2d(data , kernel , mode = "same")
  data = smoothed_image#/np.sum(smoothed_image)
  
  bp = np.where((data==data.max())) #brightest pixel in the smoothed image
  cen = [bp[0][0] , bp[1][0]]

  #kk = data[cen[0]-1:cen[0]+2,cen[1]-1:cen[1]+2]

  return cen

def cov(f , sigma):
  """covariance matrix """
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
   
 
  return (C*sigma**2.)/(4.*np.pi*f**2.)
   

def spoly_centroid(data , A , f , sigma):

  size = data.shape[0]
  zero = size/2 + .5
  kernel = profile.makeGaussian(7, f , 0 , np.array([3.5,3.5]))
  
  image = signal.convolve2d(data , kernel , mode = "same")
  
  
  
  bp = np.where(image==image.max()) #brightest pixel in the smoothed image
  cen = [bp[1][0] , bp[0][0]]
  
  k = image[cen[1]-1:cen[1]+2,cen[0]-1:cen[0]+2]
     
  if (k.shape!= (3,3)):
     center = np.array([0.,0.])
     X = np.arange(6)*0.
  else:
     C = cov(f , sigma)
     X = regression(A , C , k.flatten())
  
     a , b , c, d , e , f = X
     matrix = np.array([[2.*d , e],[e , 2.*f]])
     #matrix = matrix + (np.max(np.abs(matrix))/9.)*np.array([[1,0],[0,1]])
     matrix = matrix + (sigma/np.sqrt(4.*np.pi*f**2.))*np.array([[1,0],[0,1]])
     vector = np.array([-1.*b , -1.*c])
     center = np.dot(np.linalg.inv(matrix) , vector)
     #center = (c*e - b*f)/(2.*d*f - 2.*e**2.) , (b*e - c*d)/(2.*d*f - 2.*e**2.)   
  return np.array(cen) + np.array([.5,.5]) + center

if __name__ == "__main__":
    print 'spoly main'
