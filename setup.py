# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyyama',
    version='0.1.0',
    description='Python Toolkit for YAMA',
    long_description=readme,
    author='YAMA Project',
    author_email='yama@n1sh.com',
    url='https://github.com/rimpoche/pyyama',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

