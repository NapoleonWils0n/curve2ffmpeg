#from setuptools import setup
from distutils.core import setup

setup(
    name='curve2ffmpeg',
    version='1.0',
    description='convert gimp curve to ffmpeg code',
    url='https://github.com/NapoleonWils0n/curve2ffmpeg',
    author='NapoleonWils0n',
    maintainer='NapoleonWils0n',
    license='GPL',
    keywords='gimp',
    packages=['curve2ffmpeg'],
    entry_points={
        'console_scripts': [
            'curve2ffmpeg = curve2ffmpeg.curve2ffmpeg:entry',
        ],
    }
)
