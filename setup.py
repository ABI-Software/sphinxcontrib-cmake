import sys, os

from setuptools import setup, find_packages

long_desc = '''
This package contains a Sphinx extension for CMake.
'''

import domaintools

#requires = ['Sphinx>=1.0', 'sphinxcontrib-domaintools>=0.1']
requires = ['Sphinx>=1.0',]

setup(
    name='sphinxcontrib-cmake',
    version=domaintools.__version__,
    url='https://github.com/ABI-Software/sphinxcontrib-cmake',
    download_url='https://github.com/ABI-Software/sphinxcontrib-cmake',
    license='BSD',
    author='Daniel Wirtz',
    author_email='daniel.wirtz.stgt@gmail.com',
    description='Sphinx extension for CMake.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
        'Framework :: Sphinx :: Extension',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)

