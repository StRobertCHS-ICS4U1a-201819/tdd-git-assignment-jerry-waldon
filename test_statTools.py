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

def test_mean_basic1():
   assert(mean([1,2,3,4,5]) == 5)


