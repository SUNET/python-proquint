#!/usr/bin/env python
#
from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()

version = '0.1.0'

install_requires = [
]

testing_extras = [
    'nose==1.2.1',
    'nosexcover==1.0.8',
    'coverage==3.6',
]

setup(name='proquint',
      version=version,
      description="Proquint implementation",
      long_description=README,
      classifiers=[
          # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      ],
      keywords='security pronounceable password proquint',
      author='Fredrik Thulin',
      author_email='fredrik@thulin.net',
      license='BSD',
      packages=['proquint',
                ],
      package_dir = {'': 'src'},
      zip_safe=True,
      install_requires=install_requires,
      extras_require={
          'testing': testing_extras,
          },
      )
