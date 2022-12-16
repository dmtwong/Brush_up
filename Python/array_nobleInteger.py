# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:03:35 2022

@author: USER
"""
# Noble Integer
# Given an integer array A, find if an integer p exists in the array such that 
# the number of integers greater than p in the array equals to p.

# Problem Constraints
# 1 <= |A| <= 106
# -109 <= Ai <= 109

# Input Format
# First and only argument is an integer array A.

# Output Format
# Return 1 if any such integer p is found else return -1.

# Example Input
# Input 1:
  A = [3, 2, 1, 3]
  A = [3, -2, 1, 3]
  A = [3, 2, -1, 3]

# Input 2:
  A = [1, 1, 3, 3]

A = [ -2, 8, 8, 6, -2, 3, -2, -7, 3, 3, -2, 0, 4, -3, -4, -2, -1, -10, -4, -2, 7, -1, 0, -7, 3, -7, 7, 3, 2, -4, -5, 2, 6, 5, -2, 7, -1, 6, -10, 4, -9, -10, -6, -2, -3, 0, -2, 6, -8, 4, 7, 9, -7, 9, -8, -2, -7, -10, -9, -3, 8, 9, 1, 5, 4, 9, 2, 5, -3, -6, -1, -1, -6 ]

# Example Output
# Output 1:
#  1
# Output 2:
#  -1

# Example Explanation
# Explanation 1:

#  For integer 2, there are 2 greater elements in the array. So, return 1.
# Explanation 2:

#  There is no such integer exists.
# class Solution:
	# @param A : list of integers
	# @return an integer
# 	def solve(self, A):

def solve(A):
    ix = 0
    len_A = len(A)
    # while ix != len_A:        
    #     cur_list = A[:len_A]
    #     int_NobCheck = A[ix]
    #     if int_NobCheck > 
    #     # print(A[ix])
    #     if A[ix] < 0:
    #         ix += 1
    #         continue
    #     # print('done')
    #     cur_count = 0
    #     # len_cur_list = len(cur_list)
    #     for i in range(len_A):            
    #         if i == ix:
    #             continue
    #         if A[i] > int_NobCheck:
    #             cur_count += 1
    #         if cur_count > int_NobCheck:
    #             return -1        
    #     # print('current count is:', cur_count)
    #     if cur_count == int_NobCheck:
    #         return 1
    #     ix += 1
    # return -1
    count_A = [0] * (len_A + 1)
    for ix in range(len_A):
        int_NobCheck = A[ix]
        if A[ix] < 0:
            continue
        if A[ix] > len_A:
            count_A[len_A] += 1
            print('here', ix)
        else:
            # if A[ix] > len_A:
                # continue
            count_A[A[ix]] += 1
            print('there', ix)
    print(count_A)
    aggGreat = count_A[len_A]    
    print(aggGreat)
    for i in range(len_A - 1, -1, -1):
        print(aggGreat, i, count_A[i])
        if (aggGreat == i and count_A[i]) > 0:
            return 1
        elif aggGreat > i:
            return -1        
        aggGreat += count_A[i]
    return -1
A = [ 5, 6, 2 ]
solve(A)


# Suggested Solution:
#     class Solution:
# 	# @param A : list of integers
# 	# @return an integer
# 	def solve(self, A):
# 	    A.sort()
# 	    n = len(A)
# 	    for i in range(n-1):
# 	        if A[i] == A[i+1]:
# 	            continue
# 	        
# 	        if A[i] == n-i-1:
# 	            return 1
# 	    
# 	    if A[n-1] == 0:
# 	        return 1
# 	        
# 	    return -1
# Scala:    
# class Solution {
#     def solve(A: Array[Int]): Int  = {
#         val n = A.length
#         val map:Map[Int, Int] = A.sorted.zipWithIndex.toMap
#         A.find(el => el == n - map.getOrElse(el, 0) -1) match {
#             case Some(_) => 1
#             case _ => -1
#         }
#     }
# }

# GO
# /**
#  * @input A : Integer array
#  * 
#  * @Output Integer
#  */
# import "sort"

# func solve(A []int )  (int) {
#     sort.Ints(A)

    
#     for i:=0;i<len(A);i++ {
#         if A[i] == 0 && i == len(A)-1 {
#             return 1
#         }
        
#         if A[i] == len(A)-i-1 && i != len(A)-1 && A[i] != A[i+1]{
#             return 1
#         }
#     }
#     return -1
    
# }
# C++
# int Solution::solve(vector<int> &A) {
# 	sort(A.begin(), A.end()) ;
# 	int size = A.size();
# 	for(int i=0;i<size;i++){
# 		while(i+1<size && A[i]==A[i+1])
# 			i++;
# 		if(A[i]==size-1-i)
# 			return 1;
# 	}
# 	return -1;
# }