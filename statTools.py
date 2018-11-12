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


def bubble_sort(data):
    """
    Sort the list data using bubble sort algorithm
    :param data: list of comparable objects
    :return: a sorted list
    """

    # sort a list data from lowest to highest using the bubble sort algorithm
    n = len(data)
    has_swapped = True

    while has_swapped:
        has_swapped = False

        for i in range(n - 1):
            if data[i] > data[i + 1]:
                # swap item at data[i] with the item after it
                data[i], data[i + 1] = data[i + 1], data[i]
                has_swapped = True

        n -= 1
    return data


def median(my_list):
    """get the median number of the input list

    :param my_list: a list of integers of input
    :return: the median number of the input list
    """

    # return 0 if the list is empty
    if len(my_list) == 0:
        return 0

    else:
        # sort my_list
        my_list = bubble_sort(my_list)

        # return the median number of the sorted list
        return (my_list[(len(my_list) + 1) // 2] + my_list[(len(my_list) + 2) // 2]) / 2
