# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:45:56 2023

@author: USER
"""

# Problem Description
# Given a string A and integer B, what is maximal lexicographical string that can 
# be made from A if you do atmost B swaps.

# Problem Constraints
# 1 <= |A| <= 9
# A contains only digits from 0 to 9.
# 1 <= B <= 5

# Input Format
# First argument is string A.
# Second argument is integer B.

# Output Format
# Return a string, the naswer to the problem.

# Example Input
# Input 1:
A = "254"
B = 1
# Input 2:
A = "254"
B = 2
# Example Output
# Output 1:
#  524
# Output 2:
#  542
# Example Explanation
# Explanation 1:
#  Swap 2 and 5.
# Explanation 2:
# Swap 2 and 5 then swap 4 and 2.

# class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    # def solve(self, A, B):
def solve(A, B):
    # cur_max_A = A
    global max_A
    max_A = [A]
    def helper(A, B, cur_max_A, ix):
        global max_A
        # print('here is ', A, B, cur_max_A, ix, max_A)
        if B == 0:
            return A  
        n_A = len(A)    
        cur_digit = A[ix]     
        for i in range(ix + 1, n_A):
            if int(A[i]) > int(cur_digit):
                cur_digit = A[i]

        if(cur_digit != A[ix]):
            B -= 1
        for i in range(ix, n_A):
            if(A[i]==cur_digit):
                A[ix], A[i] = A[i], A[ix]
                mod_A = "".join(A)
                # print(mod_A, 'this is', ix, cur_max_A)
                if int(mod_A) > int(cur_max_A):
                       cur_max_A = mod_A
                       max_A.append(cur_max_A)
                       # print(max_A)
                      # cur_max_A.append(mod_A)
                helper(A, B , max(cur_max_A), ix + 1)     
                A[ix], A[i] = A[i], A[ix]
        return max_A    
    list_A = list(A)
    result = helper(list_A, B, A, 0)    
    return(max(result))

solve(A, B)
A = "7599"
B = 2

# Editorial
# class Solution:
#     # @param A : string
#     # @param B : integer
#     # @return a strings
#     def solve(self, A, B):
#         def swap(string,i,j):
#             s1=string[:i]
#             s2=string[i+1:j]
#             s3=string[j+1:]
#             return s1+string[j]+s2+string[i]+s3
#         def sswap(A,B,ans):
#             if B==0:
#                 return ans[0]
#             for i in range(len(A)):
#                 for j in range(i+1,len(A)):
#                     if A[j]>A[i]:
#                         temp=swap(A,i,j)
#                         if ans[0]<temp:
#                             ans[0]=temp
#                         sswap(temp,B-1,ans)
                        
#         ans=[A]
#         sswap(A,B,ans)
#         return ans[0]
                
#  class Solution {
#     def swap(s: String, i: Int, j: Int): String = {
#     val cs = s.toCharArray
#         val swp = cs(i)
#         cs(i) = cs(j)
#         cs(j) = swp
#         new String(cs)
#     }
  
#     def solve(A: String, B: Int): String = {
#         var maxString = A
#         def loop2(swaps: Int, soFar: String): Unit = {
#           var mutableStr = soFar
#           if (swaps > 0)
#             for {i <- 0 until soFar.length
#                  j <- i + 1 until soFar.length
#                  } {
#               if (mutableStr.charAt(j) > mutableStr.charAt(i)) {
#                 mutableStr = swap(mutableStr, i, j)
#                 loop2(swaps - 1, mutableStr)
#                 mutableStr = swap(mutableStr, i, j)
#               }
#             } else
#             if (mutableStr > maxString) maxString = mutableStr
    
#         }
    
#         loop2(B, A)
#         maxString
#     }
# }

# void swap(char &a,char &b)
# {
#     char c=a; a=b; b=c;
# }

# string ans;
# int n;

# void check(int i,string &str,int k)
# {
#     if(ans<str)
#     ans=str;
    
#     if(!k || i==n)
#     return;
    
#     check(i+1,str,k);

#     for(int j=i+1;j<n;j++)
#     {
#         if(str[j]>str[i])
#         {
#             swap(str[j],str[i]); 
#             check(i+1,str,k-1);
#             swap(str[j],str[i]); 
#         }
#     }
# }
# string Solution::solve(string str, int k) 
# {
#      ans=str;
#     n=str.length();
    
#      check(0,str,k);
#      return ans;
# }

# /**
#  * @input A : String
#  * @input B : Integer
#  * 
#  * @Output string.
#  */
# import "strings" 
# func solve(A string , B int )  (string) {
#     maxSoFar := A
#     a := strings.Split(A,"")
#     recur(a,0,B,&maxSoFar)
#     return maxSoFar
# }

# func swap(a []string, i, j int) []string {
#     temp := a[i]
#     a[i] = a[j]
#     a[j] = temp
#     return a
# }

# func compStringArr(a []string, b string) bool {
#     temp := ""
#     for _,v := range a{
#         temp +=v
#     }
#     return temp > b
# }

# func recur(a []string, curn int, count int, maxSoFar *string) {
#     if curn == len(a) || count == 0 {
#         return
#     }
#     //findMaxChar
#     maxChar := a[curn]
#     for i:= curn+1 ; i< len(a);i ++ {
#         if a[i] > maxChar {
#             maxChar = a[i]
#         }
#     }
#     //if MaxChar is same as curn, move on to next index
#     if maxChar == a[curn] {
#         recur(a, curn+1, count, maxSoFar)
#     } else {
#         //check if MaxChar at more than one place, recurse further with every possible swap
#         for i := curn+1 ; i < len(a) ; i++ {
#             if a[i] == maxChar {
#                 //if maxChar swap
#                 a = swap(a, curn, i)
#                 //compare to maxSoFar and save
#                 if  compStringArr(a, *maxSoFar) {
#                     temp := ""
#                     for _,v := range a{
#                         temp +=v
#                     }
#                     *maxSoFar = temp
#                 }
#                 //recur by decrementing remaingng swaps(count)
#                 recur(a, curn+1, count-1, maxSoFar)
#                 //swap back in place, to try other possible swap
#                 a = swap(a, i, curn)
#             }
#         }
#     }
# }