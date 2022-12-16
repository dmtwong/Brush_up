# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 18:56:58 2022

@author: USER
"""

# Given an integer array A of size N.
# You have to pick exactly B elements from either left or right end of the array A to get the maximum sum.
# Find and return this maximum possible sum.
# NOTE: Suppose B = 4 and array A contains 10 elements then
# You can pick the first four elements or can pick the last four elements or can 
# pick 1 from the front and 3 from the back etc. you need to return the maximum possible sum of elements you can pick.
# Problem Constraints
# 1 <= N <= 105
# 1 <= B <= N
# -103 <= A[i] <= 103

# Input Format
# First argument is an integer array A.
# Second argument is an integer B.

# Output Format
# Return an integer denoting the maximum possible sum of elements you picked.

# Example Input
# Input 1:
 A = [5, -2, 3 , 1, 2]
 B = 3
# Input 2:
 A = [1, 2]
 B = 1

# Example Output
# Output 1: 8
# Output 2: 2

# Example Explanation
# Explanation 1:
#  Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
# Explanation 2:
#  Pick element 2 from end as this is the maximum we can get
 

    def solve(A, B):
        num_right = 0
        cur_max = sum(A[:B])
        left_tot = cur_max
        right_tot = 0
        prev_tot = cur_max
        left_ix = B-1
        len_A = len(A)
        right_ix = len_A - 1
        room = max(len_A - B + 1, B)
    
        for i in range(room):
            # print(i, left_ix)
            if left_ix == -1:
                break
            # print(cur_max) # R1: 6 R2: 
            left_tot -= A[left_ix] # R1: 3
            right_tot += A[right_ix]
            # print(left_tot, right_ix) 
            cur_tot = left_tot + right_tot # R1: 3+2 = 5
            # print(cur_tot, right_ix) 
            if cur_tot > cur_max: # R1: 5 not > 6
                # print(cur_max, cur_tot)            
                cur_max = cur_tot
            left_ix -= 1 # R1: 1
            right_ix -= 1  #R1: 3
        return cur_max
    
A = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
B = 48
solve(A, B)

# Suggested Solution:
    # class Solution:
    # # @param A : list of integers
    # # @param B : integer
    # # @return an integer
    # def solve(self, A, B):
    #     n = len(A)
    #     suff = [0] * (n + 1)
    #     suff[n - 1] = A[n - 1]
    #     for i in range(n - 2, -1, -1):
    #         suff[i] = A[i] + suff[i + 1]
    #     prefSum = 0
    #     ans = suff[n - B]
    #     for i in range(B):
    #         prefSum = prefSum + A[i]
    #         suffSum = suff[n - B + i + 1]
    #         ans = max(ans, prefSum + suffSum)
    #     return ans
# # Scala
# # class Solution {
# #   def solve(A: Array[Int], B: Int): Int  = {
# #     val initialSum = A.take(B).sum
# #     var maxSum = initialSum
# #     var curSum = initialSum
# #     for (i <- B - 1 to 0 by -1) {
# #       curSum = curSum - A(i) + A(A.length - 1 - (B - 1 - i))
# #       if (maxSum < curSum) maxSum = curSum
# #     }

# #     maxSum
# #   }
# # }
# c++
# int fun(vector < int > & A, int B) {
#   int n = A.size();
#   int suff[n + 1];
#   suff[n] = 0;
#   suff[n - 1] = A[n - 1];
#   for (int i = n - 2; i >= 0; i--)
#     suff[i] = A[i] + suff[i + 1];
#   int prefSum = 0;
#   int ans = suff[n - B];
#   for (int i = 0; i < B; i++) {
#     prefSum = prefSum + A[i];
#     int suffSum = suff[n - B + (i + 1)];
#     ans = max(ans, prefSum + suffSum);
#   }
#   return ans;
# }
# int Solution::solve(vector < int > & A, int B) {
#   return fun(A, B);
# }
# GO:
# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# import "math"
# func solve(A []int , B int )  (int) {
#     // Check if len of B is greater than A
#     left_sum := make([]int, B)
#     right_sum := make([]int, B)
    
#     sum := 0
#     for i:= 0; i<B; i++ {
#         sum += A[i]
#         left_sum[i] = sum
#     }
    
#     sum = 0
#     for i:=0; i<B; i++ {
#         sum += A[len(A) - 1 - i]
#         right_sum[B - 1 - i] = sum
#     }
    
#     max_sum := math.MinInt64
    
#     for i:= -1; i <B; i++ {
#         var left int
#         if i == -1 {
#             left = 0
#         } else {
#             left = left_sum[i]
#         }
#         var right int
#         if i + 1 == B {
#             right = 0
#         } else {
#             right = right_sum[i+1]
#         }
#         curr := left + right
#         if curr > max_sum {
#             max_sum = curr
#         }
#     }
#     return max_sum
# }
