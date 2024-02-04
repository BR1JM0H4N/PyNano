# setup.py
from setuptools import setup, find_packages

setup(
    name='PyNano',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
