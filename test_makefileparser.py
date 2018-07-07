# -*- coding: utf-8 -*-
__author__ = 'gchlebus'

import pytest
import imp
automake = imp.load_source('automake', 'automake')

def test_target_not_found():
  with pytest.raises(RuntimeError):
    parser = automake.MakefileParser('test_makefiles/Makefile1', 'asd')

def test_simple_makefile():
  parser = automake.MakefileParser('test_makefiles/Makefile1')
  assert parser.prerequisites == 'foo1 foo2'.split()

def test_expand_variables():
  parser = automake.MakefileParser('test_makefiles/Makefile2')
  assert parser.prerequisites == 'foo bar'.split()

def test_dependencies():
  parser = automake.MakefileParser('test_makefiles/Makefile3')
  assert parser.prerequisites == 'foo1 foo2 foo3'.split()
