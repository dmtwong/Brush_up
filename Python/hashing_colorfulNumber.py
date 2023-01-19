# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:42:01 2023

@author: USER
"""

# Problem Description
# For Given Number A, find if it's a COLORFUL number or not.

# COLORFUL number:
# A number can be broken into different contiguous sub-subsequence parts. 
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
# Return 1 if A is a COLORFUL number, else return 0

# Problem Constraints
# 0 <= A <= 109
# Input Format
# The first argument is an integer A.
# Output Format
# Return 1 if A is a COLORFUL number, else return 0
# Example Input
A = 23
# Example Output
# 1
# Example Explanation
# A = 23
# 2 3 23
# 2 -> 2
# 3 -> 3
# 23 -> 6
# this number is a COLORFUL number since the product of every digit of a sub-sequence is different.
# Output: 1
# class Solution:
	# @param A : integer
	# @return an integer
# 	def colorful(self, A):

A = 234
A = 234353

def colorful(A):
    str_A = str(A)
    n_A = len(str_A)
    sub_power_set = []
    color_dict = {}
    for i in range(1, n_A + 1):
        j, k = 0, i
        while j <= n_A - k:
            sub_power_set.append(str_A[j:j+k])
            j += 1
        k += 1
        # print(sub_power_set)
    # result = []
    for i in sub_power_set:
        temp_val = 1
        for j in range(len(i)):
            temp_val *= int(i[j])
        # result.append(temp_val)
        if color_dict.get(temp_val, -1) == -1:
            color_dict[temp_val] = i
        else: 
            return 0
    # print(result)
    # print(color_dict.keys())
    # print(color_dict.values())
    return 1
colorful(A)

# Editorial
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def colorful(self, A):
#         products = set()
#         str_num = str(A)
#         for i in range(len(str_num)):
#             for j in range(i + 1, len(str_num) + 1):
#                 product = reduce(lambda x, y: x * y, map(int, list(str_num[i:j])))
#                 if product in products:
#                     return 0
#                 products.add(product)
#         return 1

# class Solution {
#     def colorful(A: Int): Int  = {
#     val digits = math.log10(A).toInt + 1
#     val set = new collection.mutable.HashSet[Int]

#     for (windowSize <- 1 to digits) {
#       var num = A
#       for (i <- 1 to digits - windowSize + 1) {
#         val n = (num % (math.pow(10, windowSize))).toInt
#         val res = n.toString.toList.map(_.asDigit).foldLeft(1)(_ * _)
#         if (set.contains(res)) return 0
#         set += res
#         num /= 10
#       }
#     }

#     1
#     }
# }
# int Solution::colorful(int A) {
#    if (A < 10) return 1;
# 	set<int> s;
# 	vector<int> v;
# 	while (A) {
# 		int lastdigit = A % 10;
# 	    A /= 10;
# 		for (auto &i : v) i *= lastdigit;
# 		v.push_back(lastdigit);
# 		for (auto i : v) {
# 			if (s.count(i)) return 0;
# 			else s.insert(i);
# 		}
# 	}
# 	return 1;
# }

# /**
#  * @input A : Integer
#  * 
#  * @Output Integer
#  */
# import (
#     "strconv"
# )
    
# func colorful(A int )  (int) {
#         strA := strconv.Itoa(A)
#         subNums := []string{}
#         for i := 1; i <= len(strA); i++ {
#                 for j := 0; i+j <= len(strA); j++ {
#                         subNums = append(subNums, strA[j:i+j])
#                 }
#         }
#         sumMap := map[int]bool{}

#         for i := 0; i < len(subNums); i++ {
#                 prod := 1
#                 for j := len(subNums[i]) - 1; j >= 0; j-- {
#                         digit := int(subNums[i][j] - '0')
#                         prod *= digit
#                 }
#                 if _, ok := sumMap[prod]; ok {
#                         return 0
#                 }
#                 sumMap[prod] = true
#         }
#         return 1
# }
