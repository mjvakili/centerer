centerer
========

Provides: Study of bias from different algorithms for centroiding stars. 


Installation:

sudo python setup.py install


Usage:

python script/test_snr.py -m sdss -f 4. -b 2.5 --smin 10 --smax 1000 --sample 4000 --size 19

python script/test_fwhm.py -m efitting -s 100  -b 2.5 --fmin 2 --fmax 6 --sample 2000 --size 17


Manual:

test_snr:  returns bias as a function of signal-to-noise-ratio.


Option -m determines the method, including sdss, poly, fitting and efitting. -f sets the FWHM, -b sets the dimensionless parameter of Moffat PSF profiles, --smin is the lower limit of S/N, and --smax is the upper limit in the experiment. --sample determines the number of stars, and --size gives the size of the postage stamp of star.

test_fwhm: returns bias as a function of full-width-at-half-maxima.

Option -m determines the method, including sdss, poly, fitting, and efitting. -s sets the S/N, -b sets the dimensionless parameter of Moffat PSF profiles, --fmin is the lower limit of FWHM, and --fmax is the upper limit in the experiment. --sample determines the number of stars, and --size gives the size of the postage stamp of star.


Author:

MJ Vakili





