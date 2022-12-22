# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:40:03 2022

@author: mingt
"""
# Print concentric rectangular pattern in a 2d matrix. 
# Let us show you some examples to clarify what we mean.

# Example 1:
# Input: A = 4.

# Output:

# 4 4 4 4 4 4 4 i = 0 (A * 2 ) - 1
# 4 3 3 3 3 3 4 beside first and last row first and last column everything -1  
# 4 3 2 2 2 3 4 until i = 3 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 
# Example 2:

# Input: A = 3.

# Output:
# 3 3 3 3 3 
# 3 2 2 2 3 
# 3 2 1 2 3 
# 3 2 2 2 3 
# 3 3 3 3 3 

# 2 2 2  
# 2 1 2 
# 2 2 2 

# 1


# The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

# You will be given A as an argument to the function you need to implement, and you need to return a 2D array.

# 0, 3, 6
# class Solution:
    # @param A : integer
    # @return a list of list of integers
    # def prettyPrint(self, A):

def prettyPrint(A):
    n_Mat = A*2 - 1
    result = list()     
    
    for i in range(A):
        cur_row = [] 
        ix = A 
        for j in range(i):
            cur_row.append(ix)
            ix -= 1                
        for k in range(n_Mat - 2 * i):
            cur_row.append(A - i)
        ix = A - i + 1
        for l in range(i):
            cur_row.append(ix)
            ix += 1            
        result.append(cur_row) 
    
    for i in range(A-2, -1, -1):
        # print(i)
        result.append(result[i][:])
        
    return result

prettyPrint(4)
