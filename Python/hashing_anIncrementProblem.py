# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:32:46 2023

@author: USER
"""

# Problem Description
# Given a stream of numbers A. On arrival of each number, you need to increase its 
# first occurrence by 1 and include this in the stream.
# Return the final stream of numbers.
# Note: You will traverse the stream from left to right and update the first occurrence
# of the number by 1, if found.

# Problem Constraints
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10000
# Input Format
# First and only argument is the array A.
# Output Format
# Return an array, the final stream of numbers.

# Example Input
# Input 1: 
A = [1, 1] 
# Input 2:
A = [1, 2]
# Input 3:
A = [1, 1, 2, 2]

# Example Output
# Output 1:
# [2, 1]
# Output 2:
# [1, 2]
# Output 3:
# [3, 1, 3, 2]
# Example Explanation
# Explanation 1:
# On arrival of the second element, the other element is increased by 1. 
# Explanation 2:
# No increases are to be done. 
# Explanation 3:
# Stream after arrival of numbers (1-based indexing):
#   First number  (1): [1]          , Simply push 1 to the stream
#   Second number (1): [2, 1]       , Increment first occurence of 1, present at 1st Index and push 1 to the stream
#   Third number  (2): [3, 1, 2]    , Increment first occurence of 2, present at 1st Index and push 2 to the stream
#   Fourth number (2): [3, 1, 3, 2] , Increment first occurence of 2, present at 3rd Index and push 2 to the stream

# class Solution:
    # @param A : list of integers
    # @return a list of integers
    # def solve(self, A):
# from collections import OrderedDict
# tmp = []
# curr_ix = OrderedDict()
# curr_ix[7] = 3
# tmp.append(curr_ix)
# curr_ix = OrderedDict()
# curr_ix[3] = 13
# tmp.append(curr_ix)
# tmp
# this_Dict = dict()
# this_Dict[3] = [0]
# this_Dict[3].append(1) 
# shift_ix = this_Dict[3].pop()
# this_Dict[3+1] = [shift_ix]
# this_Dict
# this_Dict[-5] = [2]
# result = [-99] * 3
# # j = 0
# for i in this_Dict:
#     curr_loop = this_Dict[i]
#     for ix in curr_loop:
#         result[ix] = i 
#         # j += 1
# result
# for i in []:
#     print(i)
#     print('Null')
def solve(A):
    this_Dict = dict()
    n_A = len(A)
    def add_key(val, ix, update = False):
        if val not in this_Dict:
            # print(ix, val, 'no changed')
            this_Dict[val] = [ix]
            this_Dict[val].sort()
            # print([(x, this_Dict[x]) for x in this_Dict], '!')
        # else: 
        elif update == True:
            # print(ix, val, update)
            this_Dict[val].append(ix) 
            this_Dict[val].sort()
            incr_val = val + 1
            shift_ix = this_Dict[val].pop(0)
            # print('need to update', shift_ix, incr_val)
            add_key(incr_val, shift_ix)
            # print([(x, this_Dict[x]) for x in this_Dict], '!!')
            # update(val, shift_ix)
        else:
        #     print(ix, val, update)
            # this_Dict[val].pop(0)
            this_Dict[val].append(ix) 
            this_Dict[val].sort()
            # print([(x, this_Dict[x]) for x in this_Dict], '!!!')

    for i in range(n_A):
        # print('here is i and originally', A[i])
        curr_val = A[i]
        add_key(curr_val, i, update = True)
    # print(this_Dict)
    result = [-99] * n_A
    # print(this_Dict.keys())
    # print(this_Dict.values())
    for i in this_Dict:        
        curr_loop = this_Dict[i]
        for ix in curr_loop:
            result[ix] = i 
    return result
# A
# for i in this_Dict:
#     # print(i)
#     print(this_Dict[i])
# [this_Dict[x] for x in this_Dict]
solve(A)
A = [ 1, 2, 3, 2, 3, 1, 4, 2, 1, 3 ]

# 124231
# 4, 5, 3, 2, 3, 2, 4, 2, 1, 3
# The expected return value: 
# 4 5 3 2 3 2 4 2 1 3 
# [2, 4, 5, 3, 3, 2, 4, 2, 1, 3]
# [5, 9, 10, 6, 8, 2, 7, 4, 1, 3]

# Editorial
# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):
#         first_occurance = dict()
#         for index, a in enumerate(A):
#             if a in first_occurance:
#                 A[first_occurance[a]] += 1
#                 first_occurance[a + 1] = min(first_occurance.get(a + 1, len(A)), first_occurance[a])
#             first_occurance[a] = index               
#         return A
# class Solution {
#     def solve(A: Array[Int]): Array[Int]  = {

#     def loop(i: Int, cache: Map[Int, Int]): Array[Int] = {
#       if (i == A.length) A
#       else {
#         val nCache =
#           if (cache.contains(A(i))) {
#             val oldPos = cache(A(i))
#             val newVal = A(oldPos) + 1

#             A(oldPos) = newVal

#             if (cache.contains(newVal))
#               cache + (newVal -> Math.min(oldPos, cache(newVal)))
#             else
#               cache + (newVal -> oldPos)
#           }
#           else cache
#         loop(i + 1, nCache + (A(i) -> i))
#       }
#     }

#     loop(0, Map.empty[Int, Int])
#   }


# }
# vector<int> Solution::solve(vector<int> &A) {
#     vector<int> res;
#     for(int i=0;i<A.size();i++) {
#         auto it=find(res.begin(),res.end(),A[i]);
#         if(it!=res.end()) {
#             (*it)++;
#             res.push_back(A[i]);
#         }
#         else {
#             res.push_back(A[i]);
#         }
#     }
#     return res;
# }
# /**
#  * @input A : Integer array
#  * 
#  * @Output Integer array.
#  */
# func solve(A []int )  ([]int) {
#     m := make(map[int]int)
    
#     for i, v := range A {
#         if _, ok := m[v]; ok {
#             A[m[v]]++
#             m[A[m[v]]] = m[v]
#             m[v] = i
#         } else {
#             m[v] = i
#         }
#     }
#     return A
# }