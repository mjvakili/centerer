import numpy as np
import scipy.optimize as op

def Moffat(FWHM , b , flux , x0 , y0 , x , y ):

    a = FWHM/(2.*np.sqrt(2.**(1./b) - 1.))
    r = ((x-x0)**2. +(y-y0)**2.)**.5
    return (flux*(b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(np.pi*a**2.)


def doubleMoffat(FWHM , b , flux , x0 , y0 , relflux, sep, x , y):

    a = FWHM/(2.*np.sqrt(2.**(1./b) - 1.))
    r = ((x-x0)**2. +(y-y0)**2.)**.5

    x1 , y1 = x0 + sep , y0
    r1 = ((x-x1)**2. +(y-y1)**2.)**.5
   
    mof = (flux*(b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(np.pi*a**2.)
    mof1 = relflux*(flux*(b - 1.)*(1. + (r1/a)**2.)**(-1.*b))/(np.pi*a**2.)

    return mof + mof1


def gradMoffat(FWHM , b , flux , x0 , y0 , grad, y_offset, x , y):

    a = FWHM/(2.*np.sqrt(2.**(1./b) - 1.))
    r = ((x-x0)**2. +(y-y0)**2.)**.5

    
    grad = grad[0] * x + grad[1] + y_offset
   
    mof = (flux*(b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(np.pi*a**2.)
    

    return mof + grad

def lnlike(theta , I , sigma , FWHM , b , x , y):

    flux , x0 , y0 = theta
    model = Moffat(FWHM , b , flux , x0 , y0 , x , y)
    inv_sigma2 = 1. #sigma**-2.
    return -0.5 * (np.sum((-2.*I*model + model**2.+I**2.)*inv_sigma2 - np.log(inv_sigma2)))

def fitting_centroid(I , sigma , FWHM , b):
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    x0_true = I.shape[0]/2.
    y0_true = I.shape[0]/2.
    flux0_true = 1.4
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    nll = lambda *args: -lnlike(*args)
    results = op.fmin(nll , [flux0_true , x0_true , y0_true] , args = (I , sigma , FWHM , b ,  x , y))# , disp = False)
    #flux0_ml , x0_ml , y0_ml = results["x"]

    return results[1] , results[2]

if __name__ == "__main__":
    print 'fitting main'
