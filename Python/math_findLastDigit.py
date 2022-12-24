# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 22:01:31 2022

@author: mingt
"""

# Problem Description
 
 # Find last digit of the number AB.
# A and B are large numbers given as strings.


# Problem Constraints
# 1 <= |A| <= 105
# 1 <= |B| <= 105


# Input Format
# First argument is a string A.
# First argument is a string B.


# Output Format
# Return an integer.


# Example Input
# Input 1:
# A = 2
# B = 10
# Input 2:
# A = 11
# B = 11


# Example Output
# Output 1:
# 4
# Output 2:
# 1


# Example Explanation
# Explanation 1:
# 210 = 1024, hence last digit is 4.
# Explanation 2:
# 1111 = 285311670611, hence last digit is 1.
# class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
def solve(A, B):
    a = int(A)
    b = int(B)
    # result = a ** b
    # return result % 10
    
    if b == 0:
        return  1
    if a == 0: 
        return  0
    
    last_A = int(A[-1])
    
    if b % 4 == 0:
        power = 4
    else:
        power = b % 4
         
    result = last_A ** power     
    return result % 10

# Suggested:
#     class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def solve(self, A, B):
#         num1=int(A)%10
#         num2=int(B)%4
#         if num2==0:
#             num2=4
#         return (num1**num2)%10
    
#     public class Solution {
#     public int solve(String A, String B) {
#         int k = A.charAt(A.length() - 1) - '0';
#         ArrayList<Integer> v = new ArrayList<Integer>();
#         v.add(k);
#         while (true) {
#             int x = v.get(v.size() - 1) * k;
#             x %= 10;
#             if (x == v.get(0)) {
#                 break;
#             } else {
#                 v.add(x);
#             }
#         }
#         int n = v.size();
#         int b = 0;
#         int mul = 1;
#         for (int i = B.length() - 1; i >= 0; --i) {
#             int x = B.charAt(i) - '0';
#             b = (b + x * mul) % n;
#             mul = (mul * 10) % n;
#         }
#         b = (b - 1 + n) % n;
#         return v.get(b);
#     }
# }
                
#    int Solution::solve(string A, string B) {
#     int k = A.back() - '0';
#     vector<int> v(1, k);
#     while (true) {
#         int x = v.back() * k;
#         x %= 10;
#         if (x == v[0]) {
#             break;
#         } else {
#             v.push_back(x);
#         }
#     }
#     int n = v.size();
#     int b = 0;
#     int mul = 1;
#     for (int i = B.size() - 1; i >= 0; --i) {
#         int x = B[i] - '0';
#         b = (b + x * mul) % n;
#         mul = (mul * 10) % n;
#     }
#     b = (b - 1 + n) % n;
#     return v[b];
# }