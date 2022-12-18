# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:18:11 2022

@author: USER
"""


# Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting 
# if its a palindrome or not, respectively.

# Notes:

# Expected solution is linear in time and constant in space.
# For example,
# List 1-->2-->1 is a palindrome.
# List 1-->2-->3 is not a palindrome.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# class Solution:
# 	# @param A : head node of linked list
# 	# @return an integer
# 	def lPalin(self, A):
	def lPalin(A):
        import copy
        def getVal(A):
            temp = None
            if A.val != None:
                temp = A.val
                A = A.next
            return temp
        # cur_node = copy.deepcopy(A)
        cur_val = A.val
        list_val = []
        while A != None:
            # print(id(A))
            cur_val = getVal(A)
            # print(cur_val)
            if(cur_val != None):
                list_val.append(cur_val)
            A = A.next
        n_A = len(list_val)
        i, j = 0, n_A - 1
        sofarPal = True
        # print(list_val)
        while(sofarPal and (i < j)):
            # print(i, j)            
            if list_val[i] == list_val[j]:
                i += 1
                j -= 1
            else:
                sofarPal = False
        return int(sofarPal)


# node_1a = ListNode(1)    #2371143182464
# id(node_1a)
# id(node_1b)
# id(node_1c)
# node_1b = ListNode(2) #2371143182992
# node_1c = ListNode(1) #2371143182560
# node_1a.next = node_1b
# node_1b.next = node_1c
#     # node_1a
lPalin(node_1a)



# Suggeseted Solution:
#     class Solution:
#     # @param A : head node of linked list
#     # @return an integer
#     def lPalin(self, A):
#         lenL = 0
#         head = thead = thead2 =A
        
#         # Find length of the linked list
#         while head is not None:
#             head = head.next
#             lenL += 1
        
#         # Reverse right half of the linked list
#         i = 0
#         prev = None
#         nextNode = thead.next
#         while thead is not None:
#             nextNode = thead.next
#             if i >= (lenL // 2):
#                 thead.next = prev
#             prev = thead
#             thead = nextNode
#             i += 1

#         # Check left and right part of the linked list
#         j = 0
#         while j <= (lenL // 2) and thead2 is not None:
#             if thead2.val != prev.val:
#                 return 0
#             thead2 = thead2.next
#             prev = prev.next
#             j += 1
        
#         return 1
    
#     /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def lPalin(A: ListNode): Int  = {
#         import scala.collection.mutable.ArrayBuffer

#     var len = 0
#     var n = A
#     while (n != null) {
#       len += 1
#       n = n.next
#     }

#     val fh = (len / 2) - 1
#     val sh = len - 1 - fh

#     n = A
#     var i  = 0
#     val secHalf: ArrayBuffer[Int] = ArrayBuffer()
#     while (n != null) {
#       if (i >= sh) secHalf += n.value
#       i += 1
#       n = n.next
#     }

#     var res = 1
#     n = A
#     for (i <- secHalf.length - 1 to 0 by - 1 if res == 1) {
#       if (secHalf(i) != n.value) res = 0
#       else n = n.next
#     }

#     res
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
# ListNode*reverse(ListNode*head)
# {
#     ListNode*prev=NULL;
#     ListNode*curr=head;
#     ListNode*n;
#     while(curr!=NULL)
#     {
#         n = curr->next;
#         curr->next = prev;
#         prev = curr;
#         curr = n;
#     }
#     return prev;
# }
# int Solution::lPalin(ListNode* A) {
#     ListNode*slow = A;
#     ListNode*fast = A;
#     if(A==NULL || A->next==NULL) return 1;  // returning true if num of nodes are 0 or 1
#     if(A->next->next==NULL)
#     {
#         if(A->val == A->next->val) return 1;  //if num of nodes are 2 checking palindrom or not
#         else return 0;
#     }
#     while(fast->next!=NULL && fast->next->next!=NULL) //finding middile node of linkedlist
#     {
#         slow = slow->next;
#         fast = fast->next->next;   
#     }
#     ListNode*temp = reverse(slow->next); //reversing linked list after midpoint
#     while(A!=NULL && temp!=NULL)
#     {   
#         if(A->val != temp->val) return 0;  
#         A = A->next;
#         temp=temp->next;
#     }
#     return 1;
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
#  * @Output Integer
#  */
 
#  //Compare twoLists
# func compareTwoLists(first, second *listNode) int {
#     temp1 := first
#     temp2 := second
#     for temp1 != nil && temp2 != nil {
#         if temp1.value == temp2.value {
#             temp1 = temp1.next
#             temp2 = temp2.next
#         } else {
#             return 0
#         }
#     }

#     if temp1 == nil && temp2 == nil {
#         return 1
#     }

#     return 0
# }

# /* Helper Function to Reverse LinkedList */
# func Reverse(root *listNode) *listNode {
#     if root == nil || root.next == nil {
#         return root
#     }
#     // Reach till end of list and start recursion
#     rest := Reverse(root.next)
#     root.next.next = root
#     root.next = nil
#     return rest
# }

# func lPalin(root *listNode )  (int) {
#     var first, second *listNode
#     fast := root
#     slow := root
#     var middleNode *listNode

#     var prev *listNode
#     if root == nil || root.next == nil{
#         return 1
#     }
#     for fast != nil && fast.next != nil {
#         fast = fast.next.next
#         prev = slow
#         slow = slow.next

#     }

#     //In case of even, fast will be non nil. 
#     if fast != nil {
#         middleNode = slow
#         second = slow.next
#         prev.next = nil
#     } else {
#         second = slow
#         prev.next = nil
#     }

#     first = root
#     secondreversed := Reverse(second)
#     result := compareTwoLists(first, secondreversed)
#     second = Reverse(secondreversed)


#     // Recreate the list
#     if middleNode != nil {
#         prev.next = middleNode
#         middleNode.next = second
#     } else {
#         prev.next = second
#     }

#     return result

# }
