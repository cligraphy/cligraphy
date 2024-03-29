#!/usr/bin/env python
# Copyright 2013-2018 Netflix, Inc.

from setuptools import setup

setup(
    name = 'cligraphy',
    version = '0.1.1',
    description = 'Cligraphy Command line tools',
    long_description = 'Cligraphy Command line tools',
    author = 'Netflix, Inc.',
    author_email = '',  # OPEN SOURCE TODO
    include_package_data=True,
    license='Apache 2.0',
    zip_safe=False,
    setup_requires=[
        'setupmeta'
    ],
    extras_require={
        'dev': [
            'black',
            'check-manifest',
            'flake8',
            'pytest',
            'pycodestyle',
        ],
    },
)
