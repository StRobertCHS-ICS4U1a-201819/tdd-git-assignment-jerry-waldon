"""
-------------------------------------------------------------------------------
Name:		test_statTools.py
Purpose:
white-box and black-box test programs in statTools with TDD method

Author:		Zhang.W

Created:		11/12/2018
------------------------------------------------------------------------------
"""

import pytest
from statTools import *

"median tests"


def test_median_empty():
    assert(median([]) == 0)


def test_median_basic1():
    assert(median([1, 2, 3, 4, 5]) == 3)


def test_median_basic2():
    assert(median([9, 8, 7, 6, 5]) == 7)


def test_median_unusual1():
    assert(median([1, 1, 1, 1, 1, 1]) == 1)


def test_median_unusual2():
    assert(median([1, 2, 3, 4]) == 2.5)


def test_median_unusual3():
    assert(median([9, 6, 4, 2]) == 5)
