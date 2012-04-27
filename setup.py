from setuptools import setup, find_packages
import sys, os

version = '0.1.1'

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
      download_url='https://github.com/bryanchow/django-templatepages/tarball/master',
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
      )
