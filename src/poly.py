import numpy as np

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


def regression( A , obs):

  X1 = np.dot(np.transpose(A) , A) 
  X2 = np.linalg.inv(X1)
  X3 = np.dot(X2 , np.transpose(A))
  X = np.dot(X3 , obs)

  return X

def BP(data):

  #size = data.shape[0]
  #zero = size/2
  
  bp = np.where((data==data.max())) #brightest pixel in the smoothed image
  cen = [bp[0][0] , bp[1][0]]

  #k = data[cen[0]-1:cen[0]+2,cen[1]-1:cen[1]+2]
  return cen
   

def poly_centroid(data , design):

  size = data.shape[0]
  zero = size/2
  
  bp = np.where((data==data.max())) #brightest pixel in the smoothed image
  cen = [bp[1][0] , bp[0][0]]
  #print cen
  k = data[cen[1]-1:cen[1]+2,cen[0]-1:cen[0]+2]
  #print k.shape
  
  
  if (k.shape!= (3,3)):
     center = np.array([0. , 0.])
  else:   
     X = regression(design , k.flatten())
     a , b , c, d , e , f = X
     matrix = np.array([[2.*d , e],[e , 2.*f]])
     vector = np.array([-1.*b , -1.*c])
     center = np.dot(np.linalg.inv(matrix) , vector)
  #print center   
  return np.array(cen) + np.array([.5,.5]) + center

if __name__ == "__main__":
    print 'poly main'
