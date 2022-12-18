# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:37:47 2022

@author: USER
"""

# self note: this answer lean on other's work need to review the suggest solution again 

# K reverse linked list

# Bookmark
# Medium
# 66.4% Success

# 281

# 4
# Asked In:
# Microsoft
# Amazon
# Given a singly linked list and an integer K, reverses the nodes of the

# list K at a time and returns modified linked list.

# NOTE : The length of the list is divisible by K

# Example :

# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

# Try to solve the problem using constant extra space.

# Definition for singly-linked list.


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
# 	def reverseList(self, A, B):


def reverseList(A, B):
    # import copy
    if not A or B == 1:
        return A
    dummy = ListNode(-99) 
    dummy.next = A
    prev = dummy
    curr = dummy
    next_node = dummy
    n_A = 0
    remain_A = 0
    
    while curr:
        curr = curr.next
        n_A += 1
 
    while next_node:
        curr = prev.next  
        next_node = curr.next  
        remain_A = n_A > B and B or n_A - 1
        for i in range(1, remain_A):
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            next_node = curr.next
        prev = curr
        n_A -= B
 
    return dummy.next

# # node_0 = ListNode(0)
# node_1a = ListNode(1)    #2371143182464
# # id(node_1a)
# # id(node_1b)
# # id(node_1c)
# node_1b = ListNode(2) #2371143182992
# node_1c = ListNode(3) #2371143182560
# node_1d = ListNode(4) #2371143182560
# node_1e = ListNode(5) #2371143182560
# node_1f = ListNode(6) #2371143182560

# # node_0.next = node_1a
# node_1a.next = node_1b
# node_1b.next = node_1c
# node_1c.next = node_1d
# node_1d.next = node_1e
# node_1e.next = node_1f

# result = reverseList(node_1a, 3)

#      result.val
#     result.next.val
#  result.next.next.val
# A : [ 6 -> 10 -> 0 -> 3 -> 4 -> 8 ]
# B : 3

# The expected return value: 
# 0 -> 10 -> 6 -> 8 -> 4 -> 3 



# Suggested Solution:
    
# # Definition for singly-linked list.
# # class ListNode:
# #    def __init__(self, x):
# #        self.val = x
# #        self.next = None

# class Solution:
#     # @param A : head node of linked list
#     # @param B : integer
#     # @return the head node in the linked list
#     def reverseList(self, A, B):
#         if B == 1:
#             return A
#         l=None
#         prev,curr=None,A
#         while curr!=None:
#             k=B
#             head=curr
#             p,n=None,curr.next
#             while curr!=None and k>1:
#                 curr.next=p
#                 p=curr
#                 curr=n
#                 n=n.next if n else None
#                 k-=1
#             head.next=curr.next
#             curr.next=p
#             if prev:
#                 prev.next=curr
#             else:
#                 l=curr
#             prev=head
#             curr=head.next
#         return l
# Scala:
# /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def reverseList(A: ListNode, B: Int): ListNode  = {
#     if (B < 2) A
#     else {

#       var n = A
#       var last = A
#       var acc: ListNode = null

#       while (n != null) {
#         var i = 0
#         var s: ListNode = null
#         val sLast = n

#         while (i < B) {
#           val t = n.next
#           n.next = s
#           s = n
#           n = t
#           i += 1
#         }

#         if (acc == null) acc = s
#         else last.next = s
#         last = sLast

#       }

#       acc
#     }
#   }
# }


# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
# ListNode* reverse(ListNode* A) {
#     if (!A -> next)
#         return A;
#     ListNode *next = A -> next;
#     A -> next = NULL;
#     ListNode *reversed = reverse(next);
#     next -> next = A;
#     return reversed;
# }

# ListNode* Solution::reverseList(ListNode* A, int K) {
#     ListNode *reversedFirst = A;
#     for (int i = 1; i < K; i += 1) {
#         reversedFirst = reversedFirst -> next;
#     }

#     // prev is the last element of the previous bucket
#     // first is the first element of the current bucket
#     // last is the last element of the current bucket
#     ListNode *prev = new ListNode(0);
#     ListNode *first;
#     prev -> next = A;
#     ListNode *last = prev;
    
#     while (last -> next) {
#         // Find the current bucket
#         for (int i = 1; i <= K; i += 1) {
#             last = last -> next;
#         }
#         first = prev -> next;
#         // Unlink the bucket from the list and reverse it
#         prev -> next = NULL;
#         ListNode *next = last -> next;
#         last -> next = NULL;
#         reverse(first);
#         // Attack the reversed bucket to the list
#         // After the bucket is reversed, first and last are reversed
#         prev -> next = last;
#         first -> next = next;
#         prev = last = first;
#     }
#     return reversedFirst;
# }

# /**
#  * Definition for singly-linked list.
#  * type listNode struct {
#  *     value int
#  *     next *listNode
#  * }
#  * 
#  * func listNode_new(val int) *listNode{
#  *     var node *listNode = new(listNode)
#  *     node.value = val
#  *     node.next = nil
#  *     return node
#  * }
#  */
# /**
#  * @input A : Head pointer of linked list 
#  * @input B : Integer
#  * 
#  * @Output head pointer of list.
#  */
# func reverse(a *listNode) *listNode {
#     var curr, prev, next *listNode
#     curr=a
#     for curr!=nil {
#         next=curr.next
#         curr.next=prev
#         prev=curr
#         curr=next
#     }
#     return prev
# }
# func reverseList(A *listNode , B int )  (*listNode) {
#     k, head :=B, A
#     var originalHead, tmp, newHead, prev *listNode
#     var firstTime bool = true
#     for head!=nil {
#         if k==B {
#             originalHead=head
#         }
#         if k==1 {
#             tmp=head.next
#             head.next=nil
#             newHead=reverse(originalHead)
#             if firstTime {
#                 A=newHead
#                 firstTime=false
#             }
#             if prev!=nil {
#                 prev.next=newHead
#             }
#             prev=originalHead
#             k=B
#             head=tmp
#             continue
#         }
#         head=head.next
#         k-=1
#     }
#     return A
# }
