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


# empty case
def test_median_empty():
    assert(median([]) == "The list is empty, please enter a integer list.  ")


# common odd case
def test_median_basic1():
    assert(median([1, 2, 3, 4, 5]) == 3)


# common reverse odd case
def test_median_basic2():
    assert(median([9, 8, 7, 6, 5]) == 7)


# unusual same number case
def test_median_unusual1():
    assert(median([1, 1, 1, 1, 1, 1]) == 1)


# unusual even case
def test_median_unusual2():
    assert(median([1, 2, 3, 4]) == 2.5)


# unusual reverse even case
def test_median_unusual3():
    assert(median([9, 6, 2, 4]) == 5)


# unusual negative case
def test_median_unusual4():
    assert(median([-2, -1, 0, 1, 2]) == 0)


# string case
def test_median_string():
    assert(median(["s", "g"]) == "There is a string in the list, please enter a integer list.  ")


"range test"


# empty case
def test_range_empty():
    assert(range([]) == "The list is empty, please enter a integer list.  ")


# common odd case
def test_range_basic1():
    assert(range([1, 2, 3, 4, 5]) == 4)


# common reverse odd case
def test_range_basic2():
    assert(range([9, 8, 7, 6, 5]) == 4)


# unusual same number case
def test_range_unusual1():
    assert(range([1, 1, 1, 1, 1, 1, 1]) == 0)


# unusual odd case
def test_range_unusual2():
    assert(range([4, 6, 2, 9, 0, 3]) == 9)


# unusual negative case
def test_range_unusual3():
    assert(range([-1, 3, -5, 6]) == 11)


# string case
def test_range_string():
    assert(range(["d", "g"]) == "There is a string in the list, please enter a integer list.  ")


"upper_quartile tests"


# empty case
def test_upper_quartile_empty():
    assert(upper_quartile([]) == "The list is empty, please enter a integer list.  ")


# common odd case
def test_upper_quartile_basic1():
    assert(upper_quartile([1, 2, 3, 4, 5]) == 4.5)


# common reverse odd case
def test_upper_quartile_basic2():
    assert(upper_quartile([5, 4, 3, 2, 1]) == 4.5)


# unusual even case
def test_upper_quartile_unusual1():
    assert(upper_quartile([1, 2, 3, 4]) == 3.5)


# unusual same number case
def test_upper_quartile_unusual2():
    assert(upper_quartile([1, 1, 1, 1, 1, 1]) == 1)


# unusual negative case
def test_upper_quartile_unusual3():
    assert(upper_quartile([3, -5, 8, 0]) == 5.5)


# string case
def test_upper_quartile_string():
    assert(upper_quartile(["g", 'd']) == "There is a string in the list, please enter a integer list.  ")


"standard deviation tests"


# empty case
def test_standard_deviation_empty():
    assert(standard_deviation([]) == "The list is empty, please enter a integer list.  ")


# common odd case
def test_standard_deviation_basic1():
    assert(standard_deviation([1, 2, 3, 4, 5]) == 1.41)


# string case
def test_standard_deviation_string():
    assert(standard_deviation(["hd", "s"]) == "There is a string in the list, please enter a integer list.  ")
