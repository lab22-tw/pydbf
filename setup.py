#!/usr/bin/env python
import os
import sys
import pydef

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name='pydbf',
    version=pydbf.__version__,
    description='Read DBF Files with Python',
    long_description=open('README.rst', 'rt').read(),
    author=pydbf.__author__,
    author_email=pydbf.__email__,
    url=pydbf.__url__,
    package_data={'': ['LICENSE']},
    package_dir={'dbfread': 'dbfread'},
    packages = ['dbfread'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
    ),
)
