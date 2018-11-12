"""
-------------------------------------------------------------------------------
Name:		test_statTools.py
Purpose:
white-box test and black-box test on the programs in statTools.py

Author:		Cui.Jerry

Created:		11/11/2018
------------------------------------------------------------------------------
"""

import pytest
from statTools import *

def test_mean_basic1():
   assert(mean([1,2,3]) == 2)
def test_mean_basic2():
   assert(mean([1,2,3,4,5]) == 3)
def test_mean_empty():
   assert(mean([]) == 0)


def test_mode_basic1():
   assert(mode([2,4,3,2,2,2]) == 2)

def test_mode_basic2():
   assert(mode([2,4,3,3,3,2]) == 3)

def test_mode_unusual1():
    assert(mode([2,4,3,3,3,2,2]) == 3)

def test_mode_unusual2():
    assert(mode([2,4,3,3,3,2,2]) == 2)


