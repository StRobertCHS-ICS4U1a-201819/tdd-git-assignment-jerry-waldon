"""
-------------------------------------------------------------------------------
Name:		statTools.py
Purpose:
write four functions with TDD method

Author:		Zhang.W

Created:		11/11/2018
------------------------------------------------------------------------------
"""


def median(my_list):
    """
    get the median number of the input list
    :param my_list: a integer list
    :return: the median number of the input list
    """

    # return error statement if my_list is empty
    if len(my_list) == 0:
        return "The list is empty, please enter a integer list.  "

    # return error statement if there is a string i my_list
    for i in my_list:
        if type(i) == str:
            return "There is a string in the list, please enter a integer list.  "

    else:
        # sort my_list
        my_list.sort()

        # return the median number of my_list
        return (my_list[(len(my_list) + 1) // 2 - 1] + my_list[(len(my_list) + 2) // 2 - 1]) / 2


def range(my_list):
    """
    calculate the value of the largest value minus the smallest value
    :param my_list: a integer list
    :return: the range of the input list
    """

    # return error statement if my_list is empty
    if len(my_list) == 0:
        return "The list is empty, please enter a integer list.  "

    # return error statement if there is a string i my_list
    for i in my_list:
        if type(i) == str:
            return "There is a string in the list, please enter a integer list.  "

    else:
        # sort my_list
        my_list.sort()

        # return the range of my_list
        return my_list[len(my_list) - 1] - my_list[0]


def upper_quartile(my_list):
    """
    get the median number of the second half of the input list
    :param my_list: a integer list
    :return: the upper quartile og the input list
    """

    # return error statement if my_list is empty
    if len(my_list) == 0:
        return "The list is empty, please enter a integer list.  "

    # return error statement if there is a string i my_list
    for i in my_list:
        if type(i) == str:
            return "There is a string in the list, please enter a integer list.  "

    else:
        # sort my_list
        my_list.sort()

        # return the upper quartile of my_list
        return median(my_list[(len(my_list) + 1) // 2:])


def standard_deviation(my_list):
    """
    calculate the
    :param my_list: a integer list
    :return: the standard deviation of the input list
    """

    # assign sum1 and sum2 with a value of 0
    sum1 = 0
    sum2 = 0

    # let the program run the times of the length of my_list
    for i in my_list:
        # return error statement if there is a string i my_list
        if type(i) == str:
            return "There is a string in the list, please enter a integer list.  "

        else:
            # get the sum of my_list and assign it with sum1
            sum1 += i

    # return error statement if my_list is empty
    if len(my_list) == 0:
        return "The list is empty, please enter a integer list.  "

    else:
        # get mean of my_list
        mean = sum1 / len(my_list)

        # let the program run the times of the length of my_list
        for index in my_list:
            # get the sum of the square of difference between the mean and each value
            sum2 += (mean - index) ** 2

        # return the standard deviation
        return round((sum2 / len(my_list)) ** 0.5, 2)
