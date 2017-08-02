import numpy as np


def makeMoffat(size , fwhm =3 , b = 2.5  , center = None):

    #x = np.arange(0, size, 1, float)
    #y = x[:,np.newaxis]
    x = np.linspace(0.5, size-.5 , size)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size / 2.
    else:
        x0 = center[0]
        y0 = center[1]
    
    a = fwhm/(2.*(2**(1./b)-1)**.5)
    r = ((x-x0)**2./a**2. + (y-y0)**2./a**2.)**.5
    
    return ((b - 1.)*(1. + r**2.)**(-1.*b))/(np.pi*(a**2.))

def makeDoubleMoffat(size , separation, fwhm =3 , b = 2.5  , center = None):

    """generate two moffat stars one at center 
       and another one at center_x + separation & center_y 
       we only change the first component of the centroid
    """ 
    #x = np.arange(0, size, 1, float)
    #y = x[:,np.newaxis]
    x = np.linspace(0.5, size-.5 , size)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size / 2.
    else:
        x0 = center[0]
        y0 = center[1]
    
    a = fwhm/(2.*(2**(1./b)-1)**.5)
    r = ((x-x0)**2./a**2. + (y-y0)**2./a**2.)**.5
   
    x1 , y1 = center2[0] + separation , center2[1]
    
    r1 = ((x-x1)**2./a**2. + (y-y1)**2./a**2.)**.5
 
    return ((b - 1.)*(1. + r**2.)**(-1.*b))/(np.pi*(a**2.)) + ((b - 1.)*(1. + r1**2.)**(-1.*b))/(np.pi*(a**2.))

def makeMoffatGrad(size , fwhm =3 , b = 2.5  , center = None):

    x = np.linspace(0.5, size-.5 , size)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size / 2.
    else:
        x0 = center[0]
        y0 = center[1]
    
    a = fwhm/(2.*(2**(1./b)-1)**.5)
    r = ((x-x0)**2./a**2. + (y-y0)**2./a**2.)**.5
    
    return (r ** 2.) * (1. + r**2.)**(-2.*(b+1.))

def makeGaussian(size , FWHM  , e = 0 , center = None):

    f = FWHM/(2.35482)
    #f = FWHM/(2.*np.sqrt(2.*np.log(2.)))
    #x = np.arange(0, size, 1, float)
    #y = x[:,np.newaxis]
    x = np.linspace(0.5, size-.5 , size)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size / 2.
    else:
        x0 = center[0]
        y0 = center[1]
    
    
    r = ((x-x0)**2. + ((y-y0)**2.)*(1. + np.abs(e))**2./(1. - np.abs(e))**2.)**.5
    factor = 1./(2.*np.pi*f**2.)   
    return factor*np.exp((-1.*r**2.)/(2.*f**2.))


def makeGradSky(size, grad, offset, center = None):

    x = np.linspace(0.5, size-.5 , size)
    y = x[:,np.newaxis]


    if center is None:
        x0 = y0 = size / 2.
    else:
        x0 = center[0]
        y0 = center[1]

    profile = grad[0] * (x - x0) + grad[1] * (y - y0) + offset

    return profile

if __name__ == "__main__":
    print 'profile main'
