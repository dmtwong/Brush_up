# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:58:38 2023

@author: USER
"""

##############################################
# Still need to be fixed
##############################################

# Problem Description 
# An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each string may be an integer or an operator.
# Problem Constraints
# 1 <= N <= 105
# Input Format
# The only argument given is string array A.
# Output Format
# Return the value of arithmetic expression formed using reverse Polish Notation.
# Example Input
# Input 1:
A =   ["2", "1", "+", "3", "*"]
# Input 2:
A = ["4", "13", "5", "/", "+"]
# Example Output
# Output 1:    9
# Output 2:    6

# Example Explanation
# Explaination 1:
#     starting from backside:
#     * : () * ()
#     3 : () * (3)
#     + : (() + ()) * (3)
#     1 : (() + (1)) * (3)
#     2 : ((2) + (1)) * (3)
#     ((2) + (1)) * (3) = 9
# Explaination 2:
#     + : () + ()
#     / : () + (() / ())
#     5 : () + (() / (5))
#     13 : () + ((13) / (5))
#     4 : (4) + ((13) / (5))
#     (4) + ((13) / (5)) = 6
# class Solution:
	# @param A : list of strings
	# @return an integer
# 	def evalRPN(self, A):
def evalRPN(A):
    def operHelper(x, y, oper):        
        if oper == '+':
            return x + y
        if oper == '-':
            return x - y
        if oper == '*':
            return x * y
        if oper == '/':
            # return x / y
            return x // y
    def priorty(oper):
        priority_dict = {}
        priority_dict['+'] = 1
        priority_dict['-'] = 1
        priority_dict['*'] = 2
        priority_dict['/'] = 2
        # return priority_dict[oper]
        try:
            result = priority_dict[oper]
        except:
            result = 0
        return result   
    val_list = []
    oper_list = []    
    i = 0       
    while i < len(A):
        isDigit = (A[i] in '0123456789')  
        # print(i, isDigit)
        if A[i] == ' ':
            i += 1
            isDigit = (A[i] in '0123456789')  
            continue
        elif A[i] == '(':
            oper_list.append(A[i])
        elif isDigit == True:
            curr_val = 0
            isDigit = (A[i] in '0123456789')  
            while (i < len(A) and isDigit == True):
                print(A[i])
                curr_val = (curr_val * 10) + int(A[i])
                i += 1            
                isDigit = (A[i] in '0123456789')  
                print(A[i], isDigit)
            val_list.append(curr_val)            
        elif A[i] == ')':        
            while len(oper_list) != 0 and oper_list[-1] != '(':          
                print('here', val_list, oper_list)    
                y = val_list.pop()
                x = val_list.pop()
                oper = oper_list.pop()                
                val_list.append(operHelper(x, y, oper))
                print(x, y, oper)
            oper_list.pop()
        else:
            while (len(oper_list) != 0 and priorty(oper_list[-1]) >= priorty(A[i])):      
                print('there', val_list, oper_list)                  
                y = val_list.pop()
                x = val_list.pop()
                oper = oper_list.pop()
                print(x, y, oper)
                val_list.append(operHelper(x, y, oper))
             
            oper_list.append(A[i])        
        i += 1     
    while len(oper_list) != 0:        
        y = val_list.pop()
        x = val_list.pop()
        oper = oper_list.pop()                
        val_list.append(operHelper(x, y, oper))
    print(val_list)
    return val_list[-1]

A =   ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
evalRPN(A)
 