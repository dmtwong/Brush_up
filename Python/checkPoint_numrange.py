# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:25:58 2022

@author: USER
"""
# Given an array of non negative integers A, and a range (B, C), 

# find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C

# Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]

# where 0 <= i <= j < size(A)

# Example :

# ans = 3 

# as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]

# NOTE : The answer is guranteed to fit in a 32 bit signed integer.

# class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
# 	def numRange(self, A, B, C):

def numRange(A, B, C):
    def countSub(A, leftRightBound):
        n_A = len(A)
        head = 0
        tail = 0 
        roll_sum = 0
        numSub = 0 
    
        while tail < n_A :       
            # print(leftRightBound, roll_sum, head, A[head], tail, A[tail], numSub)
            roll_sum += A[tail] 
            while (head <= tail and roll_sum > leftRightBound) :
                # print('here', head, tail, roll_sum, leftRightBound)
                roll_sum -= A[head]
                head += 1
            # print('there', tail, head)
            numSub += (tail - head + 1)
            tail += 1     
        return numSub
    
    leftC = countSub(A, B - 1) 
    rightC = countSub(A, C)
    return rightC - leftC

A = [10, 5, 1, 0, 2]
B, C = (6, 8)
A = [10, 5, 1, 0, 0, 2]
B, C = (6, 8)
A = [10, 5, 1, 0, 0, 1, 2]
B, C = (6, 8)
A = [10, 5, 1, 0, 0, 1, 2]
B, C = (6, 9)
numRange(A, B, C)
