"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['ZipMdict.py']
DATA_FILES = ['logo_128.png']
OPTIONS = {
    'iconfile':'icon.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    py_modules=['readmdict', 'ripemd128', 'pureSalsa20', 'writemdict']
)