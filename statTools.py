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

       avg = sum / len(myList)     # get average
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

       appears = 0     # set appears for counting the number of same values appear in the list
       check_appears = 0       # set the check for comparing to get maximum frequency of the values
       max_appears_val = 0     # set a restore place to put the value with maximum frequency

       # run the loop before the second last value
       for i in range(len(myList)-1):

           # count by 1 when the value is equal with the next value
           if myList[i] == myList[i+1]:
               appears += 1

           else:
               if appears > check_appears:

                   # record the maximum frequency and restore the value
                   check_appears = appears
                   max_appears_val = myList[appears]

               appears = 0     # reset the appears to 0
       return max_appears_val

def lower_quartile(myList):
   """Determine the value that is at the first quarter in the list given. If the number of values at each time when the
   lists are splited to be half, the range will be the average of two middle values

   :param myList: A list of random integers
   :return: the value at the first quarter position
   """

   return 2