# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:00:29 2022

@author: USER
"""

# Problem Description
# Find the Bth smallest element in an unsorted array of non-negative integers A.
# Definition of kth smallest element: The kth smallest element is the minimum possible 
# n such that there are at least k elements in the array <= n.
# In other words, if the array A was sorted, then Ak - 1

# NOTE: You are not allowed to modify the array (The array is read-only). Try to do it using constant extra space.

# Problem Constraints
# 1 <= |A| <= 106
# 1 <= B <= |A|
# 1 <= A[i] <= 109


# Input Format
# The first argument is an integer array A.
# The second argument is integer B.


# Output Format
# Return the Bth smallest element in given array.


# Example Input
# Input 1:

A = [2, 1, 4, 3, 2]
B = 3
# Input 2:
A = [1, 2]
B = 2

# Example Output
# Output 1:
#  2
# Output 2:
#  2
# class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
# 	def kthsmallest(self, A, B):
    
def kthsmallest(A, B):
    # # A.sort()
    # # return A[B]
    # set_A = list(set(A))
    # set_A.sort()
    
    # for i in range(len(set_A)):
    #     # print(i, B, A.count(set_A[i]))
    #     B -= A.count(set_A[i])
    #     if (B <= 0):
    #         return set_A[i]
    #     else:
    #         continue
    def count(A, mid):
        result = 0
        for i in range(len(A)):
            if A[i] <= mid:
                result += 1
        return result
     
    low = -2147483648
    high = 2147483647
 
    for i in range(len(A)):
        low = min(low, A[i])
        high = max(high, A[i])
 
    while low < high:
        mid = low + (high - low) // 2
        if count(A, mid) < B:
            low = mid + 1
        else:
            high = mid
    return high

   
A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
B = 9
kthsmallest(A, B)
A = [ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ]
B = 1
