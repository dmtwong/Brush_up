# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 19:10:06 2022

@author: USER
"""
# Problem Description
 
# Determine whether an integer is a palindrome. Do this without extra space.

# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) 
# is x with its digit reversed. Negative numbers are not palindromic.

# Problem Constraints
# INT_MIN <= A <= INT_MAX

# Input Format
# The first argument is an integer A.

# Output Format
# Return 1 if A is a Palindrome Integer else return 0.

# Example Input
# Input 1:
A = 12121
# Input 2:
A = 123

# Example Output
# Output 1:
# 1
# Output 2:
# 0

# Example Explanation
# Explanation 1:
#  12121 when reversed will be 12121, and 12121 = 12121, hence a palindrome number.

# Explanation 2:
#  123 when reversed will be 321, and 123 != 321, hence not a palindrome number
 
# class Solution:
	# @param A : integer
	# @return an integer
# 	def isPalindrome(self, A):
def isPalindrome(A):
    if A < 0:
        return 0
    str_A = str(A)
    
    def isPal(str_int):
        if len(str_int) <= 1:
            return 1
        result = str_int[0] == str_int[-1] and isPal(str_int[1:-1])
        return result
    if isPal(str_A) == True:
        return 1
    else: 
        return 0

isPalindrome(A)

# # Suggested:
#     class Solution:
#     # @param A : integer
#     # @return an integer
#     def isPalindrome(self, A):
#         B = str(A)
#         if B == B[::-1]:
#             return 1
#         else:
#             return 0
# class Solution {
#  def isPalindrome(A: Int): Int  = {
#     if(A <0) return 0
#     var reverse: Long = 0
#     var temp = A
#     while(temp > 0) {
#       reverse = reverse * 10 + temp % 10
#       temp = temp/10
#     }
#     if(reverse == A) 1 else 0
#   }
# }
# int Solution::isPalindrome(int A) {
#     assert(A >= INT_MIN && A <= INT_MAX);
#     string a = to_string(A);
#     string b = a;
#     reverse(b.begin(), b.end());
#     if(a == b) return 1;
#     else return 0;
# }
# /**
#  * @input A : Integer
#  * 
#  * @Output Integer
#  */
# func ReverseInteger(A int) int {
#     rev := 0
#     for A != 0 {
#         lastDigit := A % 10
#         rev = rev*10 + lastDigit
#         A = A / 10
#     }
#     return rev
# }

# func isPalindrome(A int) int {
#     if A < 0 {
#         return 0
#     }
#     rev := ReverseInteger(A)
#     if rev == A {
#         return 1
#     }
#     return 0
# }