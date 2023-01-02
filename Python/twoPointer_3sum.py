# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 21:14:46 2023

@author: USER
"""

# Problem Description
# Given an array A of N integers, find three integers in A such that the sum is 
# closest to a given number B. Return the sum of those three integers.
# Assume that there will only be one solution.

# Problem Constraints
# -108 <= B <= 108
# 1 <= N <= 104
# -108 <= A[i] <= 108

# Input Format
# First argument is an integer array A of size N.
# Second argument is an integer B denoting the sum you need to get close to.

# Output Format
# Return a single integer denoting the sum of three integers which is closest to B.

# Example Input
# Input 1:
A = [-1, 2, 1, -4]
B = 1
# Input 2: 
A = [1, 2, 3]
B = 6

# Example Output
# Output 1:2
# Output 2:6

# Example Explanation
# Explanation 1:
#  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
# Explanation 2:
#  Take all elements to get exactly 6.
# class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
# 	def threeSumClosest(self, A, B):
    
def threeSumClosest(A, B):
    n_A = len(A)
    A.sort()
    # smallest_diff = B
    result = None
    # def reachSecond(j, last):
        
    for i in range(n_A - 2):
        # print('first number is', A[i])
        # for j in range(1, n_A -2) 
        j = i + 1
        # for k in range(j + 1,)
        last_ix = n_A - 1
        
        while (j < last_ix):
            reset = True
            while reset:                 
                # print('second mber is', A[j], last_ix)            
                curr_sum = A[i] + A[j] + A[last_ix]
                curr_diff = abs(B - curr_sum) # 5
                if result == None:
                    result = curr_sum
                    smallest_diff = abs(B - result)
                if curr_sum == B:
                    return B
                
                if smallest_diff > curr_diff:
                    # print('is getting closer!', result, curr_sum)
                    result = curr_sum
                    smallest_diff = curr_diff
                elif curr_sum > B:
                    last_ix -= 1
                    if last_ix == j:
                        break
                    continue
                else:
                    break
            j += 1
    return result


A = [12, 3, 4, 1, 6, 9]
B = 24
A.sort()
A = [1, 2, 3, 4, 5]
B = 9
A = [ -6, 1, -4, -1, 8, -4, 9, 0, -3, 7, -3, 2, -4, -2, 3, -4, 10, 0, 9, 6, 1, 3, 4, 2 ]
sorted(A) # -6, 1, 2
B = -3
A = [ 7, -6, 2, 10 ]
B = 3

threeSumClosest(A, B) #3,9, 12

# Editorial:
#     class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def threeSumClosest(self, A, B):
#         n = len(A)
#         if n == 0:
#             return B
#         A.sort()
#         minDiff = 2147483648
#         ret = 0
#         for i in range(n):
#             j = i + 1
#             k = n - 1
#             while j < k :
#                 temp = A[i]+A[j]+A[k]
#                 diff = abs(temp-B)
#                 if diff == 0:
#                     return temp
#                 if diff < minDiff:
#                     minDiff = diff
#                     ret = temp
#                 if temp <= B:
#                     j += 1
#                 else:
#                     k -= 1
#         return ret
# class Solution {
#     def threeSumClosest(A: Array[Int], B: Int): Int  = {
#       import scala.collection.mutable.ArrayBuffer
#       val buff = ArrayBuffer[Int]()
#       val sorted = A.sorted
#       val len = A.length
#       for (i <- 0 until len - 2) {
#         var l = i + 1
#         var r = len - 1
#         while (l < r) {
#           val sum = sorted(i) + sorted(l) + sorted(r)
#           if (sum == B) return B
#           else {
#             buff.append(sum)
#             if (sum < B) l = l + 1
#             else r = r - 1
#           }
#         }
#       }
    
#       buff.minBy(p => math.abs(B - p))
#     }
# }
# int Solution:: threeSumClosest(vector<int> &num, int target) {
#     sort(num.begin(), num.end());
#     long long bestSum = 1000000000, sum = 0;
#     // Fix the smallest number in the three integers
#     for (int i = 0; i < num.size() - 2; i++) {
#         // Now num[i] is the smallest number in the three integers in the solution
#         int ptr1 = i + 1, ptr2 = num.size() - 1;
#         while (ptr1 < ptr2) {
#             sum = num[i] + num[ptr1] + num[ptr2];
#             if (abs(target - sum) < abs(target - bestSum)) {
#                 bestSum = sum;
#             }
#             if (sum > target) {
#                 ptr2--;
#             } else {
#                 ptr1++;
#             }
#         }
#     }
#     return bestSum;
# }
# import (
#     "sort"
#     "math"
# )
# func threeSumClosest(arr []int, target int) (int) {
# 	sort.Ints(arr)
# 	
# 	nearest := math.MaxInt32
# 	for i := 0; i < len(arr) - 2; i++ {
# 		j, k := i + 1, len(arr) - 1
# 		for j < k {
# 			next := arr[i] + arr[j] + arr[k]
# 			if math.Abs(float64(target - nearest)) > math.Abs(float64(target - next)) {
# 				nearest = next
# 			}
# 			
# 			if next > target {
# 				k--
# 			} else if next < target {
# 				j++
# 			} else {
# 				return nearest
# 			}
# 		}
# 	}
# 	return nearest
# }