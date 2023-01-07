# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 21:12:35 2023

@author: USER
"""
# Problem Description
# Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
# Also given an integer C which represents knapsack capacity.
# Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.
# NOTE:
# You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

# Problem Constraints
# 1 <= N <= 103
# 1 <= C <= 103
# 1 <= A[i], B[i] <= 103


# Input Format
# First argument is an integer array A of size N denoting the values on N items.
# Second argument is an integer array B of size N denoting the weights on N items.
# Third argument is an integer C denoting the knapsack capacity.

# Output Format
# Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

# Example Input
# Input 1:
 A = [60, 100, 120] # value
 B = [10, 20, 30] # weight
 C = 50 # capacity
# Input 2:
 A = [10, 20, 30, 40]
 B = [12, 13, 15, 19]
 C = 10

# Example Output
# Output 1:
#  220
# Output 2:
#  0
# Example Explanation
# Explanation 1:

#  Taking items with weight 20 and 30 will give us the maximum value i.e 100 + 120 = 220
# Explanation 2:

#  Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.
# class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    # def solve(self, A, B, C):
def solve(A, B, C):
    # import collections
    # pairAB = collections.OrderedDict()
    pairAB = []
    for i in range(len(A)):
        pairAB.append((A[i], B[i]))
    # print(pairAB)   
    
    def solve_withMemory(sub_pairAB, remain_C, memo_Dict = {}):
        n_pairAB = len(sub_pairAB)
        # print(sub_pairAB[0], remain_C)
        if (n_pairAB, remain_C) in memo_Dict:
            result = memo_Dict[(n_pairAB, remain_C)]
        elif n_pairAB == 0 or remain_C == 0:
            result = (0, ())
        elif sub_pairAB[0][1] > remain_C: # too heavy hence only explore right path
            result = solve_withMemory(sub_pairAB[1:], remain_C, memo_Dict)
        else:
            curr_val, curr_weight = sub_pairAB[0]
            # print(curr_val, curr_weight, sub_pairAB[0])
            # print(solve_withMemory(sub_pairAB[1:], remain_C - curr_weight, memo_Dict))
            valLeft,withItemTaken = solve_withMemory(sub_pairAB[1:], remain_C - curr_weight, memo_Dict)
            # valLeft = solve_withMemory(sub_pairAB[1:], remain_C - curr_weight, memo_Dict)
            # print(temp[0])
            # print(temp)
            valLeft += curr_val
            valright, withoutItemTaken = solve_withMemory(sub_pairAB[1:], remain_C, memo_Dict)
            # valright = solve_withMemory(sub_pairAB[1:], remain_C, memo_Dict)
            if valLeft > valright:
                # print('added with item weight:', curr_weight)
                result = (valLeft, withItemTaken + (sub_pairAB[0], ))
                remain_C -= curr_weight
                # print(result)
                # print(remain_C)
            else:
                # print('dropped')
                result = (valright, withoutItemTaken)
                # print(result)
                # print(remain_C)
        memo_Dict[(n_pairAB, remain_C)] = result
        # print(memo_Dict.keys())
        # print(memo_Dict.values())

        return result
    
    # return solve_withMemory(pairAB, C)[0]
    return solve_withMemory(pairAB, C)
solve(A, B, C)

A = [ 377, 932, 309, 945, 440, 627, 324, 538, 539, 119, 83, 930, 542, 834, 116, 640, 659, 705, 931, 978, 307, 674, 387, 22, 746, 925, 73, 271, 830, 778, 574, 98, 513, 987, 291, 162, 637, 356, 768, 656, 575, 32, 53, 351, 151, 942, 725, 967, 431, 108, 192, 8, 338, 458, 288, 754, 384, 946, 910, 210, 759, 222, 589, 423, 947, 507, 31 ]
B = [ 14, 19, 1, 42, 13, 6, 11, 10, 25, 38, 49, 34, 46, 42, 3, 1, 42, 37, 25, 21, 47, 22, 49, 50, 19, 35, 32, 35, 4, 50, 19, 39, 1, 39, 28, 18, 29, 44, 49, 34, 8, 22, 11, 18, 14, 15, 10, 17, 36, 2, 1, 50, 20, 7, 49, 4, 25, 9, 45, 10, 40, 3, 46, 36, 44, 44, 24 ]
len(A) == len(B)
C = 588
temp =solve(A, B, C)
weight_list = [y for x, y in temp[1]]
sum(weight_list )
# The expected return value: 
22819
# Your function returned the following: 
30736