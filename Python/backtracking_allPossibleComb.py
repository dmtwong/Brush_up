# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:12:18 2023

@author: USER
"""
# Problem Description 
 
# You are given a array of strings A of length N.

# You have to return another string array which contains all possible special strings in Lexicographic order.
#  A special string is defined as a string with length equal to N, 
#  and ith character of the string is equal to any character of the ith string in the array A.

# Problem Constraints
# 1 <= N <= 5
# 1 <= |Ai| <= 8

# Input Format
# The first argument is the string array A.

# Output Format
# Return a string array consisting of all possible special strings.

# Example Input
# Input 1:
A = ['ab', 'cd']
# Input 2:
A = ['aa', 'bb']

# Example Output
# Output 1:
# ['ac', 'ad', 'bc', 'bd']
# Output 2:

# ['ab', 'ab', 'ab', 'ab']

# Example Explanation
# Explanation 1:
# Since, the first character has to be from the 1st string 'ab' and the 2nd from 'cd'.
# These are the all possible 4 combinations.
# Explanation 2:

# Note we can have duplicate strings, you have to add all of them.
# class Solution:
    # @param A : list of strings
    # @return a list of strings
    # def specialStrings(self, A):
# import itertools
# a=[1,2,3]
# b=[4,5,6]
# c=[7,8,9]
# sorted(list(itertools.product(a,c,b)))
A = [ "wc", "lch" ]

def specialStrings(A):
    # import itertools
    n_A = len(A)
    list_A = []    
    for i in range(n_A):
        list_A.append([])
        for j in A[i]:
            list_A[i].append(j)
    # print(list_A)
    result = [[]]
    for list_ele in list_A:
        # print("now", list_ele)
        ind_comb = []
        for char in list_ele:
            # print('here', char)
            for prev in result:
                # print('there', prev)
                ind_comb.append(prev + [char])
            # print(ind_comb)
        # print(result)
        result = ind_comb
    # result = sorted(list(itertools.product(list_A)))
    # return result
    final_result = []
    for comb in result:
        final_result.append("".join(comb))
    # final_result = sorted(list(set(final_result)))
    final_result = sorted(final_result)     
    return final_result
A = [ "ozqz", "p", "abm" ]

specialStrings(A)
# Editorial:
# class Solution:
#     # @param A : list of strings
#     # @return a list of strings
#     def recur(self,A,res,temp,index):
#         if(index == len(A)):
#             res.append(str(temp))
#             return
#         curr = temp
#         for i in range(len(A[index])):
#             temp = temp + A[index][i]
#             self.recur(A,res,temp,index+1)
#             temp = curr
#     def specialStrings(self, A):
#         res = []
#         self.recur(A,res,"",0)
#         res.sort(reverse = False)
#         # print(res)
#         return res
# GO:
#     /**
#  * @input A : array of strings
#  * 
#  * @Output string array.
#  */
 
# import (
#     "strings"
#     "sort"
# )
# func specialStrings(A []string) []string {
#     ans := []string{}
#     if len(A) == 0 {
#         return ans
#     }
#     c := []string{}
#     d := &c
#     first := strings.Split(A[0], "")
#     for _, a := range first {
#         combine(a, A[1:], d)
#     }
#     sort.Strings(c)
#     return c
# }

# func combine(a string, b []string, c *[]string) {
#     if len(b) == 0 {
#         *c = append(*c, a)
#     } else {
#         temp := b[0]
#         b = b[1:]
#         tempArr := strings.Split(temp, "")
#         for _, s := range tempArr {
#             combine(a+s, b, c)
#         }
#     }
# }
#        C++
#         vector < string > ans;
# void rec(vector < string > & A, int i, int j, string par) {
#     string curr = par;
#     if (i == A.size()) {
#         ans.push_back(curr);
#         return;
#     }
#     if (j < A[i].length() - 1) {
#         rec(A, i, j + 1, curr);
#     }
#     curr += A[i][j];
#     rec(A, i + 1, 0, curr);
# }

# vector < string > Solution::specialStrings(vector < string > & A) {
#     ans.clear();
#     string curr = "";
#     rec(A, 0, 0, curr);
    
     
#     return ans2;
# }