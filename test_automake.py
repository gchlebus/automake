# -*- coding: utf-8 -*-
__author__ = 'gchlebus'

import pytest
import os
import imp
import contextlib
from threading import Thread
import time
automake = imp.load_source('automake', 'automake')

TMP_FILENAME = 'tmp_file'
TEST_MAKEFILES_DIR = 'test_makefiles'

@contextlib.contextmanager
def changedir(dirpath):
  cwd = os.getcwd()
  os.chdir(dirpath)
  try:
    yield
  finally:
    os.chdir(cwd)

@contextlib.contextmanager
def cleanupfile(filename):
  try:
    yield
  finally:
    if os.path.exists(filename):
      os.remove(filename)

def test_simplerun():
  automake.STOP_AFTER_NSEC = 1
  with changedir(TEST_MAKEFILES_DIR), cleanupfile(TMP_FILENAME):
    automake.automake(test_simplerun.__name__, debug=True)
    assert os.path.exists(TMP_FILENAME)

def test_makefilechange():
  automake.STOP_AFTER_NSEC = 2
  with changedir(TEST_MAKEFILES_DIR), cleanupfile(TMP_FILENAME):
    t = Thread(target=automake.automake, args=(test_makefilechange.__name__,))
    t.start()
    time.sleep(1)
    open(test_makefilechange.__name__, 'a').close()
    os.utime(test_makefilechange.__name__, None)
    t.join()
    with open(TMP_FILENAME, 'r') as f:
      assert 2 == len(f.readlines())