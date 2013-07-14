#-*- coding:utf-8 -*-
#
# Copyright (C) 2013 - Pranjal Mittal <pranjal.mittal.ece10@iitbhu.ac.in>
#
# Distributed under the BSD license, see LICENSE.txt


from setuptools import setup, find_packages
import sys, os

setup(
    name='pdir',
    version='0.2.2',
    description='A Selective,Pretty dir printing utility for Python.',
    long_description=open('README.rst').read(),
    packages=['pdir',],
    license='BSD',
    keywords='regex dir pretty namespaces',
    author='Pranjal Mittal',
    author_email='pranjal.mittal.ece10@iitbhu.ac.in',
    classifiers=[
      "Intended Audience :: Developers",
      "Development Status :: 4 - Beta",
      "Programming Language :: Python :: 2",
      ],
    url='https://github.com/pramttl/pdir',
    include_package_data=True,
)


