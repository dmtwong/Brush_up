# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 21:38:47 2022

@author: USER
"""

# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.

# For example,

# Given 1->2->3->3->4->4->5, return 1->2->5.

# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
# 	def deleteDuplicates(self, A):

# set_A = (1,2,5)    
# 1 in set_A
# 3 in set_A
# set_A.__add__((6,))
# set_A = set_A.__add__((None,))
# set_A = set_A.__add__((6,))
# set_A.
# set_A = list()
# set_A.append(None)
# set_A.append(1)
# set_A
def deleteDuplicates(A):
    if not A or A.next == None:
        return A    
    current = A  
    # curr_next = A.next
    dummy = curr_prev = ListNode(None)
    dummy.next = current
    # set_A = []
    # sing_result = []
    # dup_result = []
    while (current and current.next): 
        # print(current.val, current.next)
        curr_key = current.val
        # if curr_key not in set_A and curr_key not in dup_result:
        #     print("here", current.val, current.next)
        #     # curr_prev.next = current
        #     set_A.append(current.val)
        #     # curr_prev = current
        #     sing_result.append(current)
        # elif curr_key not in dup_result:
        #     print("there", current.val, current.next)
        #     sing_result.remove(current)
        #     dup_result.append(current)
        # else:
        #     print("now")
        #     pass
        if current.val == current.next.val: # as this link list is sorted
            while((current and current.next) and (current.val == current.next.val)): # until curr.next.val is larger
                current = current.next
            current = current.next
            curr_prev.next = current
        else: 
            curr_prev = curr_prev.next
            current = current.next
        # current = current.next
    # return A
    return dummy.next
    # for i in range(len(sing_result) - 1):
    #     sing_result[i].next = sing_result[i+1] 
    # return sing_result[0]           
            
# 1->2->3->3->4->4->5
node1= ListNode(1)            
node2= ListNode(2)     
node3= ListNode(3)     
node4= ListNode(3)     
node5= ListNode(4)     
node6= ListNode(4)     
node7= ListNode(5)         
node1.next = node2
node2.next = node3
node3.next = node4 
node4.next = node5
node5.next = node6   
node6.next = node7
tmp = deleteDuplicates(node1)
while tmp != None:
    print(tmp.val)
    tmp = tmp.next

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

# class Solution:
#     # @param A : head node of linked list
#     # @return the head node in the linked list
#     def deleteDuplicates(self, A):
#         self.head = A
#         dummy_node = ListNode(0)
#         dummy_node.next = self.head
#         prev = dummy_node
#         curr = self.head
#         while curr is not None:
#             if curr.next is not None and curr.val == curr.next.val:
#                 while curr.next is not None and curr.val == curr.next.val:
#                     curr = curr.next
#                 prev.next = curr.next
#             else:
#                 prev = prev.next
#             curr = curr.next
#         return dummy_node.next
# /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def deleteDuplicates(A: ListNode): ListNode  = {
#       val temp = new ListNode(0)
#       temp.next = A
#       var prev = temp
#       var current = A
    
#       while (current != null) {
#         while (current.next != null && prev.next.value == current.next.value) {
#           current = current.next
#         }
    
#         if (prev.next == current) prev = prev.next
#         else prev.next = current.next
    
#         current = current.next
#       }
#       temp.next
#     }
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
#  * 
#  * @Output head pointer of list.
#  */
# func deleteDuplicates(A *listNode )  (*listNode) {
#     if A == nil {
#         return nil
#     }
#     var previousValidPointer *listNode
#     var headPointer *listNode
#     suspectPointer := A
#     for suspectPointer != nil {
#         nextPointer := suspectPointer.next
#         for nextPointer != nil {
#             if nextPointer.value != suspectPointer.value {
#                 break
#             }
#             nextPointer = nextPointer.next
#         }
#         if nextPointer == suspectPointer.next {
#             // This means that suspectPointer did not have duplicates.
#             if headPointer != nil {
#                 previousValidPointer.next = suspectPointer
#             } else {
#                 headPointer = suspectPointer
#             }
#             previousValidPointer = suspectPointer
#             previousValidPointer.next = nil
#         }
#         suspectPointer = nextPointer
#     }
#     return headPointer
# }
