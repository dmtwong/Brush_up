# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:38:08 2022

@author: USER
"""
# Problem Description
# Given a linked list A of length N and an integer B.
# You need to reverse every alternate B nodes in the linked list A.

# Problem Constraints
# 1 <= N <= 105
# 1<= Value in Each Link List Node <= 103
# 1 <= B <= N
# N is divisible by B

# Input Format
# First argument is the head pointer of the linkedlist A.

# Second argument is an integer B.
# Output Format
# Return the head pointer of the final linkedlist as described.

# Example Input
# Input 1:

 A = 3 -> 4 -> 7 -> 5 -> 6 -> 6 -> 15 -> 61 -> 16
 B = 3
 # Input 2:

 A = 1 -> 4 -> 6 -> 6 -> 4 -> 10
 B = 2


# Example Output
# Output 1:

#  7 -> 4 -> 3 -> 5 -> 6 -> 6 -> 16 -> 61 -> 15
# Output 2:

#  4 -> 1 -> 6 -> 6 -> 10 -> 4
 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.following = None

# class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    # def solve(self, A, B):
def solve(A, B):
    if (not A) or (B == 1):
        return A
    curr = A
    ix = 0    
    prev = temp = tail = result = join = None
    
    while (curr != None) :     
        ix = B
        join = curr
        prev = None
        while (curr != None and ix > 0):             
            ix -= 1
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp         
        if (result == None):
            result = prev    
        if (tail != None):
            tail.next = prev    
        tail = join
        tail.next = curr
        ix = B
        while (curr != None and ix > 0):
            ix -= 1
            prev = curr
            curr = curr.next
        tail = prev
    return result
    # temp = A
    # temp = ListNode(None)
    # temp.next = A
    # curr = temp 
    # following = temp 
    # last = temp
    # count_len, block_size = 0, 0
 
    # while curr != None:
    #     curr = curr.next
    #     count_len += 1
    
    # isRev = True
    # while following:
    #     # print('here', following.val)
    #     block_size = (count_len > B and B) or (count_len - 1) 
    #     if (isRev):
    #         curr = last.next
    #         following = curr.next
    #         for i in range(1, block_size):
    #             # print('there', i, curr.next, following.next, last.next)
    #             curr.next = following.next
    #             following.next = last.next
    #             last.next = following
    #             following = curr.next
    #             # print('there', i, curr.next, following.next, last.next)
    #         last = curr
    #         count_len -= B
    #     else:
    #         for i in range(1, block_size):
    #             # print('there', i, curr.next, following.next, last.next)

    #     isRev = not(isRev)
    
    # return temp.next
        

Node1 = ListNode(4) 
Node2 = ListNode(1) 
Node3 = ListNode(6)
Node4 = ListNode(6)
Node5 = ListNode(10)
Node6 = ListNode(4)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
temp = solve(Node1, 2)
temp.val
temp.next.val
temp.next.next.val
temp.next.next.next.next.val


# Editorial:
#     # Definition for singly-linked list.
# # class ListNode:
# #    def __init__(self, x):
# #        self.val = x
# #        self.next = None
# def kAltReverse(head, k) :  
#     current = head  
#     next = None
#     prev = None
#     count = 0
  
#     #1) reverse first k nodes of the linked list  
#     while (current != None and count < k) :  
#         next = current.next
#         current.next = prev  
#         prev = current  
#         current = next
#         count = count + 1; 
      
#     # 2) Now head pos to the kth node.  
#     # So change next of head to (k+1)th node 
#     if(head != None):  
#         head.next = current  
  
#     # 3) We do not want to reverse next k  
#     # nodes. So move the current  
#     # poer to skip next k nodes  
#     count = 0
#     while(count < k - 1 and current != None ):  
#         current = current.next
#         count = count + 1
      
#     # 4) Recursively call for the list  
#     # starting from current.next. And make 
#     # rest of the list as next of first node  
#     if(current != None):  
#         current.next = kAltReverse(current.next, k)  
  
#     # 5) prev is new head of the input list  
#     return prev  
# class Solution:
#     # @param A : head node of linked list
#     # @param B : integer
#     # @return the head node in the linked list
#     def solve(self, A, B):
#         return kAltReverse(A,B);

# GO:
# **
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
 
 
 
# func solve(root *listNode , B int )  (*listNode) {
#     if root == nil {
#         return root
#     }

#     count := 0
#     var prev *listNode = nil
#     var current *listNode = root
#     var next *listNode = nil
#     for current != nil && count < B {
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#         count++
#     }
#     //root is at kth node & current is k+1 nodes
#     if root != nil  {
#         root.next = current;  
#     }
    
#     count = 0;  
#     for(count < B-1 && current != nil ){  
#         current = current.next;  
#         count++;  
#     }  
    
#     /*next is now k+1th node and head is the kth node*/
#     if current != nil {
#         current.next = solve(current.next, B)
#     }

#     return prev


# }
# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
# ListNode* Solution::solve(ListNode* A, int B) {
#      vector<int> store;
#     while(A)
#     {
#         store.push_back(A->val); A= A->next;
#     }
#     int i ;
#     for(i = 0; i + B< store.size(); i= i+ 2*B )
#     {
#         reverse(store.begin() + i, store.begin() + i + B);
#     }
#         reverse(store.begin() + i, store.end());
#     ListNode* result = NULL;
    
#     for(int i = store.size()-1; i>= 0; i--)
#     {
#         ListNode* Node = (ListNode*) malloc(sizeof(ListNode));
#         Node->val = store[i];
#         Node->next= result;
#         result = Node;
#     }
#     return result;
# }
