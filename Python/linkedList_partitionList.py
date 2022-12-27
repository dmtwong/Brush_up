# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:52:28 2022

@author: USER
"""


# Problem Description
#  Given a linked list A and a value B, partition it such that all nodes less than B 
#  come before nodes greater than or equal to B. 
#  You should preserve the original relative order of the nodes in each of the two partitions. 
# Problem Constraints
#  1 <= |A| <= 106 
#  1 <= A[i], B <= 109 

# Input Format
#  The first argument of input contains a pointer to the head to the given linked list. 
#  The second argument of input contains an integer, B. 
# Output Format
#  Return a pointer to the head of the modified linked list. 
# Example Input
 # Input 1: 
A = [1, 4, 3, 2, 5, 2]
B = 3
 # Input 2: 
A = [1, 2, 3, 1, 3]
B = 2
# Example Output
 # Output 1: 
# [1, 2, 2, 4, 3, 5]
 # Output 2: 
# [1, 1, 2, 3, 3]

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
# 	def partition(self, A, B):
	def partition(A, B):
        smaller_head = None
        smaller_last = None
        greater_head = None   
        greater_last = None
        temp = A
        countS = 0
        countL = 0
        countT = 0 
        while (temp != None):
            if (temp.val < B):
                if smaller_head == None:
                    smaller_head = temp
                    smaller_last = temp
                    countS += 1
                    countT += 1
                else:
                    smaller_last.next = temp
                    smaller_last = temp
                    countS += 1
                    countT += 1
            else:
                if greater_head == None:
                    greater_head = temp
                    greater_last = temp
                    countL += 1
                    countT += 1
                else:
                    greater_last.next = temp
                    greater_last = temp          
                    countL += 1
                    countT += 1
            temp = temp.next
        # return smaller_head
        # return greater_head
        if countS == 0:
            # print('here', countL)
            A = greater_head
            if greater_last == None:
                greater_head.next = None
                return A
            else:
                greater_last.next = None
                return A
        if countL == 0:
            # print('there', countS)
            A == smaller_head
            if smaller_last.next == None:
                smaller_head.next = None
                return A
            else:
                smaller_last.next = None
                return A        

        # print(countS, countL)
        A = smaller_head
        smaller_last.next = greater_head
        greater_last.next = None
        return A
node0 = ListNode(6)
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
partition(node0, 3)
temp = node0
while temp.next != None:
    print(temp.val)
    temp = temp.next
    
node0 = ListNode(1)
node1 = ListNode(1)
node0.next = node1
partition(node0, 1)
temp = node0
while temp != None and temp.val != None:
    print(temp.val)
    temp = temp.next


# Editorial:
#     class Solution:
#     # @param {ListNode} head
#     # @param {integer} x
#     # @return {ListNode}
#     def partition(self, head, x):
#         if not head:
#             return None

#         less, greaterEqual = ListNode(0), ListNode(0)
#         tempLess, tempGreaterEqual, temp = less, greaterEqual, head
#         while temp:
#             if temp.val < x:
#                 tempLess.next = temp
#                 tempLess = tempLess.next
#             else:
#                 tempGreaterEqual.next = temp
#                 tempGreaterEqual = tempGreaterEqual.next

#             cur = temp
#             temp = temp.next
#             cur.next = None

#         tempLess.next = greaterEqual.next
#         return less.next
# /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def partition(A: ListNode, B: Int): ListNode = {
#     if (A == null || A.next == null) A
#     else {
#       var less: ListNode = null
#       var moreOrEq: ListNode = null
#       var firstL: ListNode = null
#       var firstM: ListNode = null

#       var n = A
#       while (n != null) {
#         val tmp = n.next
#         if (n.value < B) {
#           if (firstL == null) firstL = new ListNode(n.value)
#           if (less == null) less = firstL
#           else {
#             n.next = null
#             less.next = n
#             less = n
#           }
#         } else {
#           if (firstM == null) firstM = new ListNode(n.value)
#           if (moreOrEq == null) moreOrEq = firstM
#           else {
#             n.next = null
#             moreOrEq.next = n
#             moreOrEq = n
#           }
#         }
#         n = tmp
#       }

#       if (firstL == null) firstM
#       else {
#         less.next = firstM
#         firstL
#       }
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
# ListNode* Solution::partition(ListNode* A, int B) {
#     if (!A) return A;
    
#     ListNode *fake1 = new ListNode(0);
#     ListNode *fake2 = new ListNode(0);
#     fake1->next = A;
    
#     ListNode *p = A, *prev = fake1, *p2 = fake2;
    
#     while (p) {
#         if (p->val < B) {
#             p = p->next;
#             prev = prev->next;
#         } else {
#             p2->next = p;
#             prev->next = p->next;
            
#             p = prev->next;
#             p2 = p2->next;
#         }
#     }
#     p2->next = NULL;
#     prev->next = fake2->next;
    
#     return fake1->next;
#     ListNode *i, *j, *toDelNode;
#     int temp;
#     i = A, j = A;
#     while (i && j && j->next) {
#         if (j->next->val < B) {
#             toDelNode = j->next;
#             j->next = toDelNode->next;
#             toDelNode->next = i;
#             i->next = toDelNode;
#             i = i->next;
#         }
#         if (j) {
#             j = j->next;
#         }
#     }
#     return A;
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
# func partition(list *listNode, x int) (*listNode) {
# 	var smaller, greater *listNode = nil, nil
# 	node := list
# 	var firstSmaller, firstGreater, lastSmaller *listNode = nil, nil, nil
# 	for node != nil {
# 		if node.value < x {
# 			if smaller == nil {
# 				smaller = node
# 				firstSmaller = smaller
# 				lastSmaller = smaller
# 				nextNode := node.next
# 				node.next = nil
# 				node = nextNode
# 			} else {
# 				smaller.next = node
# 				smaller = smaller.next
# 				lastSmaller = smaller
# 				nextNode := node.next
# 				node.next = nil
# 				node = nextNode
# 			}
# 		} else {
# 			if greater == nil {
# 				greater = node
# 				firstGreater = greater
# 				nextNode := node.next
# 				node.next = nil
# 				node = nextNode
# 			} else {
# 				greater.next = node
# 				greater = greater.next
# 				nextNode := node.next
# 				node.next = nil
# 				node = nextNode
# 			}
# 		}
# 	}
# 	if firstSmaller == nil {
# 		return firstGreater
# 	} else {
# 		lastSmaller.next = firstGreater
# 		return firstSmaller
# 	}
# }
