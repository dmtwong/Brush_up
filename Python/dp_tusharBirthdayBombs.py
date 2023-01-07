# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:54:43 2023

@author: USER
"""

# Problem Description
# It’s Tushar’s birthday today and he has N friends.

# Friends are numbered [0, 1, 2, ...., N-1] and ith friend have a positive strength B[i].

# Today being his birthday, his friends have planned to give him birthday bombs (kicks).

# Tushar's friends know Tushar's pain bearing limit and would hit accordingly.

# If Tushar’s resistance is denoted by A (>=0) then 
# find the lexicographically smallest order of friends to kick Tushar so 
# that the cumulative kick strength (sum of the strengths of friends who kicks) doesn’t exceed his resistance capacity and
# total no. of kicks hit are maximum.

# Also note that each friend can kick an unlimited number of times (If a friend hits x times, his strength will be counted x times)

# Return the lexicographically smallest array of maximum length where the ith index represents the index of the friend who will hit.

# NOTE:

# [a1, a2, ...., am] is lexicographically smaller than [b1, b2, .., bm] if a1 < b1 or (a1 = b1 and a2 < b2) ... .
# Input cases are such that the length of the answer does not exceed 100000.

# Input Format
# The first argument contains an integer, A of length N.
# The second argument contains an array of integers B.
# Output Format
# Return an array of integer, as described in the problem statement.

# Example Input
# Input 1: 
 A = 12
 B = [3, 4]
# Input 2:

 A = 11
 B = [6, 8, 5, 4, 7]


# Example Output
# Output 1: 

#  [0, 0, 0, 0]
# Output 2:

#  [0, 2]


# Example Explanation
# Explanation 1:
# The first friend with the index value 0 and strength 3 can hit 4 times, 
# providing the lexicographically smallest array of maximum length 
# Explanation 1:
# The first friend with the index value 0 and strength 6 can only hit once, 
# making the Tushar's resistance to 5, now the third friend with the index value 2 can hit once, 
# providing the lexicographically smallest array of maximum length.
# class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return a list of integers
# 	def solve(self, A, B):
def solve(A, B):
    import collections
    friend_dict = collections.OrderedDict()
    temp = 100000 # 2147483647 # None
    n_B = len(B)
    punch_list = []
    for i in range(n_B):
        if B[i] < temp:
            friend_dict[i] = B[i]
            # punch_list.append(B[i])
            punch_list.append(i)
            temp = B[i]
    n_punch_list = len(punch_list)
    # print(punch_list)
    # curr_A = A
    strength_list = [friend_dict[x] for x in punch_list]
    if len(strength_list) == 0:
        return []
    min_strength = min(strength_list)
    # print(min_strength, punch_list)
    count = 0
    result = []
    remain_A = A
    # print(strength_list)
    # print(punch_list)
    # punch_list = ([punch_list for _, punch_list in sorted(zip(strength_list, punch_list))])
    # strength_list.sort()
    while (count < n_punch_list):
        # amt_can_bear = A - punch_list[count]
        amt_can_bear = remain_A - friend_dict[punch_list[count]]
        # print(count, amt_can_bear, 1 + amt_can_bear / min_strength,  A / min_strength)
        # print(A, friend_dict[punch_list[count]], count, min_strength, amt_can_bear, 1 + A - friend_dict[punch_list[count]] / min_strength,  A / min_strength)
        if (amt_can_bear >= 0):
            # print(count)
            max_hit = remain_A // min_strength
            cur_hit = 1 + amt_can_bear // min_strength
            # print('here')
            if (cur_hit == max_hit):
                # print('there')
                result.append(punch_list[count])
                remain_A -= friend_dict[punch_list[count]]
                continue
            else:
                count += 1
        else:
            count += 1
    # print(result)
    return(result)
solve(A, B)   

A = 10
B = [ 8, 8, 6, 5, 4 ]
    
# Suggested:
#     class Solution:
#     # @param A : integer
#     # @param B : list of integers
#     # @return a list of integers
#     def solve(self, r, S):
        
#         val, idx = min((val, idx) for (idx, val) in enumerate(S))
#         ret = [idx] * (r // val)
#         diff = r % val

#         i = 0
#         for j in range(idx):
#             if diff == 0 or i == len(ret):
#                 break
#             elif 0 < S[j] - val <= diff:
#                 while 0 < S[j] - val <= diff:
#                     if i == len(ret):
#                         break
#                     ret[i] = j
#                     i += 1
#                     diff -= (S[j] - val)
#         return ret
# import scala.collection.mutable.ArrayBuffer

# class Solution {
#   def solve(k: Int, as: Array[Int]): Array[Int]  = {
#     val minKick = as.min
#     val result = new ArrayBuffer[Int]()
#     var i = 0
#     var r = k
#     while (i < as.length) {
#       if (as(i) <= r && 1 + (r - as(i)) / minKick == r / minKick) {
#         r -= as(i)
#         result += i
#       }
#       else i += 1
#     }
#     result.toArray
#   }
# }
# GO
# /**
#  * @input A : Integer
#  * @input B : Integer array
#  * 
#  * @Output Integer array.
#  */
# func solve(A int , B []int )  ([]int) {
#     resistance := A
#     strengths := B
    
#     n := len(strengths)
#     min_strength := 1<<31-1
#     candidate_strengths := []int{}
#     idx_of := map[int]int{}

#     for i := 0; i < n; i++ {
#         if strengths[i] < min_strength {
#             min_strength = strengths[i]
#             candidate_strengths = append(candidate_strengths, strengths[i])
#             idx_of[strengths[i]] = i
#         }
#     }

#     n = len(candidate_strengths)
#     result := []int{}
#     i := 0
#     for i < n {
#         cur_strength := candidate_strengths[i];
#         if cur_strength <= resistance {
#             resistance_left := resistance - cur_strength
#             max_hits := resistance / min_strength
#             cur_hits := 1 + resistance_left / min_strength
#             if cur_hits == max_hits {
#                 result = append(result, idx_of[cur_strength])
#                 resistance -= cur_strength
#                 continue
#             }
#         }
#         i++
#     }
#     return result
# }
    
