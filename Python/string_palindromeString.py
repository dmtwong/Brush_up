# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:46:40 2022

@author: USER
"""

# Problem Description
#   Given a string, determine if it is a palindrome. While checking for a palindrome, 
#   you have to ignore spaces, case, and all special characters; i.e. consider only alphanumeric characters.

# Check the sample test case for reference.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# Problem Constraints
# 1 <= |A| <= 106

# Input Format
# The first argument is a string A.

# Output Format
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


# Example Input
# Input 1:
A = "A man, a plan, a canal: Panama"
# Input 2:
A = "race a car"


# Example Output
# Output 1:
# 1
# Output 2:
# 0


# Example Explanation
# Explanation 1:
# The input string after ignoring spaces, and all special characters is "AmanaplanacanalPanama" 
# which is a palindrome after ignoring the case.
# Explanation 2:
# The input string after ignoring spaces, and all special characters is "raceacar" which is not a palindrome
# class Solution:
#     # @param A : string
#     # @return an integer
#     def isPalindrome(self, A):
def isPalindrome(A):
    import string
    n_A = len(A)
    charCatDigit = string.ascii_lowercase + string.digits
    # A = 'aBc x'
    A = A.lower()
    list_charAfterTrimed = []
    for i in range(n_A):
        if charCatDigit.find(A[i]) != -1:
            list_charAfterTrimed.append(A[i])
            
    # isPal = True
    n_trimed = len(list_charAfterTrimed)
    mid_trimed = n_trimed // 2       # 10 --> 5 01234 56789 11-> 01234 5 678910
    for i in range(mid_trimed):
        for j in range(n_trimed-1, i, -1):
            if list_charAfterTrimed[i] == list_charAfterTrimed[j-i]:
                # i+= 1                
                break
            if list_charAfterTrimed[i] != list_charAfterTrimed[j-i]:
                # print(list_charAfterTrimed)
                # print(i, j)
                # print(list_charAfterTrimed[i], list_charAfterTrimed[j])
                # isPal = False
                return 0
    return 1
            
isPalindrome(A)

# Suggested Solution:
#     class Solution:
#     # @param A : string
#     # @return an integer
#     def isPalindrome(self, A):
#         A = A.lower()
#         n = len(A)
#         low = 0
#         high = n - 1
#         ret = 1
#         while low <= high:
#             if A[low] == A[high]:
#                 low += 1
#                 high -= 1
#                 continue
#             if str(A[low]).isalnum() and str(A[high]).isalnum():
#                 ret = 0
#                 break
#             elif str(A[high]).isalnum():
#                 low += 1
#             else:
#                 high -= 1
#         return ret
# class Solution {
#     def isPalindrome(A: String): Int  = {
#         if (A.isEmpty()) {
#         	return 1;
#         }
#         var head: Int = 0;
#         var tail: Int = A.length()-1;
#         var cHead: Char = 'a';
#         var cTail: Char = 'a';
#         while(head <= tail) {
#         	cHead = A.charAt(head);
#         	cTail = A.charAt(tail);
#         	if (!Character.isLetterOrDigit(cHead)) {
#         		head = head + 1;
#         	} else if(!Character.isLetterOrDigit(cTail)) {
#         		tail = tail - 1;
#         	} else {
#         		if (Character.toLowerCase(cHead) != Character.toLowerCase(cTail)) {
#         			return 0;
#         		}
#         		head = head + 1;
#         		tail = tail - 1;
#         	}
#         }
        
#         return 1;
#     }
# }
                
#                 int Solution::isPalindrome(string A) {
#     int i = 0, j = (int)A.size() - 1;
#     while(i < j)
#     {
#         while(i < j && !isalnum(A[i])) i++;
#         while(i < j && !isalnum(A[j])) j--;
#         if (toupper(A[i]) != toupper(A[j])) return false; 
#         i++;
#         j--;
#     }
#     return true;
# }
#                 /**
#  * @input A : String
#  * 
#  * @Output Integer
#  */
# func isPalindrome(A string )  (int) {
#     i := 0
#     j := len(A) - 1
    
#     for {
#         for i < j && !isAlphaNumeric(A[i]) {
#             i++
#         }
        
#         for i < j && !isAlphaNumeric(A[j]) {
#             j--
#         }
        
#         if i > j {
#             return 1
#         }
        
#         if !sameIgnoreCase(A[i], A[j]) {
#             return 0
#         }
        
#         i++
#         j--
#     }
    
#     return 0
# }

# func isAlphaNumeric(a byte) bool {
#     return (a >= 'A' && a <= 'z') || (a >= '0' && a <= '9')
# }

# func sameIgnoreCase(a, b byte) bool {
#     if a >= 'a' && a <= 'z' {
#         a -= 32
#     }
#     if b >= 'a' && b <= 'z' {
#         b -= 32
#     }
    
#     return a == b
# }
