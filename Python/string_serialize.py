# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:02:15 2023

@author: USER
"""

# Problem Description 
# You are given an array A of strings and we have to serialize it and return the serialized string.
# Serialization: Scan each element in a string, calculate its length and append it with a string and a element separator or deliminator (the deliminator is ~). We append the length of the string so that we know the length of each element.
# For example, for a string 'interviewbit', its serialized version would be 'interviewbit12~'.

# Problem Constraints
# 1 <= |A| <= 1000
# 1 <= |Ai| <= 1000
# Ai only contains lowercase english alphabets.

# Input Format
# The first argument A is the string array A.
# Output Format
# Return a single integer denoting the serialized string.


# Example Input
# Input 1:
A = ['scaler', 'academy']
# Input 2:

A = ['interviewbit']


# Example Output
# Output 1:
# scaler6~academy7~
# Output 2:

# interviewbit12~


# Example Explanation
# Explanation 1:
# Length of 'scaler' is 6 and academy is 7. So, the resulting string is scaler6~academy7~.
# Explanation 2:

# Explained in the description above.

# class Solution:
    # @param A : list of strings
    # @return a strings
    # def serialize(self, A):
def serialize(A):
    n_A = len(A)
    result = ""
    for i in range(n_A):
        n_curr_i = len(A[i])
        # result = result + "~" + A[i] + str(n_curr_i)
        result = result + A[i] + str(n_curr_i) + "~"
    # n_result = len(result)
    # return result[1:]
    return result
serialize(A)


A = [ "ajjuqilyyj", "yuqbodnqqk", "xeskbielhz", "falbnizyfc", "kjwiqxfiep", "tmyikegcvz", "zmoouapqva", "sdqjiiznqy", "xwdtnudeoc", "zpnhuvghrs" ]
# The expected return value: 
exp_1 = 'ajjuqilyyj10~yuqbodnqqk10~xeskbielhz10~falbnizyfc10~kjwiqxfiep10~tmyikegcvz10~zmoouapqva10~sdqjiiznqy10~xwdtnudeoc10~zpnhuvghrs10~'
act_1 = serialize(A)
exp_1 == act_1
max(len(act_1),len(exp_1))
for i in range(130):
    try:
        if (exp_1[i] != act_1[i]):
            print(i)
            print(exp_1[i])
            print(act_1[i])
    except:
            print('error at ',i)
exp_1[129]
act_1[129]
