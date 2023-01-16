# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:36:24 2023

@author: USER
"""

# Problem Description
# Given a string A consisting of lowercase characters.
# Check if characters of the given string can be rearranged to form a palindrome.
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

# Problem Constraints
# 1 <= |A| <= 105
# A consists only of lower-case characters.

# Input Format
# First argument is an string A.

# Output Format
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

# Example Input
# Input 1:
 A = "abcde"
# Input 2:
 A = "abbaee"
# Example Output
# Output 1: 0
# Output 2: 1

# Example Explanation
# Explanation 1:
#  No possible rearrangement to make the string palindrome.
# Explanation 2:
#  Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.
# class Solution:
    # @param A : string
    # @return an integer
    # def solve(self, A):
def solve(A):
    n_A = len(A)
    isEven = n_A % 2 == 0
    processing = []
    for i in range(n_A):
        curr_char = A[i]
        if (curr_char in processing):
            processing.remove(A[i])
        else:
            processing.append(curr_char)
    n_pro = len(processing)
    # print(processing, isEven)
    if (isEven and n_pro == 0) or (not isEven and n_pro == 1):
        return 1
    else:
        return 0
# A
solve(A)

# # function to check whether characters 
# # of a string can form a palindrome  
# def canFormPalindrome(st) : 
  
#     # Create a count array and initialize   
#     # all values as 0 
#     count = [0] * (26) 
  
#     # For each character in input strings, 
#     # increment count in the corresponding 
#     # count array 
#     for i in range( 0, len(st)) : 
#         count[ord(st[i])-ord('a')] = count[ord(st[i])-ord('a')] + 1
  
#     # Count odd occurring characters 
#     odd = 0
      
#     for i in range(0, 26) : 
#         if (count[i] & 1) : 
#             odd = odd + 1
  
#         if (odd > 1) : 
#             return False
              
#     # Return true if odd count is 0 or 1,  
#     return True
# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
#         if(canFormPalindrome(A)):
#             return 1
#         return 0

# /**
#  * @input A : String
#  * 
#  * @Output Integer
#  */
# func solve(A string )  (int) {
#     m := make(map[rune]int)
#     isOdd := len(A) % 2
#     oddChar := 0
#     for _, r := range A {
#         m[r]++
#     }
#     for _, v := range m {
#         if v % 2 == 1 {
#             oddChar++
#         }
#         if oddChar > isOdd {
#             return 0
#         }
#     }
#     return 1
# }

# int Solution::solve(string A) {
#   int hashMap[26] = {0};
#   for (char a: A)
#     hashMap[a - 'a']++;
#   int odd = 0;
#   for (int a: hashMap)
#     if (a % 2)
#       odd++;
#   if (odd > 1)
#     return 0;
#   return 1;
# }