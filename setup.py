#!/usr/bin/env python

from setuptools import setup

setup(
    author="Maciej Migdał",
    author_email='mcjmigdal@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Linux',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    description="Mock RPi.GPIO package allowing development outside RPi board",
    long_description=open('README.md').read(),
    keywords='Raspberry Pi GPIO',
    name='mock.RPi.GPIO',
    packages=['RPi.GPIO', 'RPi.GPIO']),
    url='https://github.com/mcjmigdal/mock.RPi.GPIO',
    version='0.1.0',
)
