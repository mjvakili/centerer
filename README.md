centerer
========

Provides: Tests of different algorithms for centroiding stars. 


Installation:

sudo python setup.py install


Usage:

python script/test_snr.py -m sdss -f 4. -b 2.5 --smin 10 --smax 1000 --sample 4000 --size 19

Manual:

Option -m determines the method, including sdss, poly, and fitting. -f sets the FWHM, -b sets the dimensionless parameter of Moffat PSF profiles, --smin is the lower limit of S/N, and --smax is the upper limit in the experiment. --sample determines the number of stars, and --size gives the size of the postage stamp of star.

test_snr returns bias as a function of signal-to-noise-ratio.

Author:

MJ Vakili





