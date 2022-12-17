# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 12:22:51 2022

@author: USER
"""

# Problem Description

# Given a number A in a form of string.
# You have to find the smallest number that has same set of digits as A and is greater than A.
# If A is the greatest possible number with its set of digits, then return -1.

# Problem Constraints
#  1 <= A <= 10100000
#  A doesn't contain leading zeroes.

# Input Format
# First and only argument is an numeric string denoting the number A.

# Output Format
# Return a string denoting the smallest number greater than A with same set of digits , if A is the largest possible then return -1.

# Example Input
# Input 1:
 A = "218765"
# Input 2:
 A = "4321"
 
# Example Output
# Output 1: "251678"
# Output 2: "-1"

# Example Explanation
# Explanation 1:

#  The smallest number greater then 218765 with same set of digits is 251678.
# Explanation 2:

#  The given number is the largest possible number with given set of digits so we will return -1.

# class Solution:
    # @param A : string
    # @return a strings
    # def solve(self, A):
A = '14321'  # 21134


def solve(A):
    A = list(A)
    n_A = len(A)
    ix_right = n_A - 2
    while ix_right >= 0:
        if A[ix_right] < A[ix_right + 1]:
            break
        ix_right -= 1         

    if ix_right < 0:
        return -1
    else:
        for i in range(n_A - 1, ix_right, -1):
            if A[i] > A[ix_right]:
                A[i], A[ix_right] = A[ix_right], A[i]         
                break
   
        A[ix_right + 1: ] = reversed(A[ix_right + 1: ]) 
    return ''.join(A)
 
A = '1234'
A= '4321'
solve(A)


# Suggested Solution:
#     # Python program to find the smallest number which  
# # is greater than a given no. has same set of  
# # digits as given number 
  
# # Given number as int array, this function finds the  
# # greatest number and returns the number as integer 
# def findNext(number,n): 
#     # Start from the right most digit and find the first 
#     # digit that is smaller than the digit next to it
#     i=-1
#     for idx in range(n-1,0,-1): 
#         if number[idx] > number[idx-1]: 
#             i=idx
#             break
               
#     # If no such digit found,then all numbers are in  
#     # descending order, no greater number is possible 
#     if i == -1:
#         return "-1"
           
#     # Find the smallest digit on the right side of  
#     # (i-1)'th digit that is greater than number[i-1] 
#     x = number[i-1] 
#     smallest = i 
#     for j in range(i+1,n): 
#         if number[j] > x and number[j] < number[smallest]: 
#             smallest = j 
           
#     # Swapping the above found smallest digit with (i-1)'th 
#     number[smallest],number[i-1] = number[i-1], number[smallest] 
       
#     # X is the final number, in integer datatype  
#     x = 0
#     # Converting list upto i-1 into number 
#     for j in range(i): 
#         x = x * 10 + number[j] 
       
#     # Sort the digits after i-1 in ascending order 
#     number = sorted(number[i:]) 
#     # converting the remaining sorted digits into number 
#     for j in range(n-i): 
#         x = x * 10 + number[j]
#     return x
  
# class Solution:
#     # @param A : string
#     # @return a strings
#     def solve(self, A):
#         #list variable to integeres
#         int_list =[]
#         # converting characters to integers
#         for ch in A:
#             int_list.append(int(ch))
#         return findNext(int_list,len(int_list))
    
# Scala:
#     class Solution {
#     def solve(A: String): String  = {


#     def smallestOfGreat(array: Array[Char], v: Char): Int = {
#       def loop(pos: Int): Int = {
#         if (pos == array.length) - 1
#         else
#         if (array.charAt(pos) > v) loop(pos + 1) else pos
#       }

#       loop(0)
#     }

#     var lastButOne = A.length - 2

#     while (lastButOne >= 0 && A.charAt(lastButOne) >= A.charAt(lastButOne + 1))
#       lastButOne -= 1

#     if (lastButOne < 0 || lastButOne == 0 && A.charAt(0) == A.charAt(1)) "-1"
#     else {
#       val (before, after) = A.toArray.splitAt(lastButOne)
# //      println(s"before [${before.mkString("Array(", ", ", ")")}], after [${after.mkString("Array(", ", ", ")")}]")
#       // take the smallest among the greater than X
#       //      var minPos = after.tail.indexWhere(_ < after.head)
#       var minPos = smallestOfGreat(after.tail, after.head)

# //      println(s"head (1) ${after.head} minPos $minPos")
#       if (minPos == -1) minPos = after.length - 1

# //      println(s"head (2) ${after.head} minPos $minPos")
#       val min = after.tail.charAt(minPos - 1)

#       val tmp = after(0)
#       after(0) = after(minPos)
#       after(minPos) = tmp
#       val after2 = after.tail.sorted

#       val remaining = before.mkString + min ++ after2.mkString
#       //      println(s"remaining $remaining")
#       remaining
#     }
#   }






# }
# C++
#     string findNext(string number, int n)
# {
#    int i, j;

#    // I) Start from the right most digit and find the first digit that is
#    // smaller than the digit next to it.
#    for (i = n-1; i > 0; i--)
#        if (number[i] > number[i-1])
#           break;

#    // If no such digit is found, then all digits are in descending order
#    // means there cannot be a greater number with same set of digits
#    if (i==0)
#    {
#      return "-1";
#    }

#    // II) Find the smallest digit on right side of (i-1)'th digit that is
#    // greater than number[i-1]
#    char x = number[i-1];
#    int smallest = i;
#    for (j = i+1; j < n; j++)
#        if (number[j] > x && number[j] < number[smallest])
#            smallest = j;

#    // III) Swap the above found smallest digit with number[i-1]
#    swap(number[smallest], number[i-1]);
#    string a=number.substr(i);
#    string b=number.substr(0,i);
#     // IV) Sort the digits after (i-1) in ascending order 
#    sort(a.begin(),a.end());
#    string ans=b+a;
#    return ans;
# }

# string Solution::solve(string A) {
#     return findNext(A,A.size());
# }

# GO:
#     /**
#  * @input A : String
#  * 
#  * @Output string.
#  */
 
# import "sort"

# func solve(A string )  (string) {
#     if len(A) == 1 {
#         return "-1"
#     }

#     var digits []byte
#     res, i, pos := make([]byte, len(A)), 0, -1

#     for j := len(A) - 1; j > 0; j-- {
#         digits = append(digits, A[j])
#         if A[j] > A[j-1] {
#             pos = j - 1
#             break
#         }
#     }

#     if pos == -1 {
#         return "-1"
#     }

#     for i = 0; i < pos; i++ {
#         res[i] = A[i]
#     }

#     for j := 0; j < len(digits); j++ {
#         if A[pos] < digits[j] {
#             res[i], i = digits[j], i+1
#             digits[j] = A[pos]
#             break
#         }
#     }

#     sort.Slice(digits, func(m, n int) bool { return digits[m] < digits[n] })

#     for j := 0; j < len(digits); j++ {
#         res[i], i = digits[j], i+1
#     }

#     return string(res)
# }
