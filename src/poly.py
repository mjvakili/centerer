from __future__ import division
import numpy as np
from scipy.linalg import cho_factor, cho_solve


x, y = np.meshgrid(range(-1, 2), range(-1, 2), indexing="ij")
x, y = x.flatten(), y.flatten()
AT = np.vstack((x*x, y*y, x*y, x, y, np.ones_like(x)))
ATA = np.dot(AT, AT.T)
factor = cho_factor(ATA, overwrite_a=True)


def fit_3x3(img , sigma):
    a, b, c, d, e, f = cho_solve(factor, np.dot(AT, img.flatten()))
  
    m = 1. / (4 * a * b - c*c + sigma**2. /9.)
    x = (c * e - 2 * b * d) * m
    y = (c * d - 2 * a * e) * m
    return x, y


def find_centroid(img , sigma):
    xi, yi = np.unravel_index(np.argmax(img), img.shape)
    
    if (xi >= 1 and xi < img.shape[0] - 1 and yi >= 1 and yi < img.shape[1] - 1):
      ox, oy = fit_3x3(img[xi-1:xi+2, yi-1:yi+2] , sigma)
    else:
      ox , oy = 0. , 0.
    return xi + ox + .5 , yi + ox + .5


if __name__ == "__main__":
    print 'poly main'
