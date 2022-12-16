# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 22:42:07 2022

@author: USER
"""

class Solution:
    # @param A : string
    # @return an integer
    # def titleToNumber(self, A):
import string        
def titleToNumber(A):
    result = 0
    
    len_A = len(A)
    deg_A = len_A
    full_char = string.ascii_uppercase
    
    for i in range(len_A):
        cur = full_char.find(A[i])
        result += 26**(deg_A - 1) * (cur + 1)
        deg_A -= 1
    return result

    
titleToNumber('A')
titleToNumber('AB')
