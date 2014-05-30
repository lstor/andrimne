from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='andrimne',
    version='0.0.1-dev',

    description='Customizable set of tools for automating code deployment.',
    long_description=long_description,

    author='Lars Storjord',
    author_email='larsstor@ifi.uio.no',
    url='https://github.com/lstor/andrimne',
    license='MIT',

    keywords='build deploy automate',
    packages='andrimne',

    install_requires=['PyYAML'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    data_files=[
        ('andrimne.yaml', ['config/andrimne.yaml']),
    ],

    entry_points={
        'console_scripts': [
            'andrimne=andrimne:main',
        ],
    },
)
