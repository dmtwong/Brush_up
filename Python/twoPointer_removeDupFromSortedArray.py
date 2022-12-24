# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:42:15 2022

@author: mingt
"""

#########################
 
########################
# Problem Description 
# Given a sorted array A consisting of duplicate elements.

# Your task is to remove all the duplicates and return the length of the sorted array 
# of distinct elements consisting of all distinct elements present in A.

# Note: You need to update the elements of array A by removing all the duplicates

# Input Format
# First and only argurment containing the integer array A.

# Output Format
# Return a single integer, as per the problem given.

# Example Input
# Input 1:
A = [1, 1, 2]
# Input 2:
A = [1, 2, 2, 3, 3]
# Example Output
# Output 1:2
# Output 2:3

# Example Explanation
# Explanation 1:

# Updated Array: [1, 2, X] after rearranging. Note that there could be any number in place of x since we dont need it.
# We return 2 here.
# Explanation 2:

# Updated Array: [1, 2, 3, X, X] after rearranging duplicates of 2 and 3.
# We return 3 from here.


# class Solution:
    # @param A : list of integers
    # @return an integer
    # def removeDuplicates(self, A):
def removeDuplicates(A):
    # # A = list(set(A))    
    # # return A
    # n_A = len(A)
    # i, j = 0, 1
        
    # # result = [x for x in range(n_A)]
    # j = 1
    # # result = A[0]
    # for i in range(n_A - 1):
    #     if A[i] == A[i+1]:
    #         pass
    #     else:
    #         # print(A[i], result[i], j)
    #         A[j] = A[i+1]
    #         # result = A[j]
    #         j += 1
    # n_result = len(set(A))
    # return n_result  
    # # if A[-1] != result:
    # #     result = A[-1]
        
    # # result[j] = A[-1]
    # # j += 1
    # # return result
    i = 0
    j = 1
    while (j < len(A)):
        if (A[i] < A[j]):
            # print(i, j, A[i], A[j])
            A[i+1], A[j] = A[j], A[i+1]
            # print(A[i], A[j])
            i += 1
        j += 1
        
    while(j-1 > i):
        A.pop()
        j-=1
        
    return len(A)

# Suggested Solution:
# import sys
# from ctypes import *
# from ctypes.util import find_library
# from solution import *
# import queue

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# #OK
# def input_linked_list(libc):
#     inputSize = c_int()
#     libc.scanf(b"%d", byref(inputSize))
#     inputSize = inputSize.value
#     if inputSize == 0:
#         return None
#     val = c_int()
#     libc.scanf(b"%d", byref(val))
#     root = ListNode(val.value)
#     inputSize -= 1
#     prev = root
#     while inputSize > 0:
#         inputSize -= 1
#         libc.scanf(b"%d", byref(val))
#         newNode = ListNode(val.value)
#         prev.next = newNode
#         prev = newNode
#     return root

# #OK
# def print_linked_list(node):
#     sz = 1200000
#     while node is not None:
#         sz -= 1
#         if sz <= 0:
#             break
#         if node.next is not None:
#             sys.stdout.write("%s -> " % node.val)
#         else:
#             sys.stdout.write("%s " % node.val)
#         node = node.next
#     print ('')

# #OK
# def preorder(node):
#     if node is None:
#         return
#     sys.stdout.write("%s " % node.val)
#     preorder(node.left)
#     preorder(node.right)

# #OK
# def postorder(node):
#     if node is None:
#         return
#     postorder(node.left)
#     postorder(node.right)
#     sys.stdout.write("%s " % node.val)

# #OK
# def print_tree(node):
#     sys.stdout.write("Returned tree's PreOrder traversal : [ ")
#     preorder(node)
#     sys.stdout.write("] ## ")
#     sys.stdout.write("Returned tree's PostOrder traversal : [ ")
#     postorder(node);
#     print("]")

# #OK
# def input_tree(libc):
#     inputSize = c_int()
#     libc.scanf(b"%d", byref(inputSize))
#     inputSize = inputSize.value
#     if inputSize == 0:
#         return None
#     val = c_int()
#     left = c_int()
#     right = c_int()
#     libc.scanf(b"%d", byref(val))
#     q = queue.Queue()
#     root = TreeNode(val.value)
#     q.put(root)
#     while not q.empty():
#         x = q.get()
#         libc.scanf(b"%d%d", byref(left), byref(right))
#         leftVal = left.value
#         rightVal = right.value
#         if leftVal != -1:
#             leftNode = TreeNode(leftVal)
#             x.left = leftNode
#             q.put(leftNode)
#         if rightVal != -1:
#             rightNode = TreeNode(rightVal)
#             x.right = rightNode
#             q.put(rightNode)
#     return root

# #OK
# def input_list_int(libc):
#     inputSize = c_int()
#     ele = c_int()
#     libc.scanf(b"%d", byref(inputSize))
#     l = []
#     inputSize = inputSize.value
#     while inputSize > 0:
#         inputSize = inputSize - 1
#         libc.scanf(b"%d", byref(ele))
#         l.append(ele.value)
#     return l

# #OK
# def input_list_char(libc):
#     inputSize = c_int()
#     ele = c_char()
#     libc.scanf(b"%d", byref(inputSize))
#     l = []
#     inputSize = inputSize.value
#     while inputSize > 0:
#         inputSize = inputSize - 1
#         libc.scanf(b" %c", byref(ele))
#         l.append(ele.value.decode("utf-8"))
#     return l

# #OK
# def input_string(libc):
#     A = create_string_buffer(1000005)
#     libc.gets(byref(A))
#     A=A.value
#     A=A.decode("utf-8")
#     return A

# #OK
# def input_list_string(libc):
#     inputSize = c_int()
#     ele = create_string_buffer(1000005)
#     libc.scanf(b"%d", byref(inputSize))
#     l = []
#     inputSize = inputSize.value
#     while inputSize > 0:
#         inputSize = inputSize - 1
#         libc.scanf(b"%s", byref(ele))
#         l.append(ele.value.decode("utf-8"))
#     return l

# #OK
# def input_list_list_int(libc):
#     rowSize = c_int()
#     colSize = c_int()
#     ele = c_int()
#     libc.scanf(b"%d%d", byref(rowSize), byref(colSize))
#     l = []
#     rowSize = rowSize.value
#     colSize = colSize.value
#     while rowSize > 0:
#         rowSize -= 1
#         newL = []
#         tmpCol = colSize
#         while colSize > 0:
#             colSize -= 1
#             libc.scanf(b"%d", byref(ele))
#             newL.append(ele.value)
#         colSize = tmpCol
#         l.append(newL)
#     return l

# #OK
# def print_list(l):
#     for i in l:
#         sys.stdout.write("%s " % i)
#     print('')

# #OK
# def print_list_list(l, toSort):
#     if toSort:
#         l.sort()
#     for newL in l:
#         sys.stdout.write('[')
#         for i in newL:
#             sys.stdout.write("%s " % i)
#         sys.stdout.write('] ')
#     print('')

# if __name__ == "__main__":
#     library = find_library("c")
#     cdll.LoadLibrary(library)
#     libc = CDLL(library)

#     testcases = c_int()
#     libc.scanf(b"%d\n", byref(testcases))
#     testcases = testcases.value

#     while testcases > 0:
#         testcases -= 1
#         obj = Solution()
        

#         A = input_list_int(libc)
#         libc.scanf(b"\n")
#         print (obj.solve(A))
#         for i in A:
#     	    if cnt <= 0:
#     		    break
#     	    cnt -= 1
#     		sys.stdout.write("%s " % i)

# 	    print ""
#         sys.stdout.flush()

# C++:
    
# Editorial


# int Solution::removeDuplicates(vector<int> &A) {
#     assert(A.size() >= 1 && A.size() <= 1e6);
#     int count = 0, n = A.size();
# 	for (int i = 0; i < n; i++) { 
# 	    assert(A[i] >= 0 && A[i] <= 2e9);
# 		if (i < n - 1 && A[i] == A[i+1]) continue;
# 		else {
# 			A[count] = A[i];
# 			count++;
# 		}
# 	}
# 	return count;
# }

# Java:
# public class Solution {
# 	public int removeDuplicates(ArrayList<Integer> A) {
# 	    int index = 1;
# 	    int n = A.size();
# 	    
# 	    if (A == null || A.size() == 0)
# 	        return 0;
# 	    
# 	    for (int i = 1; i < n; i++) {
# 	        
# 	        if (A.get(i).intValue() != A.get(i - 1).intValue()) {
# 	            int temp = A.get(index);
# 	            A.set(index, A.get(i));
# 	            index++;
# 	        }
# 	    }
# 	    
# 	    return index;
# 	    
# 	}
# }