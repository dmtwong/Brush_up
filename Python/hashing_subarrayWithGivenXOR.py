# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:02:58 2023

@author: USER
"""

# Problem Description
# Given an array of integers A and an integer B.
# Find the total number of subarrays having bitwise XOR of all elements equals to B.
# Problem Constraints
# 1 <= length of the array <= 105
# 1 <= A[i], B <= 109

# Input Format
# The first argument given is the integer array A.
# The second argument given is integer B.
# Output Format
# Return the total number of subarrays having bitwise XOR equals to B.
# Example Input
# Input 1:
 A = [4, 2, 2, 6, 4]
 B = 6
# Input 2:
 A = [5, 6, 7, 8, 9]
 B = 5
# Example Output
# Output 1:
#  4
# Output 2:
#  2
# Example Explanation
# Explanation 1:
#  The subarrays having XOR of their elements as 6 are:
#  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
# Explanation 2:
#  The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]

# class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # def solve(self, A, B):
def solve(A, B):
    n_A = len(A)
    result = 0
    xor_dict = {}
    prefix_list = [0 for x in range(n_A)]
    prefix_list[0] = A[0]
    for i in range(1, n_A):
        prefix_list[i] = A[i] ^ prefix_list[i - 1]
    # print(prefix_list)
    for j in range(n_A):
        curr_xor = prefix_list[j] ^ B
        if curr_xor in xor_dict.keys():
            result += xor_dict[curr_xor]
        if (prefix_list[j] == B):
            result += 1
        # xor_dict[prefix_list[j]] += 1
        xor_dict[prefix_list[j]] = xor_dict.get(prefix_list[j], 0) + 1
        # print(xor_dict.keys())
        # print(xor_dict.values())
    return result
A
solve(A, B)

# SuggesteD:
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         hashmap = {}
#         hashmap[0] = 1        
#         count = 0
#         running = 0        
#         for i in A:
#             running ^= i
#             if running^B in hashmap:
#                 count += hashmap[running^B]
#             if running in hashmap:
#                 hashmap[running] += 1
#             else:
#                 hashmap[running] = 1                
#         return count 
# class Solution {
#   def solve(nums: Array[Int], k: Int): Int  = {
#     val hm = scala.collection.mutable.HashMap[Int, Int]()
#     var cou = 0
#     var curSum = 0
#     for (i <- 0 until nums.length) {
#       curSum ^= nums(i)
#       if (curSum == k) {
#         cou += 1
#       }
#       val km = curSum ^ k
#       val t = hm.getOrElse(km, 0)
#       cou += t
#       val t1 = hm.getOrElse(curSum, 0) + 1
#       hm += (curSum -> t1)
#     }
#     return cou
#   }
# }
# int Solution::solve(vector<int> &A, int B) {
#     int n = A.size();
#     int ans = 0; // Initialize answer to be returned

#     // Create a prefix xor-sum array such that xorArr[i] has value equal to XOR of all elements in A[0 ..... i]
#     int xorArr[n];

#     // Create map that stores number of prefix array elements corresponding to a XOR value
#     unordered_map<int, int> mp;

#     // Initialize first element of prefix array
#     xorArr[0] = A[0];

#     // Computing the prefix array.
#     for (int i = 1; i < n; i++)
#         xorArr[i] = xorArr[i - 1] ^ A[i];

#     // Calculate the answer
#     for (int i = 0; i < n; i++) {
#       // Find XOR of current prefix with m.
#         int tmp = B ^ xorArr[i];

#         // If above XOR exists in map, then there is another previous prefix with same XOR, i.e., there is a subarray ending at i with XOR equal to B.
#         ans = ans + mp[tmp];

#         // If this subarray has XOR equal to m itself.
#         if (xorArr[i] == B)
#             ans++;

#         // Add the XOR of this subarray to the map
#         mp[xorArr[i]]++;
#     }

#     // Return total count of subarrays having XOR of elements as given value m
#     return ans;
# }

# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# func solve(A []int , B int )  (int) {
#     sum := 0
#     m := make(map[int]int)
#     ans := 0
#     m[0] = 1
#     for _, a := range A {
#         sum ^= a 
#         ans += m[sum^B]
#         m[sum]++
#     }
#     return ans
# }

# // 4, 2, 2, 6, 4
# // f(i,j) = sum ^B = f(j,0)
