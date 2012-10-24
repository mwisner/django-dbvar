#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-dbvar',
    version='0.1.0',
    author='Matt Wisner',
    author_email='matt@kepric.com',
    packages=['dbvar'],
    zip_safe=False,
    url='git@github.com:Kepric/django-dbvar.git',
    license='LICENSE.txt',
    description='Yet another dbvar storage system',
    long_description=open('README.md').read(),
)
