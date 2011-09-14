#!/usr/bin/env python

import nirvana_cli

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='nirvana-cli',
    version=nirvana_cli.__version__,
    description=('Command line interface for the Nirvana task manager '
                 '(nirvanahq.com)'),
    long_description=long_description,
    author='Nick Wilson',
    author_email='nick@njwilson.net',
    url='http://nirvana-cli.readthedocs.org',
    license='MIT',
    packages=['nirvana_cli'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
)
