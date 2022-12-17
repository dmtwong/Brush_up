# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:09:29 2022

@author: USER
"""

# Problem Description

# Given an integer array A of size N. You need to count the number of special elements in the given array.
# A element is special if removal of that element make the array balanced.
# Array will be balanced if sum of even index element equal to sum of odd index element.


# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <= 109

# Input Format
# First and only argument is an integer array A of size N.

# Output Format
# Return an integer denoting the count of special elements.

# Example Input
# Input 1:
A = [2, 1, 6, 4]
# Input 2:
A = [5, 5, 2, 5, 8]
# Example Output
# Output 1: 1
# Output 2: 2

# Example Explanation
# Explanation 1:

#  After deleting 1 from array : {2,6,4}
#     (2+4) = (6)
#  Hence 1 is the only special element, so count is 1
# Explanation 2:

#  If we delete A[0] or A[1] , array will be balanced
#     (5+5) = (2+8)
#  So A[0] and A[1] are special elements, so count is 2.

# class Solution:
    # @param A : list of integers
    # @return an integer
    # def solve(self, A):
# solve(A)    

def solve(A):
    n_A = len(A)
    # corner case:
    if n_A == 1:
        return 1
    elif n_A == 2:
        return 0
    
    sum_odd, sum_even = 0, 0
    
    for i in range(n_A):
        if (i % 2 == 0):
            sum_even += A[i]
        else:
            sum_odd += A[i]
    
    cur_odd, cur_even = 0, A[0]
    
    result = 0
    temp_sum_even = 0
    temp_sum_odd = 0
    
    for j in range(1, n_A - 1):
        if j % 2 == 1:
            # print(j, A[j], cur_odd, cur_even, sum_odd, sum_even)
            cur_odd += A[j]
            temp_sum_even = cur_even + sum_odd - cur_odd 
            temp_sum_odd = cur_odd + sum_even - cur_even - A[j]
        else:
            # print(j, A[j], cur_odd, cur_even, sum_odd, sum_even)
            cur_even += A[j]
            temp_sum_odd  = cur_odd + sum_even - cur_even
            temp_sum_even = cur_even + sum_odd - cur_odd - A[j]
        
        if (temp_sum_odd == temp_sum_even):
            result += 1
    
    if sum_odd == sum_even - A[0]:
        result += 1
    
    if (n_A % 2 == 1):
        if (sum_odd == sum_even - A[n_A - 1]):
            result += 1
    else:
        if (sum_even == sum_odd - A[n_A - 1]):
            result += 1
    return result

# Suggested Solution:
#     class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         n = len(A)
#         odd = 0
#         even = 0
#         leftOdd = [0] * n
#         rightOdd = [0] * n
#         leftEven = [0] * n
#         rightEven = [0] * n
#         for i in range(n):
#             leftOdd[i] = odd
#             leftEven[i] = even
#             if(i%2 == 0):
#                 even += A[i]
#             else:
#                 odd += A[i]
        
#         odd = 0
#         even = 0
#         for i in range(n-1, -1, -1):
#             rightOdd[i] = odd
#             rightEven[i] = even
#             if(i%2 == 0):
#                 even += A[i]
#             else:
#                 odd += A[i]
        
#         ans = 0
#         for i in range(n):
#             if(leftOdd[i] + rightEven[i] == leftEven[i] + rightOdd[i]):
#                 ans += 1
            
#         return ans
# C++
# int Solution::solve(vector<int> &A) {
#     int n = A.size();
#     int odd = 0, even = 0;
#     int leftOdd[n], rightOdd[n];
#     int leftEven[n], rightEven[n];
#     for(int i = 0;i < n; i++){
#         leftOdd[i] = odd;
#         leftEven[i] = even;
#         if(i%2 == 0)
#             even += A[i];
#         else
#             odd += A[i];
#     }
#     odd = 0;
#     even = 0;
#     for(int i = n-1; i >= 0; i--){
#         rightOdd[i] = odd;
#         rightEven[i] = even;
#         if(i%2 == 0)
#             even += A[i];
#         else
#             odd += A[i];
#     }
#     int ans = 0;
#     for(int i = 0; i < n; i++){
#         if(leftOdd[i] + rightEven[i] == leftEven[i] + rightOdd[i]){
#             ans++;
#         }
#     }
#     return ans;
# }

# Scala:
#     class Solution {
#     def solve(A: Array[Int]): Int  = {
#         var totalEven = 0
#         var totalOdd = 0
#         for(i <- A.indices) {
#             if(i % 2 ==0)
#                 totalEven += A(i)
#             else
#                 totalOdd += A(i)
#         }

#         var count = 0
#         var sumEven = 0
#         var sumOdd = 0
#         for(i <- A.indices) {
#             var even = sumEven
#             var odd = sumOdd
#             if(i %2 == 0) {
#                 even += totalOdd - sumOdd
#                 odd += totalEven - sumEven - A(i)
#                 sumEven += A(i)
#             }
#             else {
#                 even += totalOdd - sumOdd - A(i)
#                 odd += totalEven - sumEven
#                 sumOdd += A(i)
#             }
#             if(even == odd)
#                 count += 1
#         }
#         count
#     }
# }
#     /**
#  * @input A : Integer array
#  * 
#  * @Output Integer
#  */
# func solve(A []int )  (int) {
#     lenA := len(A)
#     var evenComplete,oddComplete int
#     for i:=0;i<lenA;i++{
#         if i%2 == 0{
#             evenComplete = evenComplete + A[i]
#         }else{
#             oddComplete = oddComplete + A[i]
#         }
#     }
    
#     var evenSoFar, oddSoFar int
#     var addTo *int
#     num := 0
#     for i:=0; i<lenA; i++{
#         if i%2 == 0{
#             evenComplete = evenComplete - A[i]
#             addTo = &evenSoFar     
#         }else{
#             oddComplete = oddComplete - A[i]
#             addTo = &oddSoFar
#         }
#         if (evenComplete + oddSoFar) == (oddComplete + evenSoFar){
#             num++
#         }
#         *addTo = *addTo + A[i]
#     }
    
#     return num
    
# }
