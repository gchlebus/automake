# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

from setuptools import setup, find_packages

setup(
  name='automake',
  version='0.1.0',
  author='Grzegorz Chlebus',
  url='https://github.com/gchlebus/automake',
  license='BSD 3-Clause',
  author_email='gchlebus@gmail.com',
  packages=find_packages(exclude=['test']),
  install_requires=['click', 'watchdog'],
  entry_points='''
    [console_scripts]
    automake=automake.cli:cli
  '''
)
