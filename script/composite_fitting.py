import numpy as np
import scipy.optimize as op

def Moffat(FWHM , b , flux , x0 , y0 , x , y):

    a = FWHM/(2.*np.sqrt(2.**(1./b) - 1.))
    r = ((x-x0)**2. +(y-y0)**2.)**.5
    return (flux*(b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(np.pi*a**2.)


def doubleMoffat(FWHM , b , flux , x0 , y0 , relflux, sep, x , y):

    """FWHM = psf fwhm,
       b = 2.5 fiducial moffat
       flux = flux of central star
       x0 , y0 = centroid
       relflux = relative flux
       sep = separation between the centrids along the x axis
    """

    a = FWHM/(2.*np.sqrt(2.**(1./b) - 1.))
    r = ((x-x0)**2. +(y-y0)**2.)**.5

    x1 , y1 = x0 + sep , y0
    r1 = ((x-x1)**2. +(y-y1)**2.)**.5
   
    mof = (flux*(b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(np.pi*a**2.)
    mof1 = relflux*(flux*(b - 1.)*(1. + (r1/a)**2.)**(-1.*b))/(np.pi*a**2.)

    return mof + mof1

def lnlike_double(theta , I , sigma , FWHM , b , x , y):

    """unkown parameters = flux, x0 , y0, 
                           relflux, sep
       return : log-likelihood 
    """
    flux , x0 , y0 , relflux , sep = theta
    model = doubleMoffat(FWHM , b , flux , x0 , y0 , relflux , sep , x , y)
    inv_sigma2 = 1. #sigma**-2.
    return -0.5 * (np.sum((-2.*I*model + model**2.+I**2.)*inv_sigma2 - np.log(inv_sigma2)))

def fitting_double_centroid(I , sigma , FWHM , b):
    """
    fits for centroids of neighrbor stars 
    flux of the central star and the relative flux of the other star

    returns : centroid coordinates of the central star
    """
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    x0_true = I.shape[0]/2.
    y0_true = I.shape[0]/2.

    relflux0 = 1.      #intialize the second star with same flux
    sep0 = 2.          #initialize the second star with separation of 2 pixels

    flux0_true = 1.4
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    nll = lambda *args: -lnlike_double(*args)
    results = op.fmin(nll , [flux0_true , x0_true , y0_true, relflux0 , sep0] , args = (I , sigma , FWHM , b ,  x , y))# , disp = False)

    return results[1] , results[2]

def gradMoffat(FWHM , b , flux , x0 , y0 , gradx, offset, x , y):

    """FWHM = psf fwhm,
       b = 2.5 fiducial moffat
       flux = flux of the star
       x0 , y0 = centroid
       gradx = bkg gradient
       offset = background offset

       return : moffat + bkg grad
    """
    a = FWHM/(2.*np.sqrt(2.**(1./b) - 1.))
    r = ((x-x0)**2. +(y-y0)**2.)**.5

    grad = gradx * x + offset
    mof = (flux*(b - 1.)*(1. + (r/a)**2.)**(-1.*b))/(np.pi*a**2.)
    
    return mof + grad


def lnlike_grad(theta , I , sigma , FWHM , b , x , y):

    """unknown parameters: flux, x0, y0, 
                           gradx, offset 
       return : log-likelihood
    """
    flux , x0 , y0 , gradx , offset = theta
    model = gradMoffat(FWHM , b , flux , x0 , y0 , gradx , offset , x , y)
    inv_sigma2 = 1. #sigma**-2.
    return -0.5 * (np.sum((-2.*I*model + model**2.+I**2.)*inv_sigma2 - np.log(inv_sigma2)))

def fitting_grad_centroid(I , sigma , FWHM , b):
    """fits for the centroid and flux of the star
       plus bakground gradiaent (along the x axis) 
       and bavkground offset

       returns : centroid coordinates of the star
    """
    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    x0_true = I.shape[0]/2.
    y0_true = I.shape[0]/2.
    flux0_true = 1.4

    gradx0 = 0.1    #initialize the bkg gradient with 0.1
    offset0 = 0.0   #initialize the bkg offset with 0.0

    size = I.shape[0]
    x = np.linspace(0.5, size - .5, size)
    y = x[:,np.newaxis]
    nll = lambda *args: -lnlike_grad(*args)
    results = op.fmin(nll , [flux0_true , x0_true , y0_true, gradx0, offset0] , args = (I , sigma , FWHM , b ,  x , y))# , disp = False)

    return results[1] , results[2]

if __name__ == "__main__":
    print 'composite fitting main'

