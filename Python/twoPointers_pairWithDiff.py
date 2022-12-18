# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:35:59 2022

@author: USER
"""

# Pair With Given Difference
# Problem Description

# Given an one-dimensional unsorted array A containing N integers.
# You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.
# Return 1 if any such pair exists else return 0.

# Input Format
# First argument is an integer array A of size N.
# Second argument is an integer B.

# Output Format
# Return 1 if any such pair exists else return 0.


# Example Input
# Input 1:
 A = [5, 10, 3, 2, 50, 80]
 B = 78
# Input 2:
 A = [-10, 20]
 B = 30
# Example Output
# Output 1: 1
# Output 2: 1

# Example Explanation
# Explanation 1:

#  Pair (80, 2) gives a difference of 78.
# Explanation 2:

#  Pair (20, -10) gives a difference of 30 i.e 20 - (-10) => 20 + 10 => 30

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
# -4, 0, 1, 2,4,5, 10, 50, 80, 82
# A = [ -259, -825, 459, 825, 221, 870, 626, 934, 205, 783, 850, 398 ]
# B = -42

def solve(A, B):
    A.sort()
    B = abs(B)
    # print(A)
    n_A = len(A)
    i, j = 0, n_A
    for i in range(n_A - 1):
        for j in range(n_A - 1, i, -1):
            if A[j] - A[i] == B:
                return 1
            if A[j] - A[i] < B:
                break
    return 0
solve(A, B)             

# Suggested:                    
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         temp=dict()
#         for a in A:
#             try:
#                 temp[a]=temp[a]+1
#             except KeyError:
#                 temp[a]=1
#         for a in A:
#             if((B+a)==a and temp[a]>1):
#                 return 1
#             elif(B+a==a):
#                 continue
#             elif(temp.get(B+a,0)!=0):
#                 return 1
#         return 0
# Scala:
# class Solution {
#     def solve(A: Array[Int], B: Int): Int  = {
    
#         import scala.collection.mutable
#         import scala.collection.mutable.HashMap
#         val arr = A.sorted
#         val diff = B
#         val map = new mutable.HashMap[Int, Boolean]()
#         var status = false
    
#         for(num <- arr) {
    
#           if(map.contains(num)) {
#             status = true
#           } else {
#             map.put(diff + num, true)
#             map.put(num - diff, true)
#           }
#         }
#         if(status) 1 else 0
#     }
# }
# C++
# bool findPair(vector<int>&arr, int size, int n)  
# {  
#     // Initialize positions of two elements  
#     int i = 0;  
#     int j = 1;  
#    sort(arr.begin(),arr.end());
#     // Search for a pair  
#     while (i < size && j < size)  
#     {  
#         if (i != j && arr[j] - arr[i] == n)  
#         {
#             return true;  
#         }  
#         else if (arr[j]-arr[i] < n)  
#             j++;  
#         else
#             i++;  
#     }  
#     return false;  
# }  
# int Solution::solve(vector<int> &A, int B) {
#     return findPair(A,A.size(),B);
# }
# GO
# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# func solve(A []int , B int )  (int) {
#     m := make(map[int][]int)
#     for i,a:=range A{
#         m[a] = append(m[a],i)
#     }
#     for i:=0;i<len(A);i++{
#         k := B + A[i]
#         if _,ok:=m[k];ok{
#             val := m[k]
#             for j:=0;j<len(val);j++{
#                 if val[j] != i{
#                     return 1
#                 }
#             }
#         }
#     }
#     return 0
# }
