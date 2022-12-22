# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:27:08 2022

@author: USER
"""
# Problem Description
 
#  Given a string A containing only lowercase characters.
# Find the frequencies of the characters in order of their occurrence.

# Problem Constraints
# 1 <= |A| <= 105


# Input Format
# Given a string A.


# Output Format
# Return an array of integer.


# Example Input
# Input 1:
A = "interviewbit"
# Input 2:

A = "scaler"


# Example Output
# Output 1:
# [3, 1, 2, 2, 1, 1, 1, 1]
# Output 2:

# [1, 1, 1, 1, 1, 1]


# Example Explanation
# Explanation 1:
# Characters in their order of occurence and frequecies are {'i', 3}, {'n', 1}, {'t', 2}, {'e', 2}, {'r', 1}, {'v', 1}, {'w', 1}, {'b', 1}.
# Explanation 2:

# Characters in their order of occurence and frequecies are {'s', 1}, {'c', 1}, {'a', 1}, {'l', 1}, {'e', 1}, {'r', 1}.
''
# class Solution:
    # @param A : string
    # @return a list of integers
    def solve(A):
        n_A = len(A)
        list_A = [letter for letter in A]
        list_dict = []
        list_val = []
        for i in range(n_A):
            cur_letter = list_A[i]
            if cur_letter not in list_dict:
                list_dict.append(cur_letter)
                list_val.append(1)
            else: 
                ix_char = list_dict.index(cur_letter)
                list_val[ix_char] += 1
        return list_val
solve(A)               

# Suggested:
    
#     from collections import OrderedDict
# class Solution:
#     # @param A : string
#     # @return a list of integers
#     def solve(self, A):
#         dic=OrderedDict()
#         for val in A:
#             dic[val]=dic.get(val,0)+1
        
#         ans=[]
#         for k,v in dic.items():
#             ans.append(v)
#         return ans
# vector<int> Solution::solve(string A) {
#     assert(1<=A.size() && A.size()<=1e5);
#     string order="";
#     map<char, int> mp;
#     for(char x: A){
#         assert('a'<=x && x<='z');
#         if(order.find(x)==string::npos){
#             order.push_back(x);
#         }
#         mp[x]++;
#     }
#     vector<int> ans;
#     for(char x: order){
#         ans.push_back(mp[x]);
#     }
#     return ans;
# }
# GO:
#     /**
#  * @input A : String
#  * 
#  * @Output Integer array.
#  */
# func solve(A string )  ([]int) {
#     var m map[byte]int
#     m = make(map[byte]int)
#     n := len(A)
#     for i:=0; i<n; i++{
#         elem, ok := m[A[i]]
#         if ok == true{
#             m[A[i]] = elem+1
#         }else{
#             m[A[i]] = 1
#         }
#     }
#   //  size_ans := len(m)
    
#     var ans[] int
    
#    // x:=0
#     for i:=0; i<n; i++{
#         elem, ok := m[A[i]]
#         if ok == true{
#            // ans[x] = m[A[i]]
#           //  fmt.Println(A[i], " : ", elem)
#             ans = append(ans, elem)
#            // x++
#             delete(m, A[i])
#         }else{
#             continue
#         }
#     }
#     return ans
# }