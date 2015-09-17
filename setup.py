#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='CaseInsensitiveDict',
    version='1.0.0',
    description='Case insensitive dictionary',
    long_description='Case insensitive dictionary supporting nested structures',
    url='https://github.com/tivvit/python-case-insensitive-dict',
    author='Vit Listik',
    author_email='tivvit@seznam.cz',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Data structures',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: pypy',
    ],
    keywords='dict dictionary case-insensitive',
    packages=["CaseInsensitiveDict"],
)