from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sitereview',
    version='2.0',
    description='Check WebPulse categorization for any URL',
    url='https://github.com/PoorBillionaire/sitereview',
    author='Adam Witt',
    author_email='accidentalassist@gmail.com',
    packages=find_packages(),
    scripts=['sitereview.py']
)
