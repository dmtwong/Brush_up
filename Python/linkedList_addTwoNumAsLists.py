# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:12:31 2022

@author: USER
"""

# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain
 # a single digit. 
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

# Output: 7 -> 0 -> 8

#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list

# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
# 	def addTwoNumbers(self, A, B):
def addTwoNumbers(A, B):
    temp_i = A
    temp_j = B
    result = 0
    # power = 0
    list_A = []    
    list_B = []
    while (temp_i != None and temp_j != None):
        # if power == 0:
        #     result *= 10**power
        #     power += 1
        # result += temp_i.val
        # result += temp_j.val
        list_A.append(str(temp_i.val))
        list_B.append(str(temp_j.val))
        temp_i = temp_i.next
        temp_j = temp_j.next
        # print('here', result)

    while (temp_i != None):
        # result += temp_i.val
        list_A.append(str(temp_i.val))
        list_B.append(str(0))
        # result *= 10
        temp_i = temp_i.next
        # print('there', result)
    while (temp_j != None):
        # result += temp_j.val
        list_A.append(str(0))
        list_B.append(str(temp_j.val))
        # result *= 10
        temp_j = temp_j.next
    # result *= 10    
    # print(int(''.join(list_A[::-1])))
    # print(int(''.join(list_B[::-1])))
    result = int(''.join(list_A[::-1])) + int(''.join(list_B[::-1]))
    # print(result)      
    str_result = str(result)[::-1]
    # print('abc')
    # 
    # ans_start = ListNode(int(str_result[0]))
    # ans_process = None
    # count_process = 0
    # ans_process_end = None
    # for i in range(1, len(str_result)):
    #     temp = ListNode(int(str_result[i]))
    #     if ans_start.next == None:
    #         ans_process = temp
    #         ans_start.next = temp
    #         count_process += 1
    #     else:
    #         ans_process_end = temp
    #         ans_process_end.next = temp
    # ans_start.next = ans_process
    # if ans_process_end != None:
    #     ans_process_end = None     
    # return ans_start
    
    node_result = []
    for i in range(len(str_result)):
        # print(i)
        temp = ListNode(int(str_result[i]))
        node_result.append(temp)
    # print(len(node_result))
    # print([lambda x: x.val for x in node_result])
        # print(temp.val)
    #     if ans_process == None:
    #     elif ans_process == None:
    #         ans_process_end.next = temp
    #         ans_process_end = temp
    #     # print(ans_head.next.val, ans_process.val, ans_process.next.val)
    # temp = ans_process
    # ans_process_end.next = None
    # return ans_process            
    for i in range(len(node_result) - 1):
        # print(i, node_result[i].val)
        node_result[i].next = node_result[i+1]
    return node_result[0]
        
    

# A : [ 9 -> 9 -> 1 ]
# B : [ 1 ]
# The expected return value: 
# 0 -> 0 -> 2 
A1 = ListNode(9)
A2 = ListNode(9)
A3 = ListNode(1)
B1 = ListNode(1)
A1.next = A2
A2.next = A3
A = A1
B = B1 
addTwoNumbers(A, B)


A1 = ListNode(2)
A2 = ListNode(4)
A3 = ListNode(3)
B1 = ListNode(5)
B2 = ListNode(6)
B3 = ListNode(4)


A1.next = A2
A2.next = A3
B1.next = B2
B2.next = B3
A = A1
B = B1 
addTwoNumbers(A, B)

# Editorial:
# # Definition for singly-linked list.
# # class ListNode:
# #    def __init__(self, x):
# #        self.val = x
# #        self.next = None

# class Solution:
#     # @param A : head node of linked list
#     # @param B : head node of linked list
#     # @return the head node in the linked list
#     def addTwoNumbers(self, A, B):
#         n = m = 0 # Length of A, B

#         current = A
#         while current:
#             n += 1
#             current = current.next
    
#         current = B
#         while current:
#             m += 1
#             current = current.next
    
#         if m > n: # A always contain the longest list
#             current = A
#             A = B
#             B = current
    
#         temp1 = A
#         temp2 = B
#         carry = 0
#         while temp1 and temp2: # Run loop untill smaller list
#             value = (temp1.val+temp2.val+carry)%10
#             carry = (temp1.val+temp2.val+carry)//10
#             temp1.val = value
#             current = temp1
#             temp1 = temp1.next
#             temp2 = temp2.next
    
#         while temp1: # Run loop untill longer one
#             if carry:
#                 value = temp1.val
#                 temp1.val = (value+carry)%10
#                 carry = (value+carry)//10
#             current = temp1
#             temp1 = temp1.next

#         if carry: # If after addition complete, carry left?
#             node = ListNode(carry)
#             current.next = node
    
#         return A
    
# /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def addTwoNumbers(A: ListNode, B: ListNode): ListNode  = {
#       var res = new ListNode(0)
#       val ret = res
#       var node1 = A
#       var node2 = B
#       var rem = 0
#       while (node1 != null || node2 != null) {
#         val aa = if (node1 == null) 0 else node1.value
#         val bb = if (node2 == null) 0 else node2.value
#         var sum = aa + bb + rem
#         if (sum >= 10) {
#           sum = sum - 10
#           rem = 1
#         } else {
#           rem = 0
#         }
    
#         if (node1 != null) node1 = node1.next
#         if (node2 != null) node2 = node2.next
    
#         val over = node1 == null && node2 == null
#         if (over) {
#           res.value = sum
#           if(rem > 0) {
#             res.next = new ListNode(rem)
#           }
#         } else {
#           res.value = sum
#           res.next = new ListNode(0)
#           res = res.next
#         }
#       }
#       ret
#     }
# }  
# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
# ListNode* Solution::addTwoNumbers(ListNode* A, ListNode* B) {
#     int carry = 0, temp;
#     ListNode* ret = NULL, *tempNode = NULL, *prev = NULL;
#     assert(A!= NULL || B != NULL);
#     /*
#     if (!A) {
#         return B;
#     }
#     if (!B) {
#         return A;
#     }
#     */
#     ListNode *tmp = A;
#     tmp = tmp -> next;
    
#     while(tmp!= NULL){
#         if(tmp->next == NULL)
#             assert(tmp->val != 0);
#         tmp = tmp -> next;    
#     }
    
#     tmp = B;
#     tmp = tmp -> next;
    
#     while(tmp!= NULL){
#         if(tmp->next == NULL)
#             assert(tmp->val != 0);
#         tmp = tmp -> next;    
#     }
    
#     while(A || B) {
#         temp = carry + (A?A->val:0) + (B?B->val:0);
#         carry = temp/10;
#         temp = temp%10;
#         tempNode = new ListNode(temp);
        
#         if (ret) {
#             prev->next = tempNode;
#         } else {
#             ret = tempNode;
#         }
#         prev = tempNode;
#         if (A) A = A->next;
#         if (B) B = B->next;
#     }
#     if (carry > 0) {
#         tempNode->next = new ListNode(carry);
#     }
#     return ret;
    
# }
            
# func addTwoNumbers(a, b *listNode) *listNode {
# 	if a == nil || b == nil {
# 		return nil
# 	}
# 	current := &listNode{}
# 	head := current
# 	rem := 0
# 	for a != nil || b != nil {
# 		data := rem
# 		if a != nil {
# 			data += a.value
# 			a = a.next
# 		}
# 		if b != nil {
# 			data += b.value
# 			b = b.next
# 		}
# 		if data > 9 {
# 			rem = 1
# 			data %= 10
# 		} else {
# 			rem = 0
# 		}
# 		current.next = &listNode{
# 			value: data,
# 		}
# 		current = current.next
# 	}

# 	if rem > 0 {
# 		current.next = &listNode{
# 			value: rem,
# 		}
# 	}

# 	return head.next
# }