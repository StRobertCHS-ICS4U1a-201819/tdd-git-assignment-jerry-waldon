"""
-------------------------------------------------------------------------------
Name:		statTools.py
Purpose:
write four programs with TDD method

Author:		Zhang.W

Created:		11/12/2018
------------------------------------------------------------------------------
"""
import math


def median(my_list):
    """
    get the median number of the input list

    :param my_list: a list of integers of input
    :return: the median number of the input list
    """

    # return 0 if the list is empty
    if len(my_list) == 0:
        return 0

    else:
        # sort my_list
        my_list.sort

        # return the median number of the sorted list
        return (my_list[(len(my_list) + 1) // 2 - 1] + my_list[(len(my_list) + 2) // 2 - 1]) / 2


def range(my_list):
    """get the range of the list of integers of input

    :param my_list: a list of input
    :return: the range of the list of input
    """

    # return 0 if the list is empty
    if len(my_list) == 0:
        return 0

    else:
        # sort my_list
        my_list.sort

        # return the range of my_list
        return my_list[len(my_list) - 1] - my_list[0]
