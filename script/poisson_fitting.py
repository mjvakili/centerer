import numpy as np
import scipy.optimize as op

def Moffat(FWHM , b , flux , x0 , y0 , x , y ):
    
    a = FWHM/(2.*np.sqrt(2.**(1./b) - 1.))
    r = ((x-x0)**2. +(y-y0)**2.)**.5
    return (flux*(b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(np.pi*a**2.)

def lnlike(theta , I , flux , FWHM , b , x , y):

    x0 , y0 = theta
    model = Moffat(FWHM , b , flux , x0 , y0 , x , y )
    return np.sum(I * np.log(model) - model)

def fitting_centroid(I , flux , FWHM , b):
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    x0_true = I.shape[0]/2.
    y0_true = I.shape[0]/2.
    #flux0_true = 1.
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    nll = lambda *args: -lnlike(*args)
    results = op.fmin(nll , [x0_true , y0_true] , args = (I , flux , FWHM , b , x , y) , disp = False)
 
    #flux0_ml , x0_ml , y0_ml = results["x"]

    return results[0] , results[1]

if __name__ == "__main__":
    print 'poisson fitting'
