# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:21:27 2023

@author: USER
"""

#####
# Not working
#####
# Problem Description

# You are given a preorder traversal A, of a Binary Search Tree.
# Find if it is a valid preorder traversal of a BST.
# Note: Binary Search Tree by definition has distinct keys and duplicates in binary search tree are not allowed.

# Problem Constraints
# 1 <= A[i] <= 106
# 1 <= |A| <= 105

# Input Format
# First and only argument is an integer array A denoting the pre-order traversal.

# Output Format
# Return an integer:
# 0 : Impossible preorder traversal of a BST
# 1 : Possible preorder traversal of a BST
# Example Input
# Input 1:
A = [7, 7, 10, 10, 9, 5, 2, 8]

# Example Output
# Output 1: 0

# class Solution:
    # @param A : list of integers
    # @return an integer
    # def solve(self, A):
def solve(A):
    n_A = len(A)
    rt = -2147483648
    node_list = list() 
    for i in range(n_A):
        curr_A = A[i]
        if curr_A < rt :
            print(i, curr_A, rt)
            return 0
        while len(node_list) > 0 and node_list[-1] < curr_A:
            print(node_list)
            rt = node_list.pop()
            print(node_list)
        print(curr_A)
        node_list.append(curr_A) 
    return 1
A = [ 1, 1, 2, 3, 4 ]

solve(A)

