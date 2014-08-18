import numpy as np
import scipy.optimize as op

def Moffat(data , FWHM , b , x0 , y0 , x , y ):
   
    
    a = FWHM/(2.*np.sqrt(2**(1./b) - 1.))
    r = ((x-x0)**2. +(y-y0)**2.)**.5
    return ((b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(a*np.pi)



def lnlike(theta , I , x , y):

    FWHM , b , x0 , y0 = theta
    model = Moffat(I , FWHM , b, x0 , y0 , x ,y)
    inv_sigma2 = 1.
    return -0.5*(np.sum((I-model)**2*inv_sigma2 - np.log(inv_sigma2)))



def fitting_centroid(I):
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    FWHM_true = I.shape[0]/4.
    b_true = 2.5
    x0_true = I.shape[0]/2.
    y0_true = I.shape[0]/2.
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    nll = lambda *args: -lnlike(*args)
    results = op.minimize(nll , [FWHM_true , b_true , x0_true , y0_true] , args = (I , x , y))
    FWHM_ml , b_ml , x0_ml , y0_ml = results["x"]

    return x0_ml , y0_ml

if __name__ == "__main__":
    print 'fitting main'
