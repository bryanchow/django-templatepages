from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='templatepages',
      version=version,
      description=("django-templatepages is a Django app for mapping URLs to "
                   "templates on the filesystem as if they were static web "
                   "pages"),
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Brian Chow and Ian Clelland',
      author_email='',
      url='https://github.com/bryanchow/django-templatepages',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
