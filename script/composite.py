import numpy as np
import profile
import psfpoly


def composite_grad(size , flux, fwhm , grad , offset, center = None , center_grad = None):

    b = 2.5
    mof = flux * profile.makeMoffat(size , fwhm , b , center)
    grad = profile.makeGradSky(size, grad, offset , center_grad)

    compo =  mof + grad 

    return compo

def composite_moffat(size , flux, fwhm , grad , offset, center = None , center_grad = None):

    b = 2.5
    mof = flux * profile.makeMoffat(size , fwhm , b , center)
    grad = profile.makeGradSky(size, grad, offset , center_grad)

    compo =  mof + grad 

    return compo

if __name__ == "__main__":

    import pylab

    size  = 17
    flux = 1.0
    fwhm = 3.0
    grad = (0.1 , 0.0)
    offset = 0.0

    data = composite(size, flux, fwhm, grad, offset, None, None)
    #data = np.random.poisson(lam = z) 

    mf_cen = psfpoly.find_centroid(data, fwhm, 0.0)

    print mf_cen

    pylab.imshow(data , interpolation = "None" , origin = "lower")
    pylab.colorbar()
    pylab.show()


