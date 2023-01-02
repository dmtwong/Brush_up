# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:48:00 2023

@author: USER
"""
##############
# still stuck on one test case; revisit a bit later 
##############
# Problem Description 

# Given a list of non-negative integers, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.

# Problem Constraints
# 1 <= |A| <= 105
# 1 <= Ai <= 109

# Input Format
# The first argument is an integer array A.

# Output Format
# Return a string representing the largest number formed

# Example Input
A = [3, 30, 34, 5, 9]

# Example Output
# 9534330

# Example Explanation
# Largest possible number that can be formed is 9534330
# class Solution:
    # @param A : tuple of integers
    # @return a strings
  A = [123, 213, 111]
  # order_A(123,213)
   # order_A(123,111)
  # order_A(123,1234)
  # order_A(223,224)
  # help(list.sort)
 # A.sort(key = order_A)
def largestNumber(A):
    from functools import cmp_to_key
    A = list(A) # test case use is tuple somehow
    def order_A(ele_1, ele_2):
        len_1, len_2 = 0, 0
        temp_1, temp_2 = ele_1, ele_2
        list_1, list_2 = [], []
        while temp_1 > 0:
            len_1 += 1
            list_1.insert(0, temp_1 % 10)
            temp_1 //= 10
        while temp_2 > 0:
            len_2 += 1
            list_2.insert(0, temp_2 % 10)
            temp_2 //= 10    
        # print(list_1, list_2)
        min_len = min(len_1, len_2)
        ix = 0
        while (min_len != 0):
            if list_1[ix] > list_2[ix]:
                return 1
            elif list_1[ix] < list_2[ix]:
                return -1
            else:
                # list_1.pop(0)
                # list_2.pop(0)
                min_len -= 1
                ix += 1
        min_len = min(len_1, len_2)
        j = 0
        temp_1a, temp2a = len_1, len_2
        if len_1 > len_2: # Ex: 932 vs 93 93932>93293 9393 93932 9393
            while j != temp2a and len_2 <= temp_1a -1:
                if list_1[len_2] > list_2[j]:
                    return 1
                elif list_1[len_2] < list_2[j]:
                    return -1
                else:
                    j += 1
                    len_2 += 1
        elif len_1 < len_2:
            while temp_1a != j and len_1 <= temp2a - 1:
                # print(j, len_1, list_1, list_2)
                if list_1[j] > list_2[len_1]:
                    return 1
                elif list_1[j] < list_2[len_1]:
                    return -1
                else:
                    j += 1
                    len_1 += 1
        return 1 # order doesn't matter
            
    A.sort(key = cmp_to_key(order_A), reverse = True)
    A = [str(x) for x in A]
    # return "".join(A)
    return str(int("".join(A)))  # Corner case with a list of zero

A = [8, 89]
A = [ 170, 480, 735, 896, 634, 844, 1, 610, 446, 591, 935, 802, 383, 8, 443, 247, 124, 461, 317, 457, 48, 886, 420, 473, 973, 464, 203, 288, 785, 703, 935, 7, 987, 48, 692, 633, 597, 857, 139, 733, 692, 68, 434, 587, 489, 517, 305, 432, 577, 335, 586, 34, 659, 491, 310, 857, 256, 856, 257, 877, 209, 979, 653, 646, 2, 65, 858, 779, 372, 116, 404, 268, 364, 351, 866, 824, 947, 960, 91, 691, 492, 312, 609, 915, 579, 476, 248, 192 ]
A = [ 12, 121 ]

largestNumber(A)
