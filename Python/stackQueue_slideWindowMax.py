# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 19:32:49 2022

@author: USER
"""

# Given an array of integers A.  There is a sliding window of size B which 

# is moving from the very left of the array to the very right. 

# You can only see the w numbers in the window. Each time the sliding window moves 

# rightwards by one position. You have to find the maximum for each window. 

# The following example will give you more clarity.

# The array A is [1 3 -1 -3 5 3 6 7], and B is 3.

# Window position	Max
# ———————————-	————————-
# [1  3  -1] -3  5  3  6  7	3
# 1 [3  -1  -3] 5  3  6  7	3
# 1  3 [-1  -3  5] 3  6  7	5
# 1  3  -1 [-3  5  3] 6  7	5
# 1  3  -1  -3 [5  3  6] 7	6
# 1  3  -1  -3  5 [3  6  7]	7
# Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

# Note: If B > length of the array, return 1 element with the max of the array.




# Input Format

# The first argument given is the integer array A.
# The second argument given is the integer B.
# Output Format

# Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1]
# For Example

# Input 1:
# Output 1:
#     C = [3, 3, 5, 5, 6, 7]
# class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
# 	def slidingMaximum(self, A, B):
    
def slidingMaximum(A, B):
    from collections import deque 
    n_A = len(A)
    # if n_A == 1:
    #     return A    
    # if n_A <= B:
    #     max_A = None
    #     for i in A:
    #         if max_A = None:
    #             max_A = i
    #         elif i > max_A:
    #             max_A = i
    #     return max_A
    # for i in range(n_A - B + 1): 
    #     sliding_queue.append(max(A[i:i+B])) 
            
    # return list(sliding_queue)

    # local_max = 0
    # list_local_max = list()
    # n_A  = len(A)
    # for i in range(n_A - B + 1):
    #     local_max = A[i]
    #     for j in range(1, B):
    #         if A[i + j] > local_max:
    #             local_max = A[i + j]
    #     list_local_max.append(local_max)
    # return list_local_max
    result = []
    sliding_queue = deque()
    for i in range(B):
        while sliding_queue and A[i] >= A[sliding_queue[-1]]:
            sliding_queue.pop() 
        sliding_queue.append(i)
    result.append(A[sliding_queue[0]])
    for i in range(B, n_A):
        # print(str(arr[sliding_queue[0]]) + " ", end="")
        remain_ix = i - B
        while sliding_queue and sliding_queue[0] <= remain_ix:
            sliding_queue.popleft()
        while sliding_queue and A[i] >= A[sliding_queue[-1]]:
            sliding_queue.pop()
        # print(i)
        sliding_queue.append(i)
        
        result.append(A[sliding_queue[0]])
    
    # result = []
    # # print(sliding_queue)
    # for i in sliding_queue:
    #     # print(A[i])
    #     result.append(A[i])
    return result
    # A = list(A)
    # result.append(sliding_one(A, B))

    # return result

    # A = [1, 3, -1, -3, 5, 3, 6, 7]
A = (1, 3, -1, -3, 5, 3, 6, 7)
B = 3
A = (1, )
B = 1
A = [ 287, 687, 73, 525, 152 ]
B = 5

slidingMaximum(A, B)

# ## Editorial
# from collections import deque

# class Solution:
#     # @param A : tuple of integers
#     # @param B : integer
#     # @return a list of integers
#     def slidingMaximum(self, A, B):
#         N = len(A)
#         result = []
#         queue = deque()
#         l = r = 0
#         while r < N:
            
#             while queue and A[queue[-1]] < A[r]:
#                 queue.pop()
            
#             queue.append(r)
            
#             if l > queue[0]:
#                 queue.popleft()
            
#             if r + 1 >= B:
#                 result.append(A[queue[0]])
#                 l+= 1
#             r +=1
            
#         return result
# class Solution {
#     def slidingMaximum(A: Array[Int], B: Int): Array[Int]  = {
#         import scala.collection.mutable
        
#         if (B >= A.length) Array(A.max)
#         else {
#           def add(q: mutable.ListBuffer[Int], int: Int): mutable.ListBuffer[Int] = {
#             while (q.nonEmpty && q.last < int) q.trimEnd(1)
#             q += int
#           }
    
#           val lb: mutable.ListBuffer[Int] = mutable.ListBuffer.empty
#           val ab: mutable.ArrayBuffer[Int] = mutable.ArrayBuffer.empty
    
#           for (i <- 0 until B) add(lb, A(i))
#           for (i <- B until A.length) {
#             ab += lb.head
#             if (lb.nonEmpty && lb.head == A(i - B)) lb.trimStart(1)
#             add(lb, A(i))
#           }
#           ab += lb.head
#           ab.toArray
#     }
#   }
# }
# vector<int> Solution::slidingMaximum(const vector<int> &A, int B) {
#     vector<int> res;
#     vector<int> deq(A.size() + 1);
#     int front = 0, back = -1;
#     for(int i = 0 ; i < A.size(); ++i){
#         while(front <= back && A[i] >= A[deq[back]]) back--;
#         deq[++back] = i;
#         if(deq[front] + B == i) front++;
#         if(i + 1 >= B) res.push_back(A[deq[front]]);
#     }
#     return res;
# }
# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer array.
#  */
# type Stack struct {
#     arr []int
# }
# func newStack() *Stack {
#     s:=Stack{}
#     s.arr=make([]int, 0)
#     return &s
# }
# func (s *Stack) Top() int {
#     return s.arr[len(s.arr)-1]
# }
# func (s *Stack) Push(c int) {
#     s.arr=append(s.arr, c)
# }
# func (s *Stack) Pop() int {
#     top:=s.arr[len(s.arr)-1]
#     s.arr=s.arr[:len(s.arr)-1]
#     return top
# }
# func (s *Stack) Size() int {
#     return len(s.arr)
# }

# func next_greater_element_index(A []int) []int {
#     res:=make([]int, len(A))
#     if len(A)==0 {
#         return res
#     }
#     s:=newStack()
#     s.Push(0)
#     var a, t int
#     for i:=1; i<len(A); i++ {
#         a=A[i]
#         for s.Size()>0 && A[s.Top()]<a {
#             t=s.Pop()
#             res[t]=i
#         }
#         s.Push(i)
#     }
#     for s.Size()>0 {
#         t=s.Pop()
#         res[t]=-1
#     }
#     return res
# }
# func max(A []int) int {
#     res:=A[0]
#     for i:=1; i<len(A); i++ {
#         if A[i]>res {
#             res=A[i]
#         }
#     }
#     return res
# }
# func slidingMaximum(A []int , B int )  ([]int) {
#     ngei:=next_greater_element_index(A)
#     diff:=len(A)-B+1
#     C:=[]int{}
#     if B>len(A) {
#         return []int{max(A)}
#     }
#     var j int
#     for i:=0; i<diff; i++ {
#         if ngei[i]==-1 {
#             C=append(C, A[i])
#         } else {
#             j=i
#             for ngei[j]<B &&  ngei[j]!=-1 {
#                 j=ngei[j]
#             }
#             C=append(C, A[j])
#         }
#         B+=1
#     }
#     return C
# }
