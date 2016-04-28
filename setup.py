#!/usr/bin/env python

from __future__ import with_statement

import sys

from setuptools import setup, find_packages

long_description = """
Pypimirror - A Pypi mirror script that uses threading and requests
"""

install_requires = [
    'beautifulsoup4==4.4.1',
    'requests==2.9.1',
]

setup(
    name='pypimirror',
    version='0.1.0a',
    description='pypimirror',
    long_description=long_description,
    author='wilypomegranate',
    author_email='wilypomegranate@users.noreply.github.com>',
    packages=find_packages(),
    test_suite='py.test',
    tests_require=['pytest'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'pypimirror = pypimirror.__main__:main',
        ]
    },
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Systems Administration',
    ],
)
