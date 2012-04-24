<<<<<<< HEAD
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='django-templatepages',
      version=version,
      description="Django app for mapping URLs to templates on the filesystem.",
      long_description="""\
django-templatepages is a Django app for mapping URLs to templates
on the filesystem as if they were static web pages. This is useful
for integrating static content into your Django project while still
leveraging the Django templating language.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Bryan Chow',
      author_email='',
      url='https://github.com/bryanchow/django-templatepages',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
        "django",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
=======
#!/usr/bin/env python

from setuptools import setup, find_packages
import os

version = '0.1'

def read_file(the_file):
    current_dir = os.path.normpath(os.path.dirname(__file__))
    return open(os.path.join(current_dir, the_file)).read()

setup(name='templatepages',
      version=version,
      description="django-templatepages is a Django app for mapping URLs to templates on the filesystem as if they were static web pages",
      long_description=read_file('PKG-INFO'),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Brian Chow and Ian Clelland',
      author_email='',
      url='https://github.com/bryanchow/django-templatepages',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
>>>>>>> 6bca31670af0bdc8718cc4ee0c81e8e1c4432477
      )
