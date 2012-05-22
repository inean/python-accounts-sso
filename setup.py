#!/usr/bin/env python

from setuptools import setup
from itertools import ifilter

def find(walk, suffix, install):
   """Find files that match suffix"""
   import os
   _files = []
   for root, dirs, files in os.walk(walk):
      for f in ifilter(lambda x: x.endswith(suffix), files):
         _files.append((install, [os.path.join(root, f)]))
   return _files

setup(
   name='accountsSSO',
   version='0.0.1',
   description='AccountSSO bindings for Harmattan platform',
   license = "BSD",
   author='Carlos Martin',
   author_email='inean.es@gmail.com',
   url='https://github.com/inean/python-accounts-sso',
   packages=['accountsSSO'],
   data_files=find('accountsSSO', '.so', 'accountsSSO'),
   classifiers=[
      "Development Status :: 3 - Alpha",
      "Topic :: Utilities",
      "License :: OSI Approved :: BSD License",
   ],
)
