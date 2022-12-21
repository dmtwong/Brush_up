# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:09:01 2022

@author: USER
"""

# Problem Description

# Given a binary array A and a number B, we need to find length of the longest 
# subsegment of ‘1’s possible by changing at most B ‘0’s.


# Problem Constraints
#  1 <= N, B <= 105
#  A[i]=0 or A[i]=1
 
# Input Format
# First argument is an binary array A.
# Second argument is an integer B.

# Output Format
# Return a single integer denoting the length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.

# Example Input
# Input 1:

 A = [1, 0, 0, 1, 1, 0, 1]
 B = 1
 
# Input 2:
 A = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
 B = 2


# Example Output
# Output 1:

#  4
# Output 2:

#  5


# Example Explanation
# Explanation 1:

#  Here, we should only change 1 zero(0). Maximum possible length we can get is by changing the 3rd zero in the array,
#  we get a[] = {1, 0, 0, 1, 1, 1, 1}
# Explanation 2:

#  Here, we can change only 2 zeros. Maximum possible length we can get is by changing the 3rd and 4th (or) 4th and 5th zeros.

# class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # def solve(self, A, B):

def solve(A, B):
    n_A = len(A)
    count = 0
    cur_ix = 0
    result = 0
    
    for i in range(n_A):
        if A[i] == 0:
            count += 1
        
        while count > B:
            if A[cur_ix] == 0:
                count -= 1
            cur_ix += 1 
        cur_len = i - cur_ix + 1
        if (cur_len > result):
            result = cur_len
            
    return result
        
solve(A, B)

# // Suggested Solution:
    # class Solution:
    # # @param A : list of integers
    # # @param B : integer
    # # @return an integer
    # def solve(self, A, B):
    #     i=0
    #     j=0
    #     ans=0
    #     while i<len(A):
    #         if A[i]==0:
    #             B-=1
    #         if B<0:
    #             if A[j]==0:
    #                 B+=1
    #             j+=1
    #         i+=1
    #     return i-j
# Scala:    
# class Solution {
#     def solve(A: Array[Int], B: Int): Int  = {
    
#         val arr = A
#         val maxUpdates = B
    
#         var currUpdates = 0
#         var start = 0
#         var end = 0
    
#         while(currUpdates < maxUpdates && end < arr.size) {
#           if(arr(end) == 0) currUpdates = currUpdates + 1
#           end = end + 1
#         }
    
#         while(end < arr.size && arr(end) == 1) end = end + 1
    
#         if(end == arr.size) return arr.size
    
#         var currSize = (end - 1) - start + 1
#         var maxSize = currSize
    
#         while(end < arr.size) {
    
#           arr(start) match {
#             case 0 => {
#               start = start + 1
#             }
#             case 1 => {
#               while(start < arr.size && arr(start) == 1) start = start + 1
#               start = start + 1
#             }
#           }
    
#           var counter = 0
#           while(end < arr.size && (counter < 1 || arr(end) == 1)) {
#             if(arr(end) == 0) counter = counter + 1
#             end = end + 1
#           }
    
#           if(end == arr.size) return Math.max(maxSize, (end - 1) - start + 1)
    
#           currSize = (end-1) - start + 1
#           maxSize = Math.max(currSize, maxSize)
#         }
    
#         maxSize
#     }
# }

# GO
# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# func solve(A []int , B int )  (int) {
#     size := len(A)
#     if size == 0 {
#         return 0
#     }

#     countZero := 0
#     begin := 0
#     maxLength := 0

#     for i := 0; i < size; i++ {
#         if A[i] == 0 {
#             countZero += 1
#         }

#         if countZero == B + 1 {
#             j := begin
#             for ; j <= i; j++ {
#                 if A[j] == 0 {
#                     j += 1
#                     countZero -= 1
#                     break
#                 }
#             }

#             begin = j
#         } else {
#             if maxLength < i - begin + 1 {
#                 maxLength = i - begin + 1
#             }
#         }
#     }

#     return maxLength
# }

# C++:
#     int Solution::solve(vector<int> &A, int B) {

#     int i = 0;
#     int j = 1;
#     int highest = 0;
#     int noofzeroes = 0;
    
#     if(A.size()==1&&B>=1){
#         return 1;
#     } else if(A.size()==1&&B==0&&A[0]==0){
#         return 0;
#     } else if(A.size()==1&&B==0&&A[0]==1){
#         return 1;
#     } 

    

#         if(A[0]==0) noofzeroes++;
#         if(A[1]==0) noofzeroes++;

#     while(i<A.size() && j<A.size()){
        
#         // cout<<"looping"<<endl;
#         if(noofzeroes<=B){

#         int count = j - i + 1;
#         if(count>highest){
#             highest = count;
#         }
#             if((j+1)==A.size()){
#                 break;
#             }
#             if(A[j+1]==1){
#                 j++;
#             } else if(A[j+1]==0){
#                 if(noofzeroes<B){
#                     j++;
#                     noofzeroes++;
#                 } else if(noofzeroes == B){
#                     if(A[i]==0){
#                         noofzeroes--;
#                         i++;
#                     } else{
#                         i++;
#                     }
#                 }
#             }
#         } else {
#                 if(A[i]==0){
#                     i++;
#                     noofzeroes--;
#                 } else if(A[i]==1){
#                     i++;
#                 }
#         }


#     }

#     return highest;


# }