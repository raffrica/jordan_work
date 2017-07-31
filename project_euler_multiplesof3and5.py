#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:15:09 2017

@author: danielraff
"""
# Project Euler: Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# list(range(1000)

# sol #1

# def mult_of_3_or_5():
#    def add_multiples_to_set(integer):
#        if integer % 3 == 0:
#            multiples_set.update({integer})
#        elif integer % 5 == 0:
#            multiples_set.update({integer})
#    multiples_set = set()
#    for integer in list(range(1000)):
#        add_multiples_to_set(integer)
#    return sum(multiples_set)
  

# sol #2
      
def mult_of_3_or_5():
    def is_multiples(integer):
        if integer % 3 == 0:
            return True
        elif integer % 5 == 0:
            return True
        else:
            return False

    return sum([integer for integer in list(range(1000)) if is_multiples(integer)])
    


print(mult_of_3_or_5())


# Learning Note:
    # Initially tried to do above by having a function in the first position of 
    # the list comprehension but wasn't working
    # as Jordan pointed out, when run the above list comprehension and add the if 
    # statement, will just compile the list that = True
    # even without having a function in first position of list comprehension