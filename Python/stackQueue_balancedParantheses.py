# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:44:10 2022

@author: USER
"""

# Problem Description

# Given a string A consisting only of '(' and ')'.

# You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.

# Problem Constraints
# 1 <= |A| <= 105

# Input Format
# First argument is an string A.

# Output Format
# Return 1 if parantheses in string are balanced else return 0.

# Example Input
# Input 1:
  A = "(()())"
# Input 2:
  A = "(()"

# Example Output
# Output 1:
#  1
# Output 2:
#  0
# Example Explanation
# Explanation 1:

#  Given string is balanced so we return 1
# Explanation 2:

#  Given string is not balanced so we return 0
 
# temp = [1,2,3,4,5]
# temp.pop()
# class Solution:
    # @param A : string
    # @return an integer
    # def solve(self, A):'
def solve(A):
    stack_list = list()
    for i in A:
        if i == "(":
            stack_list.append(i)
        else:
            if i != ")":
                return 0
            if len(stack_list) == 0 :
                return 0
            stack_list.pop()                
    if len(stack_list) == 0:
        return 1
    else:
        return 0
solve(A)        


# Editorial:
# def solveQ(A):
#     stk=[]
#     for a in A:
#         if(a=='('):
#             stk.append(a)
#             continue
#         if(len(stk)==0):
#             return False
#         if(a==')'):
#             x=stk[-1]
#             stk.pop(-1)
#             if(x!='('):
#                 return False
#     if(len(stk)==0):
#         return True
#     return False
        
# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
#         if(solveQ(A)==False):
#             return 0
#         return 1

# class Solution {
#     def solve(A: String): Int  = {
#         var openBrackets = 0
        
#         for (c <- A) {
#             c match{
#                 case '(' => openBrackets += 1
#                 case ')' => if (openBrackets == 0) return 0 else openBrackets -= 1
#             }
#         }
#         return if (openBrackets > 0)  0 else 1
#     }
# }

# int Solution::solve(string A) 
# {
#     stack<int> s;
#     for(int i=0;i<A.size();i++)
#     {
#         if(A[i]=='(')
#         {
#             s.push(i);
#         }
#         else
#         {
#             if(s.empty())
#             {
#                 return 0;
#             }
#             s.pop();
#         }
#     }
#     return s.empty();
    
# }
# /**
#  * @input A : String
#  * 
#  * @Output Integer
#  */
# func solve(A string )  (int) {
#     stack := []byte{}
    
#     for _, val := range A {
#         if val == '(' {
#             stack = append(stack, '(')
#         } else {
#             if len(stack) == 0 {
#                 return 0
#             }
            
#             stack = stack[0:len(stack)-1]
#         }
#     }
    
#     if len(stack) > 0 {
#         return 0
#     }
    
#     return 1
# }
