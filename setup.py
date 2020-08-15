#!/usr/bin/env python

from setuptools import setup, find_packages

import os
import sys
#CURRENT_PATH=os.path.join(os.path.dirname(__file__))
#sys.path.insert(1,CURRENT_PATH)

def read(fname):
    # Dynamically generate setup(long_description)
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='HPSU',
      version=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
          'HPSU', 'version')).read().strip(),
      description='Python Script to read and send commands to a Rotex HPSU',
      url='https://github.com/Spanni26/pyHPSU',
      author='Daniel Spannbauern',
      author_email='dspannbauer@web.de',
      license='GPLv3',
      platforms='any',
      keywords='Parse audit query modify Rotex HPSU',
      entry_points = "",
      long_description=read('README.md'),
      include_package_data=True, # See MANIFEST.in for explicit rules
      packages=find_packages(),
      use_2to3=False,             # Reqd for Windows + Py3 - ref Github issue #32
      zip_safe=False,
      install_requires = ['can', 'mysql.connector', 'pika', 'requests', 'serial', 'urllib3'],   # Package dependencies here
      #setup_requires=["setuptools_hg"],  # setuptools_hg must be installed as a python module
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Telecommunications Industry',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Communications',
          'Topic :: Internet',
          'Topic :: System :: Networking',
          'Topic :: System :: Networking :: Monitoring',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
     )
