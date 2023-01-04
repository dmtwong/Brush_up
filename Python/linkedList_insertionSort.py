# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:23:41 2023

@author: USER
"""

# Sort a linked list using insertion sort.

# We have explained Insertion Sort at Slide 7 of Arrays

# Insertion Sort Wiki has some details on Insertion Sort as well.

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
# class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
# 	def insertionSortList(self, A):
def insertionSortList(A):
    if (not A) or (not A.next): # no need to sort if no ele or only 1 
        return A
    # if not A.next:
        # return A
    temp = ListNode(None)
    temp.next = A
    last = A
    curr = A.next
    
    while curr:
        # print('here', curr.val, last.val)
        curr_next = curr.next
        curr_temp = temp
        if curr.val < last.val:
            while (curr_temp.next != curr) and (curr_temp.next.val <= curr.val):
                # print('there',curr_temp.val)
                curr_temp = curr_temp.next
            if curr_temp.next != curr:
                # print('where')
                last.next = curr.next
                store     = curr_temp.next
                curr_temp.next = curr
                curr.next      = store
        else:
            # print('!')
            last = curr
        # print('!!')
        curr = curr_next
    return temp.next

# Example :

# Input : 1 -> 3 -> 2

# Return 1 -> 2 -> 3

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
temp = insertionSortList(node1)
while temp != None:
    print(temp.val)
    temp = temp.next    

# Edityorial:
#     # Definition for singly-linked list.
# # class ListNode:
# #    def __init__(self, x):
# #        self.val = x
# #        self.next = None

# class Solution:
#     # @param A : head node of linked list
#     # @return the head node in the linked list
#     def insertionSortList(self, A):
#         head = A
#         point = head
#         A = A.next
        
#         while A:
#             point = head
#             while point != A:
#                 if point.val > A.val:
#                     tmp = point.val
#                     point.val = A.val
#                     A.val = tmp
#                 else:
#                     point = point.next
#             A = A.next
#         return head
# /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def insertionSortList(A: ListNode): ListNode  = {

#     def insert(first: ListNode, n: ListNode): ListNode = {
#       val nFirst = if (first.value >= n.value) {
#         n.next = first
#         n
#       } else {
#         var node = first
#         while (node.next != null && node.next.value < n.value) node = node.next
#         val tmp = node.next
#         node.next = n
#         n.next = tmp
#         first
#       }
#       nFirst
#     }

#     if (A == null || A.next == null) A
#     else {
#       var f: ListNode = null
#       var n = A
#       while (n != null) {
#         val tmp = n.next
#         if (f == null) {
#           f = new ListNode(n.value)
#         } else {
#           n.next = null
#           val nf = insert(f, n)
#           f = nf
#         }
#         n = tmp
#       }
#       f
#     }
#   }
# }
#           /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
# ListNode* Solution::insertionSortList(ListNode* A) {
#     if (!A || !A->next) return A;
    
#     ListNode *newHead = new ListNode(A->val);
#     ListNode *it = A->next;
#     ListNode *it_inner, *next, *oldHead, *oldNext;
#     while (it) {
#         it_inner = newHead;
#         next = it->next;
#         if (it->val <= newHead->val) {
#             oldHead = newHead;
#             newHead = it;
#             newHead->next = oldHead;
#         } else {
#             while (it_inner->next) {
#                 if (it->val > it_inner->val && it->val <= it_inner->next->val) {
#                     oldNext = it_inner->next;
#                     it_inner->next = it;
#                     it->next = oldNext;
#                 }
#                 it_inner = it_inner->next;
#             }
#             if (!it_inner->next && it->val > it_inner->val) {
#                 it_inner->next = it;
#                 it->next = NULL;
#             }
#         }
#         it = next;
#     }
#     return newHead;
# }
            
#             /**
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
#  * 
#  * @Output head pointer of list.
#  */
# func insertionSortList(A *listNode )  (*listNode) {

#     if(A==nil||A.next==nil){
#         return A
#     }
    
#     var result *listNode
    
#     temp:=A
    
#     for temp!=nil{
#         next:= temp.next
#         //insert at head position
#         if(result==nil || result.value>= temp.value){
#             temp.next = result
#             result = temp
#         }else{
#             //find the node position where to insert
#             sortedRef := result
#             for (sortedRef!=nil && sortedRef.next!=nil && 
#             sortedRef.next.value<temp.value){
#                 sortedRef = sortedRef.next
#             }
#             temp.next = sortedRef.next
#             sortedRef.next = temp
#         }
#         temp= next
#     }
#     return result


# }