# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:44:49 2023

@author: USER
"""

# Problem Description
# You are given a string A which is a serialized string. You have to restore the original array of strings.
# The string in the output array should only have lowercase english alphabets.
# Serialization: Scan each element in a string, calculate its length and append it with a string and a element separator or deliminator (the deliminator is ~). We append the length of the string so that we know the length of each element.
# For example, for a string 'interviewbit', its serialized version would be 'interviewbit12~'.

# Problem Constraints
# 1 <= |A| <= 106

# Input Format
# The first argument is the string A.
# Output Format
# Return an array of strings which are deserialized.

# Example Input
# Input 1:
A = 'scaler6~academy7~'
# Input 2:
A = 'interviewbit12~'


# Example Output
# Output 1:
# ['scaler', 'academy']
# Output 2:

# ['interviewbit']
# Example Explanation
# Explanation 1:
# Length of 'scaler' is 6 and academy is 7. So, the resulting string is scaler6~academy7~.
# We hve to reverse the process.
# Explanation 2:

# Explained in the description above.

# class Solution:
    # @param A : string
    # @return a list of strings
    # def deserialize(self, A):
        
# def serialize(A):
#     n_A = len(A)
#     result = ""
#     for i in range(n_A):
#         n_curr_i = len(A[i])
#         # result = result + "~" + A[i] + str(n_curr_i)
#         result = result + A[i] + str(n_curr_i) + "~"
#     # n_result = len(result)
#     # return result[1:]
#     return result
# serialize(A)

def deserialize(A):
    import string
    # n_A = len(A)
    result = []
    counter = 0
    lower_chars = string.ascii_lowercase
    # for i in range(n_A):
    # ix = 0
    while (counter > -1):
        counter = A.find("~")
        # print(counter)
        curr_ele = ''
        # for i in range(ix, ix + counter):
        for i in range(counter):
            if A[i] in lower_chars:
                curr_ele = curr_ele + A[i]
                # ix += 1                 
        # print(curr_ele)
        result.append(curr_ele)
        try: 
            A = A[counter+1:]
        except:
            break
    n_result = len(result)
    return(result[:n_result-1])  
                
deserialize(A)        


# Editorial:
#     class Solution:
#     # @param A : string
#     # @return a list of strings
#     def deserialize(self, A):
#         i=j=0
#         ans=[]
#         while (j<len(A)):
#             if ("a"<=A[j]<="z"):
#                 j+=1
#                 continue
#             ans.append(A[i:j])
#             while (j<len(A)):
#                 if ("a"<=A[j]<="z"):
#                     i=j
#                     break
#                 j+=1
#         return ans
    
    
#     vector<string> Solution::deserialize(string A) {
#     vector<string> ans;
#     int i = -1;
#     int j = 0;
#     while(j < A.size()){
#         while(A[j] <= 122 && A[j] >= 97){
#             j++;
#         }
#         ans.push_back(A.substr(i + 1, j - i - 1));
#         while(j < A.size() && A[j] != '~'){
#             j++;
#         }
#         i = j++;
#     }   
#     return ans;
# }
    
#     /**
#  * @input A : String
#  * 
#  * @Output string array.
#  */
# func deserialize(A string )  ([]string) {
#     words := make([]string,0)
#     word := ""
#     first := true
#     for i:=0; i<len(A); i++ {
#         if (A[i] < 97 || A[i]> 122){
#             if first == true {
#                 words = append(words, word)
#                 first = false
#             }
#             word = ""
#             continue;
#         }
#         first = true
#         word += string(A[i])
#     }
#     return words
# }


