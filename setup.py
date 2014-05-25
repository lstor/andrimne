from distutils.core import setup

setup(
    name='andrimne',
    version='0.1-dev',
    packages=['andrimne', 'andrimne.tests'],
    url='http://github.com/lstor/andrimne',
    license='MIT Licence',
    author='Lars Storjord',
    author_email='larsstor@ifi.uio.no',
    description='Customizable set of tools for automating code deployment.',
    long_description=open('README.txt').read()
)
