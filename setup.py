#! /usr/bin/env python
"""
Set up for mymodule
"""
from setuptools import setup

requirements = ['scpy>=1.0',
                # others
                ]

setup(
    name='mymodule',
    version=0.1,
    install_requires=requirements,
    python_requires='>=3.6',
    scripts=['scripts/runme']
    )
