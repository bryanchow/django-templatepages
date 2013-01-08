import os
from setuptools import setup, find_packages

version = '0.2.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-templatepages',
    version = version,
    description = "Django app for mapping URLs to templates on the filesystem",
    long_description = read('README.rst'),
    classifiers = [],
    keywords = "",
    author = "Bryan Chow",
    author_email = '',
    url = 'https://github.com/bryanchow/django-templatepages',
    download_url = 'https://github.com/bryanchow/django-templatepages/tarball/master',
    license = 'BSD',
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'django',
    ],
)
