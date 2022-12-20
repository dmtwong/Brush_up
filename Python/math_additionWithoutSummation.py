# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:01:41 2022

@author: USER
"""

# You are given two numbers A and B.

# You have to add them without using arithmetic operators and return their sum.
# Problem Constraints
# 1 <= A, B <= 109

# Input Format
# The first argument is the integer A. The second argument is the integer B.

# Output Format
# Return a single integer denoting their sum.

# Example Input
# Input 1:
A = 3
B = 10
# Input 2:

A = 6
B = 1

# Example Output
# Output 1:13
# Output 2:7

# Example Explanation
# Explanation 1:
# 3 + 10 = 13
# Explanation 2:

# 6 + 1 = 7.
# Note, you have to add without using arithmetic operators.

# class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    # def addNumbers(self, A, B):
def addNumbers(A, B):
    # for i in range(B):
    #     A += 1
    # return A
    while (B > 0):
        shareBit = A & B
        A = A ^ B
        B = shareBit << 1
    return A
    

A = 452887384
B = 989233850
addNumbers(A, B)
