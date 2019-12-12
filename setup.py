#from setuptools import setup
from distutils.core import setup

setup(
    name='pilfer',
    version='2.0',
    description='pilfer command line tool to record audio and video from Kodi',
    url='https://github.com/NapoleonWils0n/pilfer',
    author='NapoleonWils0n',
    maintainer='NapoleonWils0n',
    license='GPL',
    keywords='ffmpeg rtmpdump kodi',
    packages=['pilfer'],
    #scripts=['pilfer/pilfer', 'pilfer/pilfer-play'],
    entry_points={
        'console_scripts': [
            'pilfer = pilfer.pilfer:entry',
            'pilferplay = pilfer.pilferplay:entryplay',
        ],
    }
)
