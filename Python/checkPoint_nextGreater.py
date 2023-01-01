# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 21:16:18 2022

@author: USER
"""

# Given an array, find the next greater element G[i] for every element A[i] in the array.  
# The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. 

# More formally,

# G[i] for an element A[i] = an element A[j] such that 
#     j is minimum possible AND 
#     j > i AND
#     A[j] > A[i]
# Elements for which no greater element exist, consider next greater element as -1.

# Example:

# Input : A : [4, 5, 2, 10]

# Output : [5, 10, 10, -1]

# Example 2:

# Input : A : [3, 2, 1]

# Output : [-1, -1, -1]

# class Solution:
	# @param A : list of integers
	# @return a list of integers
# 	def nextGreater(self, A):
# from collections import deque 
# A = [4, 5, 2, 10]
# A = deque(A) 
# 5 in A
# 1 in A
# A
# list(A)

def nextGreater(A):
    # from collections import deque 
    # deque_A = deque(A)
    result = []
    n_A = len(A)
    if n_A > 1:
        local_max = None
    else: 
        return [-1]
    
    reset_flag = False
    for i in range(n_A):         
        # print('this is ', i)
        if not reset_flag:
            local_max = A[i]
            reset_flag = True
        if A[i] < local_max and A[i-1] <= A[i]:
            # print('here')
            result.append(local_max)
            continue
        j = i + 1
        isfound = False
        while(j < n_A):
            # print('there', i, j)
            if A[j] > A[i]:
                # print('yes!')
                local_max = A[j]
                result.append(A[j])
                isfound = True
                break
            j += 1
        # print('no')
        if not isfound:
            result.append(-1)
            local_max = None
            reset_flag = False
    return result

A = [4, 5, 2, 10]

A = [3, 2, 1]
A = [ 48, 38, 42, 39, 28, 6, 49, 34 ]

nextGreater(A)      
