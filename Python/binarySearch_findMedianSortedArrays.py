# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:32:50 2022

@author: USER
"""

#####################
# not bisection below simply use a straight forward approach so it is O(m+n) instead
#####################

# Median of Array
# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays ( The median of the array formed by merging both arrays ).
# The overall run time complexity should be O(log (m+n)).
# NOTE: If the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5 

# Input Format
# The first argument is an integer array A.
# The second argument is an integer array B.

# Output Format
# Return a double value equal to the median.

# Example Input
A = [1, 4, 5]
B = [2, 3]

# Example Output
# 3

# Example Explanation
# Merged A and B will be : [1, 2, 3, 4, 5]
# Its median will be 3

# class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    # def findMedianSortedArrays(self, A, B):
        

def findMedianSortedArrays(A, B):
    result = []
    i, j = 0, 0
    n_A, n_B = len(A), len(B)
    while ((i < n_A) and (j < n_B)):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    while (i < n_A):
        result.extend(A[i:])
        i = n_A
    while (j < n_B):
        result.extend(B[j:])
        j = n_B
    n_result = len(result)
    mid_result = n_result // 2  # 5 => 2 6 => 3 
    if len(result) % 2 == 1:
        return float(result[mid_result])
    else:
        return (float(result[mid_result])+ result[mid_result - 1]) / 2    
findMedianSortedArrays(A, B)
t1 = [1, 2 ,3 ]
t2 = [4, 5, 6]
findMedianSortedArrays(t1, t2)

# SuggesteD:
    # class Solution:
    # # @param A : tuple of integers
    # # @param B : tuple of integers
    # # @return a double
    # def findMedianSortedArrays(self, A, B):
    #     m = len(A)
    #     n = len(B)
    #     if m > n:
    #         n,m = m,n
    #         A,B = B,A
    #     if m == 0:
    #         if n == 0:
    #             return 0
    #         if n%2:
    #             return B[n/2]
    #         else:
    #             return (B[n/2]+B[n/2-1])/2.0
    #     low = 0
    #     high = m
    #     while low <= high:
    #         i = (low+high)/2
    #         j = (m+n+1)/2-i
    #         if (j == 0 or i == m or B[j - 1] <= A[i]) and (i == 0 or j == n or A[i-1] <= B[j]):
    #             if (m+n)%2:
    #                 if i == 0:
    #                     return B[j-1]
    #                 elif j == 0:
    #                     return A[i-1]
    #                 return max(A[i-1],B[j-1])
    #             else:
    #                 if i == 0:
    #                     return (B[j-1] + min(A[i],B[j]))/2.0
    #                 if j == 0:
    #                 	return (A[i-1] + min(A[i],B[j]))/2.0
    #                 if i == m:
    #                 	return (max(A[i-1],B[j-1]) + B[j])/2.0
    #                 if j == n:
    #                 	return (max(A[i-1],B[j-1]) + A[i])/2.0
    #                 return (max(A[i-1],B[j-1]) + min(A[i],B[j]))/2.0
    #         elif (j == 0 or i == m or B[j - 1] > A[i]):
    #             low = i+1
    #         elif (i == 0 or j == n or A[i-1] > B[j]):
    #             high = i-1
    #     return -1

# c++
# double Solution::findMedianSortedArrays(const vector<int> &A, const vector<int> &B) {
#     int N1 = A.size();
#     int N2 = B.size();
#     if (N1 < N2) return findMedianSortedArrays(B, A);   
#     if (N2 == 0) return (A[(N1-1)/2] + (double)A[N1/2])/2.0;

#     int lo = 0, hi = N2 * 2,mid1,mid2;
#     double L1,L2,R1,R2;
#     while (lo <= hi) {
#          mid2 = (lo + hi) / 2;  
#          mid1 = N1 + N2 - mid2; 

#          L1 = (mid1 == 0) ? -1000000000 : A[(mid1-1)/2]; 
#          L2 = (mid2 == 0) ? -1000000000 : B[(mid2-1)/2];
#          R1 = (mid1 == N1 * 2) ? 1000000000 : A[(mid1)/2];
#          R2 = (mid2 == N2 * 2) ? 1000000000 : B[(mid2)/2];

#         if (L1 > R2) lo = mid2 + 1;    
#         else if (L2 > R1) hi = mid2 - 1;    
#         else return (max(L1,L2) + min(R1, R2)) / 2;
#     }
#     return -1;
# }

# java:
#     public class Solution {
# public double findMedianSortedArrays(final List<Integer> A, final List<Integer> B) {
# 	    int len = A.size() + B.size();
# 	    if(len % 2 == 1) return findKth(A, 0, B, 0, len / 2 + 1);
# 	    else return (findKth(A, 0, B, 0, len / 2) + findKth(A, 0, B, 0, len / 2 + 1)) / 2.0;
# 	}
# 	
# 	public int findKth(List<Integer> A, int A_start, List<Integer> B, int B_start, int k){
# 	    if(A_start >= A.size()) return B.get(B_start + k - 1);
# 	    if(B_start >= B.size()) return A.get(A_start + k - 1);
# 	    if(k == 1) return Math.min(A.get(A_start), B.get(B_start));
# 	    
# 	    int A_key = A_start + k / 2 - 1 < A.size() ? A.get(A_start + k / 2 - 1) : Integer.MAX_VALUE;
# 	    int B_key = B_start + k / 2 - 1 < B.size() ? B.get(B_start + k / 2 - 1) : Integer.MAX_VALUE;
# 	    
# 	    if(A_key < B_key){
# 	        return findKth(A, A_start + k / 2, B, B_start, k - k / 2);
# 	    }
# 	    else
# 	       return findKth(A, A_start, B, B_start + k / 2, k - k / 2);
# 	}
# }