# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:12:50 2022

@author: USER
"""

# Problem Description

# Given the position of a Bishop (A, B) on an 8 * 8 chessboard.

# Your task is to count the total number of squares that can be visited by the Bishop in one move.

# The position of the Bishop is denoted using row and column number of the chessboard.

# Problem Constraints
# 1 <= A, B <= 8

# Input Format
# First argument is an integer A denoting the row number of the bishop.

# Second argument is an integer B denoting the column number of the bishop.

# Output Format
# Return an integer denoting the total number of squares that can be visited by the Bishop in one move.

# Example Input
# Input 1:
 # A = 4
 # B = 4
# Example Output
# Output 1: 13
# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
    
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 D Z 5 6 7 8
# 1 2 3 C B 6 7 8
# 1 2 G 4 5 6 7 8
# 1 2 3 4 5 6 F E
# 1 2 3 4 5 6 7 A

# A, B = 8, 8
# A, B = 5, 5 
# A, B = 7, 8
def solve(A, B):
    row_right   = 8 - B
    col_up      = A - 1
    col_down    = 8 - A
    row_left    = B - 1
    
    quad_1 = min(row_right, col_up)
    quad_2 = min(row_right, col_down)
    quad_3 = min(row_left, col_down)
    quad_4 = min(row_left, col_up)
    # print(quad_1, quad_2, quad_3, quad_4)
    return quad_1 + quad_2 + quad_3 + quad_4
    
# solve(A, B)
