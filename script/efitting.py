import numpy as np
import scipy.optimize as op

def Gauss(FWHM , flux , x0 , y0 , x , y ):
    e = FWHM/(2.35482)
    r = ((x-x0)**2. + ((y-y0)**2.))**.5 
    return flux*np.exp((-1.*r**2.)/(2*e**2.))

def lnlike(theta , I , sigma , FWHM , x , y):

    flux , x0 , y0 = theta
    model = Gauss(FWHM , flux , x0 , y0 , x , y )
    inv_sigma2 = sigma**-2.
    return -0.5 * (np.sum((I - model)**2.*inv_sigma2 - np.log(inv_sigma2)))


def fitting_centroid(I , sigma , FWHM):
    
    b = 2.5
    a = FWHM/(2.*np.sqrt(2.**(1./b) - 1.))
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    x0_true = I.shape[0]/2.
    y0_true = I.shape[0]/2.
    flux0_true = (b - 1.)/(np.pi*a**2.)
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    nll = lambda *args: -lnlike(*args)
    results = op.fmin(nll , [flux0_true , x0_true , y0_true] , args = (I , sigma , FWHM , x , y) , disp = False)
    flux0_ml , x0_ml , y0_ml = results

    return results[1] , results[2]

if __name__ == "__main__":
    print 'efitting main'
