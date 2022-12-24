# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:13:12 2022

@author: mingt
"""

# Problem Description
 
# Given two sorted integer arrays A and B,
# merge B into A as one sorted array.

# Note: You have to modify the array A to contain the merge of A and B. 
# Do not output anything in your code.
# TIP: C users, please malloc the result into a new array and return the result.

# If the number of elements initialized in A and B is m and n respectively, 
# the resulting size of array A after your code is executed should be m + n


# Problem Constraints
# 1 <= |A|, |B| <= 105


# Input Format
# The first argument is an integer array A.
# The second argument is an integer array B.


# Output Format
# Update the array A.


# Example Input
A = [1, 5, 8]
B = [6, 9]

A = [6, 9]
B = [1, 5, 8]
# Example Output
# Modified A : [1 5 6 8 9]

# class Solution:
    # @param A : list of integers
    # @param B : list of integers
    
def merge(A, B):
    # import copy
    # result = []
    i, j = 0, 0
    n_B = len(B)
    while ((i < len(A)) and (j < n_B)):
        if A[i] < B[j]: 
            i += 1
        else:
            A.insert(i, B[j])
            i += 1
            j += 1
    # while (i < n_A):
    #     result.extend(A[i:])
    #     i = n_A
    while (j < n_B):
        A.extend(B[j:])
        j = n_B
    # print(A)
    # A = copy.copy(result)
    # print(result)
    # print(A)
    # print(B)

A = [ -4, 3 ]
B = [ -2, -2 ]
merge(A, B)



# Suggested:
#     class Solution:
#     # @param A : list of integers
#     # @param B : list of integers
#     def merge(self, A, B):
#         m, n = len(A), len(B)
#         A[:] = A + [0] * n
#         l = m + n
#         position = m + n - 1
#         p1, p2 = m-1, n-1
#         while p1 >= 0 and p2 >= 0:
#             if A[p1] > B[p2]:
#                 A[position] = A[p1]
#                 p1 -= 1
#             else:
#                 A[position] = B[p2]
#                 p2 -= 1
#             position -= 1
            
#         while p1 >= 0:
#             A[position] = A[p1]
#             p1 -= 1
#             position -= 1
        
#         while p2 >= 0:
#             A[position] = B[p2]
#             p2 -= 1
#             position -= 1
    
#     C++:
#         void Solution::merge(vector<int> &A, vector<int> &B) {
#     int m = A.size();
#     int n = B.size();
#     int temp[m+n+2];
#     int indexA = 0, indexB = 0;
#     for (int i = 0; i < m+n; i++){
#         if (indexB == n || (indexA < m && A[indexA] < B[indexB])) {
#             temp[i] = A[indexA];
#             indexA++;
#         } else {
#             temp[i] = B[indexB];
#             indexB++;
#         }
#     }
#     A.resize(m + n);
#     for (int i = 0; i < m+n; i++) {
#         A[i] = temp[i];
#     }
#     return;
# }
            
# JAVA:
# public class Solution {
# 	public void merge(ArrayList<Integer> A, ArrayList<Integer> B) {
# 	    int m, n;
# 	    ArrayList<Integer> res = new ArrayList<>();
# 	    
# 	    if (A == null && B == null)
# 	        return;
# 	    
# 	    if (A == null) {
# 	        A = B;
# 	        return;
# 	    }
# 	        
# 	    if (B == null)
# 	        return;
# 	        
# 	    m = A.size();
# 	    n = B.size();
# 	    
# 	    int i, j;
# 	    int k = 0;
# 	    
# 	    for (i = 0, j = 0; k < m + n; k++) {
# 	        if (i >= m)
# 	            res.add(B.get(j++));
# 	        else if (j >= n)
# 	            res.add(A.get(i++));
# 	        else if (A.get(i) <= B.get(j)) {
# 	            res.add(A.get(i));
# 	            i++;
# 	        } else {
# 	            res.add(B.get(j));
# 	            j++;
# 	        }
# 	    }
# 	    
# 	    A.clear();
# 	    
# 	    for (int num : res)
# 	        A.add(num);
# 	    
# 	    return;
# 	    
# 	}
# }