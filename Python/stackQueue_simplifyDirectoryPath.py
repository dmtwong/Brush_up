# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 22:18:29 2023

@author: USER
"""

# Problem Description
# Given a string A representing an absolute path for a file (Unix-style).
# Return the string A after simplifying the absolute path.
# In Unix-style file system:
# A period '.' refers to the current directory.
# A double period '..' refers to the directory up a level.
# Any multiple consecutive slashes '//' are treated as a single slash '/'.
# In Simplified Absolute path:
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path doesn't end with trailing slashes '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# The path will not have whitespace characters.

# Problem Constraints
# 1 <= |A| <= 106

# Input Format
# The only argument given is string A.

# Output Format
# Return a string denoting the simplified absolute path for a file (Unix-style).

# Example Input
# Input 1:
A = "/home/"
# Input 2:
A = "/a/./b/../../c/"

# Example Output
# Output 1:
# "/home"
# Output 2:
# "/c"

# class Solution:
# 	# @param A : string
	# @return a strings
# 	def simplifyPath(self, A):
        
def simplifyPath(A):
    stk_list = []
    res_str = "/" 
    n_A = len(A)
    i = 0
    rev_stk = []
    
    while i < n_A:
        # print("now", i)
        dir_cur = ""
        while (i < n_A and A[i] == '/'):
            i += 1
        while (i < n_A and A[i] != '/'):
            dir_cur += A[i]
            i += 1
        # print(dir_cur, stk_list)
        if dir_cur == "..":            
            if len(stk_list):
                stk_list.pop()
            # print(stk_list)
        elif dir_cur == '.':
            continue
        elif len(dir_cur) > 0:
            stk_list.append(dir_cur)
            # print(dir_cur, stk_list)
        i += 1
    # print(stk_list)
    while len(stk_list) > 0:
        temp = stk_list.pop()
        rev_stk.append(temp)
    # print(rev_stk)
    while len(rev_stk) > 0:
        curr = rev_stk[-1]
        if (len(rev_stk) != 1):
            res_str += (curr + "/")
        else:
            res_str += curr
        rev_stk.pop() 
    return res_str

simplifyPath(A)

# class Solution:
#     # @param A : string
#     # @return a strings
#     def simplifyPath(self, A):
#         dirs = A.split('/')
#         result = []
#         for c in dirs:
#             if c == '' or c == '.': continue
#             elif c == '..':
#                 if len(result)>0: result.pop()
#             else:
#                 result.append(c)
#         return '/'+'/'.join(result)

# class Solution {
    
#     def simplifyPath(A: String): String  = {
#         val parts = A.split("\\/").filter(_.nonEmpty).toList
    
#         def simplify(parts: List[String], acc: List[String]):List[String] = parts match {
#           case x::xs => {
#             if (x == ".") simplify(xs, acc)
#             else if (x == ".." && acc.nonEmpty) simplify(xs, acc.tail)
#             else if (x == ".." && acc.isEmpty) simplify(xs, acc)
#             else simplify(xs, x::acc)
#           }
#           case Nil => acc
#         }
    
#         val reversed = simplify(parts, List())
#         if (reversed.isEmpty) "/"
#         else reversed.reverse
#           .foldLeft(new StringBuilder())((acc, s) => acc.append("/").append(s)).toString()

#   }
    
# }

# import "strings"

# func simplifyPath(path string) string {
# 	parts := strings.Split(path, "/")
# 	queue := []string{}
# 	for _, part := range(parts) {
# 		if part == ".." {
# 			if len(queue) > 0 {
# 				queue = queue[:len(queue)-1]
# 			}
# 		} else if (part != "." && part != "") {
# 			queue = append(queue, part)
# 		}
# 	}
# 	return "/" + strings.Join(queue, "/")
# }
            
            
# Editorial


# string Solution::simplifyPath(string path) {
#     vector<string>   nameVect;
#     string name;

#     path.push_back('/');

#     for (int i = 0; i < path.size(); i++) {
#         if (path[i] == '/') {
#             if (name.size() == 0) continue;
#             if (name == "..") {     //special case 1：double dot，pop dir
#                 if (nameVect.size() > 0) nameVect.pop_back();
#             } else if (name == ".") {//special case 2:singel dot，don`t push
#             } else {          
#                 nameVect.push_back(name);
#             }
#             name.clear();
#         } else {
#             name.push_back(path[i]);//record the name
#         }
#     }

#     string result;
#     if (nameVect.empty()) return "/";
#     for (int i = 0; i < nameVect.size(); i++) {
#         result.append("/" + nameVect[i]);
#     }
#     return result;
# }