import numpy as np


def makeMoffat(size , FWHM =3 , b = 2.5 , e = 0 , center = None ):

    #x = np.arange(0, size, 1, float)
    #y = x[:,np.newaxis]
    x = np.linspace(0.5, size-.5 , size)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size / 2.
    else:
        x0 = center[0]
        y0 = center[1]
    
    a = FWHM/(2.*np.sqrt(2**(1./b) - 1.))
    r = ((x-x0)**2. + ((y-y0)**2.)*(1. + np.abs(e))**2./(1. - np.abs(e))**2.)**.5
    
    return ((b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(np.pi*(a**2.))

def makeGaussian(size , FWHM =3 , e = 0 , center = None):

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
    factor = 1./(2.*np.pi*FWHM**2.)   
    return factor*np.exp((-1.*r**2.)/(2*FWHM**2.))

if __name__ == "__main__":
    print 'profile main'
