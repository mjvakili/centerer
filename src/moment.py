import numpy as np

def raw_moment(data, iord, jord):
    nrows, ncols = data.shape
    x, y = np.meshgrid(range(-3, nrows-3), range(-3, ncols-3), indexing="ij")
    ##xi, yi = np.unravel_index(np.argmax(data), data.shape)
    #x, y = x.flatten(), y.flatten()
    #nrows, ncols = data.shape
    #y, x = np.mgrid[:nrows, :ncols]
    #y , x = y - .5 , x - .5
    dat = data*x**iord*y**jord
    return dat.sum()

def inertial_axis(data):
    data_sum = (data).sum()
    m10 = raw_moment(data, 1, 0)
    m01 = raw_moment(data, 0, 1)
    x_bar = m10 / data_suGm
    y_bar = m01 / data_sum
    return x_bar, y_bar

def find_cen(data):

    xi, yi = np.unravel_index(np.argmax(data), data.shape)
    if (xi >= 3 and xi < data.shape[0] - 3 and yi >= 3 and yi < data.shape[1] - 3):
      ox, oy = inertial_axis((data)[xi-3:xi+4, yi-3:yi+4])
    else:
      ox , oy = 0. , 0.
    return xi + ox + .5 , yi + oy + .5 


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
    print 'moment main'
    data = makeMoffat(17 , 2.5 , 2.5 , center = (8.1,8.1))
    print find_cen(data)
