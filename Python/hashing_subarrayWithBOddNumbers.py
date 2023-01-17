# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:33:57 2023

@author: USER
"""

# Problem Description
# Given an array of integers A and an integer B.
# Find the total number of subarrays having exactly B odd numbers.
# Problem Constraints
# 1 <= length of the array <= 105
# 1 <= A[i] <= 109
# 0 <= B <= A
# Input Format
# The first argument given is the integer array A.
# The second argument given is integer B.

# Output Format
# Return the total number of subarrays having exactly B odd numbers.

# Example Input
# Input 1:
 A = [4, 3, 2, 3, 4]
 B = 2
 # B = 1
# Input 2:
 A = [5, 6, 7, 8, 9]
 B = 3
# Example Output
# Output 1:
#  4
# Output 2:
#  1
# Example Explanation
# Explanation 1:
#  The subarrays having exactly B odd numbers are:
#  [4, 3, 2, 3], [4, 3, 2, 3, 4], [3, 2, 3], [3, 2, 3, 4]
# Explanation 2:
#  The subarrays having exactly B odd numbers is [5, 6, 7, 8, 9]
# class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # def solve(self, A, B):
def solve(A, B):
    n_A = len(A)
    count = 0
    # for i in range(n_A - B + 1):
    #     curr_odd = 0
    #     for j in range(i, n_A):
    #         if (A[j] % 2 == 1):
    #             # print('detected odd!', A[j])
    #             curr_odd += 1
    #         if curr_odd > B:
    #             # print('too many odd, have a new start for next subarray')
    #             break
    #         if curr_odd == B:
    #             count += 1
    # odd_ind = [0] * n_A
    # for i in range(n_A):
    #     if (A[i] % 2 == 1):
    #         odd_ind[i] = 1
    # for i in range(n_A - B + 1):
    #     curr_odd = 0
    #     isBreak = False
    #     j = i
    #     while not isBreak and j < n_A:
    #         curr_odd += odd_ind[j]
    #         j += 1
    #         if curr_odd == B:
    #             count += 1
    #         elif curr_odd > B:
    #             isBreak = True                       
    # return count

    
    odd_ind = [0] * (n_A + 1)
    ix = 0
    for i in range(n_A):
        odd_ind[ix] += 1        
        if (A[i] % 2 == 1):
            ix += 1
        if (ix >= B):
            count += odd_ind[ix - B]
    return count

A
A = [ 5, 5, 1, 3, 1 ]
B = 0
solve(A, B)

# int Solution::solve(vector<int> &A, int B) {
#     int n = A.size();
#     int count = 0;
#     int prefix[n+1];
#     memset(prefix, 0, sizeof(prefix));
#     int odd = 0;
#     // traverse in the array
#     for (int i = 0; i < n; i++)
#     {

#       prefix[odd]++;
#       // if array element is odd
#       if (A[i] & 1)
#           odd++;

#       // when number of odd elements>=M
#       if (odd >= B)
#           count += prefix[odd - B];
#     }
#     return count;
    
# }

# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# func solve(A []int , B int )  (int) {
#     if len(A) < B {
#         return 0
#     }
#     odd := make([]int, 0, 10)

#     for i, v := range A {
#         if v%2 != 0 {
#             odd = append(odd, i)
#         }
#     }

#     fEven := 0
#     lEven := -1
#     i := 0
#     sum := 0

#     for i+B <= len(odd) {
#         if B > 0 {
#             if i == 0 {
#                 fEven = odd[i]
#             } else {
#                 fEven = odd[i] - odd[i-1] - 1
#             }

#             if i+B == len(odd) {
#                 lEven = len(A) - odd[i+B-1] - 1
#             } else {
#                 lEven = odd[i+B] - odd[i+B-1] - 1
#             }
#             sum += fEven + fEven*lEven + lEven + 1
#         } else {
#             if i == len(odd) {
#                 if len(odd) > 0 {
#                     fEven = len(A) - 1 - odd[i-1]
#                 } else {
#                     fEven = len(A)
#                 }
#             } else if i == 0 {
#                 fEven = odd[i]
#             } else {
#                 fEven = odd[i] - odd[i-1] - 1
#             }
#             sum += (fEven * (fEven + 1)) / 2
#         }
#         i++
#     }
#     return sum
# }

