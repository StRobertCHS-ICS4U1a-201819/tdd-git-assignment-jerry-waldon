"""
-------------------------------------------------------------------------------
Name:     statTools.py
Purpose:
Four programs developed by the TDD method

Author:       Cui.Jerry

Created:      11-11-2018
------------------------------------------------------------------------------
"""

def mean(myList):
    """Determine the average of the values that the list given

    :param myList: A list of random integers
    :return: the average of the list given
    """

    sum = 0

    # apply for loop to compute sum of each value
    for i in range(len(myList)):
        sum += myList[i]

    avg = sum / len(myList)  # get average
    return avg
