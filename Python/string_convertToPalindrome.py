# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:15:19 2023

@author: USER
"""

# Problem Description

# Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

# If it is possible then return 1 else return 0.

# Problem Constraints
# 3 <= |A| <= 105

#  A[i] is always a lowercase character.

# Input Format
# First and only argument is an string A.

# Output Format
# Return 1 if it is possible to convert A to palindrome by removing exactly one character else return 0.

# Example Input
# Input 1:
 A = "abcba"
# Input 2:
 A = "abecbea"

# Example Output
# Output 1: 1
# Output 2: 0

# Example Explanation
# Explanation 1:
#  We can remove character ‘c’ to make string palindrome
# Explanation 2:
#  It is not possible to make this string palindrome just by removing one character 
# class Solution:
    # @param A : string
    # @return an integer
    # def solve(self, A):
def solve(A):  
    n_A = len(A)
    count = 0
    # def compare(ix_A_1, ix_A_2):
    #     len_2 = ix_A_2 - ix_A_1
    #     if len_2 == 0:
    i = 0
    j = n_A -1 
    def compare(sub_A, sub_i, sub_j):
        while sub_i < sub_j:
            if sub_A[sub_i] != sub_A[sub_j]:
                return False
            sub_i += 1
            sub_j -= 1
        return True
    
    while i < j:
        # print(i, j)
        if A[i] == A[j]:
            # print('matched')
            i += 1
            j -= 1
        else:
            # print(compare(A, i + 1, j))
            # print(compare(A, i, j-1))
            if compare(A, i + 1, j):
                return 1
            if compare(A, i, j - 1):
                return 1
            return 0
    return 1

    
    # while i < n_A // 2 and i < n_A - j - 1:
    #     print(i, A[i], A[n_A - j - 1])
    #     right = n_A - j - 1                
    #     if (A[i] != A[right]):
    #         print('failed!')
    #         if A[i+1] != A[right] and A[i] != A[right - 1]:
    #             print('here')
    #             return 0
    #         elif A[i+1] == A[right]:
    #             print('there')
    #             i += 1
    #             j += 2
    #             count += 1
    #             continue
    #         elif A[i] == A[right - 1]:
    #             print('!')
    #             i += 1
    #             j += 2
    #             count += 1
    #     else:
    #         i += 1
    #         j += 1
            
    # if (count >= 2):
    #     return 0
    # else:
    #     return 1
            
solve(A)
A = 'phmjjmap'
A = "qifjhwvhvohmnnibd"
A = 'jvwcfflufnztzreji'
A = "cnvinhc"
A = "abaccab"

# Scala:
#     class Solution {

#     def isPalindrome(A: String, left: Int, right: Int): Boolean = {
#         var left2 = left
#         var right2 = right
#         while(right2 >= left2 && A.charAt(left2) == A.charAt(right2)){
#             left2 += 1
#             right2 -= 1
#         }
#         return right2 < left2
#     }

#     def solve(A: String): Int  = {
    
#         var left: Int = 0
#         var right: Int = A.length - 1
#         while(right >= left && A.charAt(left) == A.charAt(right)){
#             left += 1
#             right -= 1
#         }
#         if(right < left || isPalindrome(A, left + 1, right) || isPalindrome(A, left, right - 1))
#             return 1
#         else
#             return 0
#     }
# }

# GO:
#     /**
#  * @input A : String
#  * 
#  * @Output Integer
#  */
# func solve(A string )  (int) {
#     l,r:=0,len(A)-1
#     n:=len(A)
#     var temp string
#     for l<=r{
#         if A[l] != A[r]{
#             temp = A[:l]
#             if l+1<n{
#                 temp += A[l+1:]
#             }
#             if temp==reverse(temp){
#                 return 1
#             }
#             temp = A[:r]
#             if r+1<n{         
#                 temp += A[r+1:]
#             }
#             if temp==reverse(temp){
#                 return 1
#             }else{
#                 return 0
#             }
#         }else{
#             l++
#             r--
#         }
#     }
#     if A==reverse(A){
#         return 1
#     }else{
#         return 0
#     }
#     return 0
# }

# func reverse(A string) string{
#     run := []rune(A)
#     l,r := 0,len(A)-1
#     for l<r{
#         run[l],run[r] = run[r],run[l]
#         l++
#         r--
#     }
#     return string(run)
# }
