# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:57:57 2022

@author: USER
"""

# Problem Description

# Given a string A. The only operation allowed is to insert characters at the beginning of the string.
# Find how many minimum characters are needed to be inserted to make the string a palindrome string.

# Problem Constraints
# 1 <= |A| <= 106

# Input Format
# The only argument given is string A.

# Output Format
# Return the minimum characters that are needed to be inserted to make the string a palindrome string.

# Example Input
# Input 1:
# A = "ABC"
# Input 2:
A = "AACECAAAA"

# Example Output
# Output 1:2
# Output 2:2

# Example Explanation
# Explanation 1:
# Insert 'B' at beginning, string becomes: "BABC".
# Insert 'C' at beginning, string becomes: "CBABC".
# Explanation 2:
# Insert 'A' at beginning, string becomes: "AAACECAAAA".
# Insert 'A' at beginning, string becomes: "AAAACECAAAA".

# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):

def solve(A):
    def findLp(sub_A):        
        n_sub_A = len(sub_A)
        lps = [None] * n_sub_A
        lps[0] = 0 

        length = 0
        i = 1
        while i < n_sub_A:         
            if sub_A[i] == sub_A[length]:
                # print(i, sub_A, length)
                # print(lps)
                length += 1
                lps[i] = length
                i += 1             
            elif length != 0:               
                # print('here', length, i)
                # print(lps)
                length = lps[length - 1]
            else: 
                # print('there', i)
                # print(lps)
                lps[i] = 0
                i += 1     
        return lps

    n_A = len(A)
    rev_A = A[::-1]    
    mirror_A = A + "$" + rev_A    
    lps = findLp(mirror_A)
    
    return n_A - lps[-1]
# A2 = "hqghumeaylnlfdxfi"
solve(A)        
# solve(A2)
