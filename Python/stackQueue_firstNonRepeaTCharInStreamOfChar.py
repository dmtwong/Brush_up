# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 17:38:57 2022

@author: USER
"""

################# Self Note #####################
# Will revisit later for this test case 

# "d" and "h" appeared so should be iiiiiiiier instead
# A : "iergxwhddh"

# The expected return value: 
# iiiiiiiiii
# Your function returned the following: 
# iiiiiiiier
######################################


# Problem Description
# Given a string A denoting a stream of lowercase alphabets. You have to make new string B.
# B is formed such that we have to find first non-repeating character each time a character 
# is inserted to the stream and append it at the end to B. If no non-repeating character 
# is found then append '#' at the end of B.
# Problem Constraints
# 1 <= length of the string <= 100000
# Input Format
# The only argument given is string A.
# Output Format
# Return a string B after processing the stream of lowercase alphabets A.
# Example Input
# Input 1:
 A = "abadbc"
# Input 2:
 A = "abcabc"
# Example Output
# Output 1: "aabbdd"
# Output 2: "aaabc#"
# Example Explanation
# Explanation 1:
#     "a"      -   first non repeating character 'a'
#     "ab"     -   first non repeating character 'a'
#     "aba"    -   first non repeating character 'b'
#     "abad"   -   first non repeating character 'b'
#     "abadb"  -   first non repeating character 'd'
#     "abadbc" -   first non repeating character 'd'
# Explanation 2:

#     "a"      -   first non repeating character 'a'
#     "ab"     -   first non repeating character 'a'
#     "abc"    -   first non repeating character 'a'
#     "abca"   -   first non repeating character 'b'
#     "abcab"  -   first non repeating character 'c'
#     "abcabc" -   no non repeating character so '#'
# class Solution:
    # @param A : string
    # @return a strings
    # def solve(self, A):
        
# a = deque()
# a
# a.append('f')
# a.append('z')
# a
# a.append('c')
# a.pop()
# a
# a
# a.popleft()
# a
# a.popleft()
# len(a) == 0
# a
# ''.join(a)
# a[0]
# a.popleft()
# len(a) == 0
# a[0] # need to use try in case queue is empty
a
# tmp1 = ['a', 'c', 'd']
# tmp2  = [2, 4, 3]

# ''.join(list(map(lambda x, y: x * y, tmp1, tmp2)))

def solve(A):
    from collections import deque 
    char_key = list()
    char_val = list()
    char_queue = deque()
    unique_queue = deque()
    repeatingChar = None    
    if len(A) == 0:
        return A
    # else:
    # repeatingChar = A[0]    
    # unique_queue.append(A[0])
    
    for i in A:
        # print('here is ', i)
        try: 
            ix = char_key.index(i)
            if len(unique_queue) == 0:
                char_queue.append("#")
                continue
            else:
                repeatingChar = unique_queue.popleft()
                # print("shouldn't it be b", repeatingChar)
            # print('There is', repeatingChar)
            char_queue.append(repeatingChar)
        except:
            ix = -1
            # print('Now:', repeatingChar)
            unique_queue.append(i)
            if repeatingChar == None:
                repeatingChar = unique_queue.popleft()
            char_queue.append(repeatingChar)        
        # repeatingChar = i
        if ix == -1:
            char_key.append(i)
            char_val.append(1)
        else:
            char_val[ix] += 1
    allRepeat = True
    if 1 in char_val:
        allRepeat = False
    # result = ''.join(list(map(lambda x, y: x * y, char_key, char_val)))
    # if allRepeat != True:
    #     char_queue.append("#")        
    return ''.join(char_queue)


 A = "abadbc"
# Input 2:
 A = "abcabc"
 A = "iergxwhddh" # test case expect: iiiiiiiiii but actual: iiiiiiiier

solve(A)            
        
    
    
    
    