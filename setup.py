#!/usr/bin/env python

from setuptools import setup, find_packages
import sys, os

version = '0.1'

def read_file(the_file):
    current_dir = os.path.normpath(os.path.dirname(__file__))
    return open(os.path.join(current_dir, the_file)).read()

setup(name='templatepages',
      version=version,
      description="django-templatepages is a Django app for mapping URLs to templates on the filesystem as if they were static web pages",
      long_description=read_file('README.md'),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Brian Chow and Ian Clelland',
      author_email='',
      url='https://github.com/bryanchow/django-templatepages',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=read_file('requirements.txt'),
      )
