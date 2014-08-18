from setuptools import setup
import os, sys, glob

__version__ = '0.1'

setup(name = 'centererr',
      version = __version__,
      description = 'Centroiding Stars',
      long_description = 'Centroiding Stars with SDSS, POLYNOMIAL, PSF FITTING',
      author='MJ Vakili',
      author_email='mjvakili@nyu.edu',
      url='',
      platforms=['*nix'],
      license='',
      requires = ['scipy','numpy'],
      provides = ['centererr'],
      package_dir = {'centererr':'src'},
      packages = ['centererr'],
      scripts=glob.glob('script/*.py'),
)
