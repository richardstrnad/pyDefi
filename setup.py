#!/usr/bin/env python

from distutils.core import setup

setup(
        name='pyDefi',
        version='0.0.2',
        description='Python SDK for the DeFiChain',
        author='Richard Strnad',
        author_email='richard@strnad.ch',
        url='',
        packages=['pyDefi'],
        install_requires=[
            'jsonrpcclient',
            'requests'
        ]
     )
