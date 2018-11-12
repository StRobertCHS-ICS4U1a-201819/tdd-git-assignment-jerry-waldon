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
   assert(mode([2,4,3,2,2,2]) == [2])

def test_mode_basic2():
   assert(mode([2,4,3,3,3,2]) == [3])

def test_mode_unusual1():
    assert(mode([2,4,3,3,3,2,2]) == [2,3])

def test_mode_unusual2():
    assert(mode([2,4,3,3,3,2,2,4,4,4]) == [4])

def test_mode_empty():
    assert(mode([]) == 0)


def test_lower_quartile_basic1():
   assert(lower_quartile([1,2,3,4,5,6,7]) == 2)

def test_lower_quartile_basic2():
   assert(lower_quartile([1,2,3,4,5,6,7,8,9,10,11]) == 3)

def test_lower_quartile_basic3():
   assert(lower_quartile([1,2,3,4,5,6]) == 1.5)

def test_lower_quartile_unusual1():
   assert(lower_quartile([1,1,1,1]) == 1)

def test_lower_quartile_unusual2():
   assert(lower_quartile([1,4,2,5,6,3]) == 1.5)

def test_lower_quartile_empty():
   assert(lower_quartile([0]) == 0)

def test_variance_basic1():
   assert(variance([1,2,3,4,5]) == 2.5)

def test_variance_basic2():
   assert(variance([3,21,98,203,17,9]) == 6219.9)

def test_variance_unusual1():
   assert(variance([0]) == -1)

def test_variance_unusual2():
   assert(variance([-1,-2,-3,-4,-5]) == 2.5)

def test_variance_empty():
   assert(variance([]) == -1)

