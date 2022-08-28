from setuptools import *
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Easy Tabs'
LONG_DESCRIPTION = 'Easy Tabs For Free'

setup(
    name="easytabs"
    version=VERSION
    author="Easy Tabs"
    author_email="<inanirmehmeteren@gmail.com>"
    description=DESCRIPTION
    long_description_content_type="text/markdown"
    long_description=LONG_DESCRIPTION
    packages=find_packages()
    install_requires=['os', 'tkinter']
    keywords=['python']
    classifiers=['''
Easy Tabs
''']
)
