# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:52:28 2022

@author: USER
"""

# somehow not pass the corner case A : [ 1 ] B : 1

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
        temp = A.next
        countS = 0
        countL = 0
        while (temp != None):
            if (temp.val < B):
                if smaller_head == None:
                    smaller_head = temp
                    smaller_last = temp
                    countS += 1
                else:
                    smaller_last.next = temp
                    smaller_last = temp
                    countS += 1
            else:
                if greater_head == None:
                    greater_head = temp
                    greater_last = temp
                    countL += 1
                else:
                    greater_last.next = temp
                    greater_last = temp          
                    countL += 1
            temp = temp.next
        if countS == 0:
            # print('here', countL)
            A.next = greater_head
            if greater_last == None:
                greater_head.next = None
                return A
            else:
                greater_last.next = None
                return A
        if countL == 0:
            # print('there', countS)
            A.next == smaller_head
            if smaller_last.next == None:
                smaller_head.next = None
                return A
            else:
                smaller_last.next = None
                return A
        # print(countS, countL)
        A.next = smaller_head
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


