# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:11:35 2022

@author: USER
"""

# Problem Description
 
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Please make sure you try to solve this problem without using library functions. 
# Make sure you only traverse the string once.


# Problem Constraints
# 1 <= |A| <= 106

# Input Format
# The first argument is a string A

# Output Format
# Return an integer denoting the length of the last word in the string.

# Example Input
# Input 1:
A = " hello world "
Input 2:
A = "InterviewBit"

# Example Output
# Output 1:
# 5
# Output 2:
# 12

# Example Explanation
# Explanation 1:
# "world" is the last word of size 5
# Explanation 2:
# "InterviewBit" is the last word of size 12

# class Solution:
	# @param A : string
	# @return an integer
# 	def lengthOfLastWord(self, A):
def lengthOfLastWord(A):
    list_A = A.split()
    n_list_A = len(list_A)
    # list_A = list_A[::-1]
    for ix_cur_word in range(n_list_A - 1, -1, -1):
        n_cur_word = len(list_A[ix_cur_word])
        if n_cur_word == 0:
            if ix_cur_word > 0:
                pass
            else:
                return 0
        return n_cur_word
    return 0
                
lengthOfLastWord(A)       

# Suggested:
    
# class Solution:
#     # @param A : string
#     # @return an integer
#     def lengthOfLastWord(self, A):
#         l=len(A)
#         if (l==0):
#             return 0
        
#         i=l-1
#         while (i>=0 and A[i]==" "):
#             i-=1
        
#         cnt=0
#         while (i>=0 and A[i]!=" "):
#             cnt+=1
#             i-=1
        
#         return cnt
# Scala
# class Solution {
#     def lengthOfLastWord(A: String): Int  = {
#       var isChar = false
#       var len = 0
#       for {
#         i <- A.indices
#         ch = A.charAt(A.length - i - 1)
#       } {
#         if (ch.isLetter) {
#           isChar = true
#           len += 1
#         } else {
#           if (isChar) return len
#         }
#       }
#       len
#     }
# }

#             GO:
# func lengthOfLastWord(word string ) (int) {
# 	
# 	length := 0
# 	state := 0
# 	for i := 0; i < len(word); i++ {
# 		isLetter := isLetter(word[i])
# 		
# 		if state == 0 && isLetter {
# 			length = 1
# 			state = 1
# 		} else if state == 1 && isLetter {
# 			length++
# 		} else if state == 1 && !isLetter {
# 			state = 0
# 		}
# 	}
# 	return length
# }

# func isLetter (char byte) bool {
# 	if (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') {
# 		return true
# 	}
# 	
# 	return false
# }