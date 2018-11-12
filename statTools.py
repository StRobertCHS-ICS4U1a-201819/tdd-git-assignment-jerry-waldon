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

    # return 0 when the list is empty
    if len(myList) == 0:
        return 0

    else:
        sum = 0

        # apply for loop to compute sum of each value
        for i in range(len(myList)):
            sum += myList[i]

        avg = sum / len(myList)  # get average
        return avg


def mode(myList):
    """Determine the value that appears with largest frequency in the values in the list given

    :param myList: A list of random integers
    :return: the value that appears with largest frequency
    """

    # condition when the list is empty
    if len(myList) == 0:
        return 0

    else:
        # get sorted list by called bubble_sort
        myList = bubble_sort(myList)

        appears = 0  # set appears for counting the number of same values appear in the list
        check_appears = 0  # set the check for comparing to get maximum frequency of the values
        max_appears_val = []  # set a restore list to put the value with maximum frequency 

        # run the loop before the second last value
        for i in range(len(myList) - 1):

            # when the value is equal with the next value
            if myList[i] == myList[i+1]:
                appears += 1        # add 1 on appears when the value is equal to the next value

                # when the value is second last, compare the number of appears 
                if i == len(myList) - 2:

                  if appears > check_appears:
                    check_appears = appears     # record the maximum frequency and restore the value
                    max_appears_val = [myList[i]]       # replace all the value with the value with largest appears
                  
                  elif appears == check_appears:
                    max_appears_val.append(myList[i])
                  appears = 0  # reset the appears to 0

            # when the value is not equal with the next value
            elif myList[i] != myList[i+1]:
               if appears > check_appears:
                    check_appears = appears     # record the maximum frequency and restore the value
                    max_appears_val = [myList[i]]       # replace all the value with the value with largest appears
                  
               elif appears == check_appears:
                    max_appears_val.append(myList[i])
               appears = 0  # reset the appears to 0

        return max_appears_val


def bubble_sort(myList):
    """Sort the list integers using bubble sort algorithm

    :param myList: list of unsorted integers
    :return: myList: list of sorted integers
    """
    # sort a list data from lowest to highest using the bubble sort algorithm
    n = len(myList)
    check = True

    while check:
        check = False

        for i in range(n - 1):
            if myList[i] > myList[i + 1]:
                # swap item at myList[i] with the item after it
                myList[i], myList[i + 1] = myList[i + 1], myList[i]
                check = True

        n -= 1
    return myList

def lower_quartile(myList):
    """Determine the value that is at the first quarter in the list given. If the number of values at each time when the
    lists are splited to be half, the range will be the average of two middle values

    :param myList: A list of random integers
    :return: the value at the first quarter position
    """
    if len(myList) == 0:
        return 0
    else:
        sorted_list = bubble_sort(myList)  # get sorted list by called bubble_sort function

        len_half_list = round(len(myList) / 2)  # get the index position of first half

        # the condition when the number of values is odd
        if len_half_list % 2 == 0:
            position = round(len_half_list / 2)
            low_quartile = position - 1
            return sorted_list[low_quartile]

        # the condition when the number of values is even
        else:

            # get the index position of two middle values
            position1 = round(len_half_list / 2)
            position2 = position1 - 1
            print(position1, position2)

            low_quartile = (sorted_list[position1 - 1] + sorted_list[position2 - 1]) / 2
            return low_quartile

def sum_val(myList):
    """Determine the sum of the values in the list given

    :param myList: A list of random integers
    :return: the sum of the values
    """
    sum = 0     # set sum as 0

    # apply for loop to compute the sum of each values
    for i in range(len(myList)):
       sum += myList[i]
    return sum

def sum_square(myList):
    """Determine the sum of the square of each value in the list given

    :param myList: A list of random integers
    :return: the sum of square of each value
    """
    sum = 0     # set sum as 0

    # apply for loop to compute the sum of square of each values
    for i in range(len(myList)):
        sum += myList[i] * myList[i]
    return sum

def variance(myList):
    """Determine variance of the list given

    :param myList: A list of random integers
    :return: the variance of the list
    """


    if myList == [0] or len(myList) == 0:
        return -1
    else:
        step1 = sum_val(myList)  # call the sum function to get sum of values in list
        step2 = step1 * step1  # calculate the square of the sum of the values in the list
        step3 = step2 / len(myList)  # the result from step2 divided by the length of the list given
        step4 = sum_square(myList)  # call the sum_square function to get the sum of square of each values in the list
        step5 = step4 - step3  # the result from step 4 subtract the result from step3
        step6 = len(myList) - 1  # get the result of the length of the list subtract 1
        step7 = step5 / step6  # the result from step5 divide by the result from step6
        return step7


   

       