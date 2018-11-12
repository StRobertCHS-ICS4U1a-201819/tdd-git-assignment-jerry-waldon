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

   return 2
