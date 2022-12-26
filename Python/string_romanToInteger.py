# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:36:28 2022

@author: USER
"""

# Given a string A representing a roman numeral.
# Convert A into integer.
# A is guaranteed to be within the range from 1 to 3999.
# NOTE: Read more 
# details about roman numerals at Roman Numeric System

# Input Format
# The only argument given is string A.
# Output Format
# Return an integer which is the integer verison of roman numeral string.
# For Example

# Input 1:
    A = "XIV"
# Output 1:
#     14

# Input 2:
    A = "XX"
# Output 2:
#     20

class Solution:
	# @param A : string
	# @return an integer
	def romanToInt(A):
        dict_romanToInt = {"I": 1,
                           "V": 5,
                           "X": 10,
                           "L": 50,
                           "C": 100,
                           "D": 500,
                           "M": 1000}
        
        result = 0
        n_A = len(A)
        i = 0
        # for i in range(n_A):
        while i < n_A:
            # print(dict_romanToInt[A[i]], dict_romanToInt[A[i+1]], result, i)
            if (i == n_A - 1) or (dict_romanToInt[A[i]] >= dict_romanToInt[A[i+1]]):
                result += dict_romanToInt[A[i]]               
            else:
                result += dict_romanToInt[A[i+1]] - dict_romanToInt[A[i]]
                i += 2
                continue
            i += 1
        return result
romanToInt(A)           

# suggested: 
# class Solution:
#     # @param A : string
#     # @return an integer
#     def romanToInt(self, A):
#         # x = "IVXLCDM"
#         d = {
#             "I":1,
#             "V":5,
#             "X":10,
#             "L":50,
#             "C":100,
#             "D":500,
#             "M":1000,
#         }
#         # print(d)
#         ans = 0
#         for i in range(len(A)-1):
#             if d[A[i]] < d[A[i+1]]:
#                 ans -= d[A[i]]
#             else:
#                 ans += d[A[i]]
#         ans += d[A[len(A)-1]]
#         return ans
# func romanToInt(roman string )  (int) {
# 	str := []rune(roman)
# 	dict := map[rune]int {'I' : 1, 'V': 5, 'X' : 10, 'L' : 50, 'C': 100, 'D': 500, 'M' : 1000}
# 	result := 0
# 	var prev, cur rune = ' ', ' '
# 	for i := len(roman) - 1; i >= 0; i-- {
# 		prev = cur
# 		cur = str[i]
# 		if dict[prev] > dict[cur] {
# 			result -= dict[cur]
# 		} else {
# 			result += dict[cur]
# 		}
# 	}
# 	
# 	return result
# }
#             int Solution::romanToInt(string A) {
#      string s=A;
#      if (s.empty()) { return 0; }
#         unordered_map<char, int> mp { {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000} };
#         int sum = mp[s.back()];
#         for (int i = s.size() - 2; i >= 0; --i) {
#             sum += mp[s[i]] >= mp[s[i + 1]] ? mp[s[i]] : -mp[s[i]];
#         }
#         return sum;
# }
#     class Solution {
#     def romanToInt(A: String): Int  = {
#         //recurisve function to calculate romanToInt with String of length 1 or greater
#         //More functional solution
#         def romanToInt(curr: Char, next: String, sum: Int ): Int = {
#             val currVal: Int =  getValue(curr)
#             var res: Int = sum
#             if(next.length == 0)  res + currVal
#             else {
#                 val nextVal = getValue(next.head)
#                 if(currVal >= nextVal) { res += currVal 
#                      romanToInt(next.head,next.tail, res )
#                 }else {
#                     res += (nextVal - currVal)
#                     if(next.tail.length == 0)  res
#                     else    romanToInt(next.tail.head,next.tail.tail, res )
#                 }
                
#             }
#         }
#         //If length of string is 0 return 0 otherwise calculate.
#         if(A.length ==0) 0 else romanToInt(A.head, A.tail, 0)
#     }
    
#     //Find the Integral Value for roman symbol
#     def getValue(c: Char): Int = c match {
#         case 'I' => 1
#         case 'V' => 5
#         case 'X' => 10
#         case 'L' => 50
#         case 'C' => 100
#         case 'D' => 500
#         case 'M' => 1000
#         case '_' => -1
#     }
# }
