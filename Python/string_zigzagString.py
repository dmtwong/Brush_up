# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 22:01:54 2022

@author: mingt
"""

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
#     (you may want to display this pattern in a fixed font for better legibility)

# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R
# And then read line by line: PAHNAPLSIIGYIR

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
# **Example 2 : **

# ABCD, 2 can be written as

# A....C
# ...B....D
# and hence the answer would be ACBD.
# class Solution:
	# @param A : string
	# @param B : integer
	# @return a strings
# 	def convert(self, A, B):
def convert(A, B):
    n_A = len(A)
    if B == 1:   
        return A
    result = ["" for x in range(n_A)]
    # print(result)
    
    row_ix = 0
    for i in range(n_A):
        # print(A[i])
        # print(row_ix)
        result[row_ix] += A[i]
        if row_ix == B - 1:
            down = False
        elif row_ix == 0:
            down = True
        if down:
            row_ix += 1
        else:
            row_ix -= 1
        # print(down)
    return(''.join(result))

 
A = "PAHNAPLSIIGYIR"
B = 3
convert(A, B)

# Suggested:
    
# import itertools

# class Solution:
#     # @param A : string
#     # @param B : integer
#     # @return a strings
#     def convert(self, A, B):
#         if len(A)<=B or B==1:
#             return A

#         BB = 2*B-2
#         ans = ''

#         for i in range(B):
#             if i==0 or i==B-1:
#                 ans += ''.join(A[i::BB])
#             else:
#                 a = A[i::BB]
#                 b = A[(BB-i)::BB]
#                 ans += ''.join(''.join([x,y]) for x,y in itertools.zip_longest(a,b,fillvalue=''))

#         return ans
# class Solution {
#     def convert(s: String, rows: Int): String  = {
#       if (rows == 1) s
#       else {
#         val b = Array.fill[StringBuilder](rows)(new StringBuilder)
#         s.foldLeft((false, 0)){ case ((down, row), c) => {
#           b(row) += c
#           if (row == 0) (true, 1)
#           else if (row == rows - 1) (false, row - 1)
#           else if (down) (down, row + 1) else (down, row - 1)
#         }}
#         b.mkString
#       }
#     }
# }
# /**
#  * @input A : String
#  * @input B : Integer
#  * 
#  * @Output string.
#  */

# func convert(A string , B int )  (string) {
#     res := make([]byte, 0, len(A))
#     if B == 1 {
#         return A
#     }
#     for row:=0; row<B; row++ {
#         i:=row
#         toSkipA := 2*(B-2-row)+2
#         toSkipB := 2*(row-1)+2
#         if row == 0 {
#             toSkipB = toSkipA
#         }
#         if row==B-1 {
#             toSkipA = toSkipB
#         }
#         //fmt.Printf("%d %d %d   ", row, toSkipA, toSkipB)
#         //continue
#         step :=0 
#         for i < len(A) {
#             res = append(res, A[i])
#             if step%2==0 {
#                 i += toSkipA
#             } else {
#                 i+=toSkipB
#             }
#             step++
#         }
#     }
#     return string(res)
# }
# public class Solution
# {
#     public String convert(String A, int B)
#     {
#         if(B < 2)
#             return A;
        
#         StringBuilder str = new StringBuilder();
        
#         int rows_below = B - 1;
#         int rows_above = 0;
#         for(int i=0; i<B; i++)
#         {
#             if(rows_below == 0)
#                 rows_below = B - 1;
            
#             for(int j=i, is_going_down=1; j<A.length(); )
#             {
#                 str.append( A.charAt(j) );
                
#                 if(i == 0)
#                 {
#                     j+=(rows_below*2);
#                     continue;
#                 }
#                 else if(i == B-1)
#                 {
#                     j+=(rows_above*2);
#                     continue;
#                 }
                
#                 if(is_going_down == 1)
#                 {
#                     j+=(rows_below*2);
#                     is_going_down = 0;
#                 }
#                 else
#                 {
#                     j+=(rows_above*2);
#                     is_going_down = 1;
#                 }
#             }
            
#             rows_below--;
#             rows_above++;
#         }
            
                
#         return str.toString();
#     }
# }
# string Solution::convert(string s, int b)
# {
#     if(b==1)
#     return s;
#     vector<vector<char> > v(b);
#     int i,l=s.length(),f=0,k=0;
#     for(i=0;i<l;i++)
#     {
#         if(f==0)
#         {
#             v[k].push_back(s[i]);
#             k++;
#             if(k==b)
#             {
#                 k-=2;
#                 f=1;
#             }
#         }
#         else
#         {
#             v[k].push_back(s[i]);
#             k--;
#             if(k==-1)
#             {
#                 k+=2;
#                 f=0;
#             }
#         }
#     }
#     string w="";
#     for(i=0;i<v.size();i++)
#     {
#         for(int j=0;j<v[i].size();j++)
#         {
#             w+=v[i][j];
#         }
#     }
#     return w;
# }
