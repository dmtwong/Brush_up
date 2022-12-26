# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 17:01:07 2022

@author: USER
"""

# Problem Description
# Write a function that takes an integer and returns the number of 1 bits it has.

# Problem Constraints
# 0 <= A <= 4294967295

# Input Format
# First and only argument contains integer A

# Output Format
# Return an integer as the answer

# Example Input
# Input1:
#     11

# Example Output
# Output1:
# 3

# Example Explanation
# Explaination1:
# 11 is represented as 1101 in binary 

# class Solution:
    # @param A : integer
    # @return an integer
    # def numSetBits(self, A):
def numSetBits(A):
    result = 0
    while (A > 0):
        # print(A//2)
        # print(A%2)
        # print(A&1)
        result += (A & 1)
        A = (A // 2)
    return result
A = 4294967295
A= 11
A= 0
A= 1
numSetBits(A)

# Suggested:
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def numSetBits(self, A):
#         ret = 0
#         while A != 0:
#             if A&1:
#                 ret += 1
#             A = A >> 1
#         return ret
# int Solution::numSetBits(unsigned int A) {
#     assert(A >= 0 && A <= UINT_MAX );
#     unsigned int total_ones = 0;
#     while (A != 0) {
#         A = A & (A-1);
#         total_ones++;
#     }
#     return total_ones;
# }
# public class Solution {
# 	public int numSetBits(long A) {
# 	    
# 	    int count = 0;
# 	    
# 	    while (A > 0) {
# 	        if ( (A & 1) != 0)
# 	            count++;
# 	        A >>= 1;
# 	    }
# 	    
# 	    return count;
# 	    
# 	}
# }
