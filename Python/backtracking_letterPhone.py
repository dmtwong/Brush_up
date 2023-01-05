# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:56:27 2023

@author: USER
"""


# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# The digit 0 maps to 0 itself.

# The digit 1 maps to 1 itself.

# Input: Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Make sure the returned strings are lexicographically sorted.

# class Solution:
	# @param A : string
	# @return a list of strings
# 	def letterCombinations(self, A):
def letterCombinations(A):      
    import collections
    n_A = len(A)
    A = [int(x) for x in A]
    digitDict  = collections.OrderedDict()
    digitDict[0] = "0"
    digitDict[1] = "1"
    digitDict[2] = "abc"
    digitDict[3] = "def"
    digitDict[4] = "ghi"
    digitDict[5] = "jkl"
    digitDict[6] = "mno"
    digitDict[7] = "pqrs"
    digitDict[8] = "tuv"
    digitDict[9] = "wxyz"
    # key_digitDict = list(digitDict.keys())
    # val_digitDict = list(digitDict.values())
    
    result = []
    temp = collections.deque()
    temp.append("")
    # print(temp) 
    while len(temp) != 0:
        success = temp.pop()
        # print(success)
        if len(success) == n_A:
            result.append(success)
            # print('here', result)
        else:
            for letter in digitDict[A[len(success)]]:
                # print('there', letter)
                temp.append(success + letter)     
                # print(temp)
    
    result.sort()
    return(result)
    
 
 

A = "2"
A = "23"
letterCombinations(A)

### Editorial
# class Solution:
#     # @param A : string
#     # @return a list of strings
#     def letterCombinations(self, digits):
#         mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
#                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': '0', '1': '1'}
#         if len(digits) == 0:
#             return []
#         if len(digits) == 1:
#             return list(mapping[digits[0]])
#         prev = self.letterCombinations(digits[:-1])
#         additional = mapping[digits[-1]]
#         return [s + c for s in prev for c in additional]

# Scala:
#     class Solution {

#     def letterCombinations(digits: String): Array[String]  = {
#         val letter_mapping = Map(                                                                                                                               
#           '0' -> "0",                                                                                                                                           
#           '1' -> "1",                                                                                                                                           
#           '2' -> "abc",                                                                                                                                         
#           '3' -> "def",                                                                                                                                         
#           '4' -> "ghi",                                                                                                                                         
#           '5' -> "jkl",                                                                                                                                         
#           '6' -> "mno",                                                                                                                                         
#           '7' -> "pqrs",                                                                                                                                        
#           '8' -> "tuv",                                                                                                                                         
#           '9' -> "wxyz"                                                                                                                                        
#          )  
    
#         def letterCombinationHelper(depth: Int, prefix: String=""): Array[String] = {                                                                           
#           if (depth == digits.length)                                                                                                                           
#             Array(prefix)                                                                                                                                       
#           else                                                                                                                                                  
#             letter_mapping(digits(depth)).foldLeft(Array.empty[String]) {                                                                                       
#               (results, x) => results ++ letterCombinationHelper(depth+1, prefix :+ x)                                                                          
#             }                                                                                                                                                   
#         }
        
#         if (digits.length == 0)
#             Array.empty[String]
#         else
#             letterCombinationHelper(0)
#     }
# }
# void recur(string A,int x,string s, vector<string>& res);

# vector<string> Solution::letterCombinations(string A) {
#     vector<string> res;
#     string s;
#     recur(A,0,s,res);
#     sort(res.begin(),res.end());
#     for (int i = 0; i < res.size(); ++i) {
#         res[i].pop_back();
#     }
#     return res;
# }
# void recur(string A,int x,string s, vector<string>& res){
#     string s1;
#     if(x>A.size()){
#         res.push_back(s);
#         return ;
#     }
#     switch(A[x]-48){
#         case 0 :
#             s1="0";
#             break;
#         case 1 :
#             s1="1";
#             break;
#         case 2 :
#             s1="abc";
#             break;
#         case 3 :
#             s1="def";
#             break;
#         case 4 : 
#             s1="ghi";
#             break;
#         case 5 :
#             s1="jkl";
#             break;
#         case 6 : 
#             s1="mno";
#             break;
#         case 7 :
#             s1="pqrs";
#             break;
#         case 8 :
#             s1="tuv";
#             break;
#         case 9 :
#             s1="wxyz";
#             break;
#     }
# //    cout<<s1;
#     s.push_back(s1[0]);
#     recur(A,x+1,s,res);
#     s.pop_back();
#     if(s1.length()>1){
#         s.push_back(s1[1]);
#         recur(A,x+1,s,res);
#         s.pop_back();;
#         s.push_back(s1[2]);
#         recur(A,x+1,s,res);
#         s.pop_back();
#     }
#     if(s1.length()==4){
#         s.push_back(s1[3]);
#         recur(A,x+1,s,res);
#         s.pop_back();
#     }
# }
#     /**
#  * @input A : String
#  * 
#  * @Output string array.
#  */
# var sol []string
# var str string
# func letterCombinations(A string )  ([]string) {
#     sol=make([]string, 0)
#     str=A
#     comb(0, "")
#     return sol
# }
# func digitToLetters(c rune) []string {
#     switch c {
#         case '0':
#             return []string{"0"}
#         case '1':
#             return []string{"1"}
#         case '2':
#             return []string{"a", "b", "c"}
#         case '3':
#             return []string{"d", "e", "f"}
#         case '4':
#             return []string{"g", "h", "i"}
#         case '5':
#             return []string{"j", "k", "l"}
#         case '6':
#             return []string{"m", "n", "o"}
#         case '7':
#             return []string{"p", "q", "r", "s"}
#         case '8':
#             return []string{"t", "u", "v"}
#         case '9':
#             return []string{"w", "x", "y", "z"}
#     }
#     return []string{}
# }    
# func comb(i int, res string) {
#     if i==len(str) {
#         sol=append(sol, res)
#         return
#     }
#     lettersArray:= digitToLetters(rune(str[i]))
#     for _, a := range lettersArray {
#         res1:=res+a
#         comb(i+1, res1)
#     }
# }