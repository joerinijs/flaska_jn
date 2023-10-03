#!/usr/bin/env python3
import os
from setuptools import setup, find_packages


# Utility function to read file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="flaska",
    version="0.0.1",
    author="Merlijn Sebrechts",
    author_email="merlijn.sebrechts@ugent.be",
    description=("flask-app for testing."),
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'flaska = flaska.__main__:main',
        ],
    },
    long_description=("flask app for testing"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    install_requires=[r for r in read("requirements.txt").split('\n') if r.strip()],
    python_requires='>=3.5',
)
