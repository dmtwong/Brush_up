# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 23:47:02 2022

@author: USER
"""

Given an integer array A of size N.
You need to check that whether there exist a element which is strictly greater 
than all the elements on left of it and strictly smaller than all the elements on right of it.
If it exists return 1 else return 0.
NOTE:
Do not consider the corner elements i.e A[0] and A[N-1] as the answer.
Problem Constraints
3 <= N <= 105
1 <= A[i] <= 109

Input Format
First and only argument is an integer array A containing N integers.

Output Format
Return 1 if there exist a element that is strictly greater than all the elements 
on left of it and strictly  smaller than all the elements on right of it else return 0.

Example Input
Input 1:
 A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
Input 2:
 A = [5, 1, 4, 4]
Example Output
Output 1:
 1
Output 2:
 0
A = [ 5706, 26963, 24465, 29359, 16828, 26501, 28146, 18468, 9962, 2996, 492, 11479, 23282, 19170, 15725, 6335 ]

class Solution:
    # @param A : list of integers
    # @return an integer
    # def perfectPeak(self, A):
def perfectPeak(A):
    len_A = len(A)
    if len_A < 3:
        return 0
    max_left = [A[0]] * len_A
    # print(max_left)
    min_right = [max(A[1:])] * len_A
    # print(min_right)
    for i in range(1, len_A):
        # print(A[i], max_left[i-1], max_left[i])
        if A[i] > max_left[i-1]:
            max_left[i] = A[i]
        else:
            max_left[i] =max_left[i-1]
    # print('here')
    for i in range(len_A - 2, -1, -1):
        # print(A[i], min_right[i+1], min_right[i])
        if A[i] < min_right[i+1]:
            min_right[i] = A[i]
        else:
            min_right[i] = min_right[i+1]
    for i in range(1, len_A - 1):
        if A[i] > max_left[i-1] and A[i] < min_right[i+1]:
            # print(A[i])
            return 1
    return 0
perfectPeak(A)        
        