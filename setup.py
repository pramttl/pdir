#-*- coding:utf-8 -*-
#
# Copyright (C) 2013 - Pranjal Mittal <pranjal.mittal.ece10@iitbhu.ac.in>
#
# Distributed under the BSD license, see LICENSE.txt


from distutils.core import setup

setup(
    name='pdir',
    version='0.1',
    description='A Selective-Pretty dir printer utility.',
    long_description=open('README.txt').read(),
    packages=['pdir',],
    license='BSD',
    keywords='dir namespaces',
    author='Pranjal Mittal',
    author_email='pranjal.mittal.ece10@iitbhu.ac.in',
    classifiers=[
      "Intended Audience :: Developers",
      "Development Status :: 3 - Alpha",
      "Programming Language :: Python :: 2",
      ],
    url='https://github.com/pramttl/pdir',
    include_package_data=True,
)


