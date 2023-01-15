# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 21:59:25 2023

@author: USER
"""
# Problem Description
# Given an integer array A of size N, find the first repeating element in it.
# We need to find the element that occurs more than once and whose index of first occurrence is smallest.
# If there is no repeating element, return -1.
# Problem Constraints
# 1 <= N <= 105                1 <= A[i] <= 109
# Input Format
# First and only argument is an integer array A of size N.
# Output Format
# Return an integer denoting the first repeating element.
# Example Input
# Input 1:
 A = [10, 5, 3, 4, 3, 5, 6]
# Input 2:
 A = [6, 10, 5, 4, 9, 120]
# Example Output
# Output 1: 5
# Output 2: -1
# Example Explanation
# Explanation 1:
#  5 is the first element that repeats
# Explanation 2:
#  There is no repeating element, output -1
# class Solution:
    # @param A : list of integers
    # @return an integer
    # def solve(self, A):
        
def solve(A):
    from collections import OrderedDict
    thisDict = OrderedDict()
    n_A = len(A)
    # buckets = []
    # first_occ = []
    # repeat_occ = []
    # for i in range(n_A):
    #     buckets.append(set())
    for i in range(n_A):                
        curr_val = A[i]
        # curr_key = curr_val % n_A 
        # curr_bucket = buckets[curr_key]
        if curr_val in thisDict.keys():
            thisDict[curr_val] += 1
        else:
            thisDict[curr_val] = 1
    for i in thisDict.keys():                
        if thisDict[i] > 1:
            return i
    return -1
solve(A)

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         n = len(A)
#         # Initialize index of first repeating element
#         mini = -1
    
#         # Creates an empty hashset named ump
#         ump = {}
    
#         # Traverse the input array from right to left
#         for i in range(n-1, -1, -1):
#             # If element is already in hash set, update min
#             if (ump.get(A[i]) != None):
#                 mini = i
#             else:   # Else add element to hash set
#                 ump[A[i]] = 1
        
#         if(mini == -1):
#             return mini
        
#         return A[mini]
# class Solution {
#     def solve(A: Array[Int]): Int  = {
#         var s = Set.empty[Int]
        
#         var lastRepeat = -1
        
#         for (i <- A.size - 1 to 0 by -1) {
#             val v = A(i)
#             if (s.contains(v)) {
#                 lastRepeat = v
#             } else {
#                 s = s + v
#             }
#         }
#         return lastRepeat
#     }
# }
# /**
#  * @input A : Integer array
#  * 
#  * @Output Integer
#  */

# func solve(A []int) int {

#     if len(A) <= 1 {
#         return -1
#     }
#     elements := make(map[int]int)

#     minRepeaterIndex := len(A)
#     for i, el := range A {
#         val, ok := elements[el]
#         if ok {
#             if val < minRepeaterIndex {
#                 minRepeaterIndex = val
#             }
#             continue
#         }
#         elements[el] = i
#     }

#     if minRepeaterIndex == len(A) {
#         return -1
#     }
#     return A[minRepeaterIndex]
# }
# int Solution::solve(vector<int> &A) {
#     int n = A.size();
#     // Initialize index of first repeating element
#     int mini = -1;

#     // Creates an empty hashset named ump
#     unordered_map<int,int> ump;

#     // Traverse the input array from right to left
#     for (int i = n - 1; i >= 0; i--)
#     {
#         // If element is already in hash set, update min
#         if (ump.find(A[i]) != ump.end())
#             mini = i;
#         else   // Else add element to hash set
#             ump[A[i]] = 1;
#     }
#     if(mini == -1){
#         return mini;
#     }
#     return A[mini];
# }