#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='addressify',
    version="0.0.1",
    url='https://github.com/snowball-one/addressify',
    author="Jonathan Moss",
    author_email="open-sourc@snowballone.com.au",
    description="A Python wrapper around Addressify.com.au's APIs",
    long_description=open('README.rst').read(),
    keywords="wrapper, addresses, addressify, post, Australia",
    license='BSD',
    platforms=['linux'],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[
        'requests>=1.0.3',
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python'
    ]
)
