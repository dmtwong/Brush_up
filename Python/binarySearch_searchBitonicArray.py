# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:14:14 2022

@author: USER
"""

# Problem Description
#  Given a bitonic sequence A of N distinct elements, write a program to find a 
#  given element B in the bitonic sequence in O(logN) time.

# NOTE:

# A Bitonic Sequence is a sequence of numbers which is first strictly increasing 
# then after a point strictly decreasing.


# Problem Constraints
# 3 <= N <= 105

# 1 <= A[i], B <= 108

# Given array always contain a bitonic point.
# Array A always contain distinct elements.

# Input Format
# First argument is an integer array A denoting the bitonic sequence.
# Second argument is an integer B.

# Output Format
# Return a single integer denoting the position (0 index based) of the element B 
# in the array A if B doesn't exist in A return -1.

# Example Input
# Input 1:

  # A = [3, 9, 10, 20, 17, 5, 1]
  # B = 20
   # solve(A, B)
# Input 2:

  # A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
  # B = 30

# Example Output
# Output 1: 3
# Output 2: -1

# Example Explanation
# Explanation 1:

#  B = 20 present in A at index 3
# Explanation 2:

#  B = 30 is not present in A

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
def solve(A, B):
    def find_bp(A, left, right):
        bp = 0
        mid = (left + right) // 2
        if A[mid] > A[mid - 1] and A[mid + 1] < A[mid]:
            return mid
        elif A[mid] > A[mid - 1] and A[mid + 1] > A[mid]:
            bp = find_bp(A, mid, right)
        else:
            bp = find_bp(A, left, mid)
        return bp
    def search_up(A, left, right, key):
        # print('up', A, left, right, key)
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == key:
                return mid
            if A[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    def search_down(A, left, right, key):
        # print('down', A, left, right, key)
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == key:
                return mid
            if A[mid] < key:
                right = mid - 1
            else:
                left = mid + 1
        return -1       
    def search(A, ix, n, key):    
        # print('here', A, ix, n, key)
        if key > A[ix]:
            return -1
        elif key == A[ix]:
            return ix
        else:
            result = search_up(A, 0, ix-1, key)
            if result != -1:
                return result                 
            return search_down(A, ix+1, n-1, key)
    n_A = len(A)
    ix = find_bp(A, 0, n_A - 1)
    result = search(A, ix, n_A, B)
    if result == -1:
        return -1
    else:
        return result
    
    
                