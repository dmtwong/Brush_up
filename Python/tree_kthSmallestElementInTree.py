# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:39:24 2023

@author: USER
"""
##########
# New error when running the function recursively : NameError: name 'kthsmallest' is not defined
##########
# Problem Description
 
# Given a binary search tree, write a function to find the kth smallest element in the tree.
# NOTE: You may assume 1 <= k <= Total number of nodes in BST

# Input Format
# The first argument is the root node of the binary tree.
# The second argument B is an integer equal to the value of k.

# Output Format
# Return the value of the kth smallest node.

# Example Input
#   2
#  / \
# 1   3
# and k = 2

# Example Output
# 2

# Example Explanation
# As 2 is the second smallest element in the tree.

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None        
        
# class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
# 	def kthsmallest(self, A, B):
def kthsmallest(A, B): 
    try:
        print(A.val, B)
    except:
        print(B, 'no val')
    if (A == None):
        return None    
    left_node = A.left
    right_node = A.right
    print('now enter left')
    left = kthsmallest(left_node, B)
    try:
        print(left)
        print(left.val)
    except:
        print('left is None!!')
    if (left != None):
        return left 
    B -= 1
    if (B == 0):
        return A    
    print('now enter right')
    return kthsmallest(right_node, B)

x1 = TreeNode(2)
x2 = TreeNode(1)
x3 = TreeNode(3)
x1.left = x2
x1.right = x3
x1.val
x1.left.val
x1.right.val
temp = kthsmallest(x1, 2)
temp.val

# 		 1
# 		/ \ 
# 	  2    3
# 		  /
# 		4
# 		 \
# 		  5

x1 = TreeNode(1)
x2 = TreeNode(2)
x3 = TreeNode(3)
x4 = TreeNode(4)
x5 = TreeNode(5)
x1.left = x2
x1.right = x3
x3.left = x4
x4.right = x5
temp = kthsmallest(x1, 1)
temp.val
