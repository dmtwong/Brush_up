# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:48:00 2023

@author: USER
"""

# Problem Description 

# Given a list of non-negative integers, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.

# Problem Constraints
# 1 <= |A| <= 105
# 1 <= Ai <= 109

# Input Format
# The first argument is an integer array A.

# Output Format
# Return a string representing the largest number formed

# Example Input
A = [3, 30, 34, 5, 9]

# Example Output
# 9534330

# Example Explanation
# Largest possible number that can be formed is 9534330
# class Solution:
    # @param A : tuple of integers
    # @return a strings
  A = [123, 213, 111]
  # order_A(123,213)
   # order_A(123,111)
  # order_A(123,1234)
  # order_A(223,224)
  # help(list.sort)
 # A.sort(key = order_A)
def largestNumber(A):
    from functools import cmp_to_key
    A = list(A) # test case use is tuple somehow
    def order_A(ele_1, ele_2):
        len_1, len_2 = 0, 0
        temp_1, temp_2 = ele_1, ele_2
        list_1, list_2 = [], []
        while temp_1 > 0:
            len_1 += 1
            list_1.insert(0, temp_1 % 10)
            temp_1 //= 10
        while temp_2 > 0:
            len_2 += 1
            list_2.insert(0, temp_2 % 10)
            temp_2 //= 10    
        # print(list_1, list_2)
        min_len = min(len_1, len_2)
        ix = 0
        while (min_len != 0):
            if list_1[ix] > list_2[ix]:
                return 1
            elif list_1[ix] < list_2[ix]:
                return -1
            else:
                # list_1.pop(0)
                # list_2.pop(0)
                min_len -= 1
                ix += 1
        # temp_1a, temp_2a = len_1, len_2
        min_len = min(len_1, len_2)
        j = 0
        k = 0 # min_len # 298 > 29 , 949 > 94 
        if len_1 > len_2: # Ex: 832 vs 83 83832>83283 8383 83832 8383 471 vs 4 4471 < 4714 c) 4343434371 4343
            while k < len_1:
                # print(k)
                if list_1[k] > list_2[j]:
                    return 1
                elif list_1[k] < list_2[j]:
                    return -1
                else:
                    if j == len_2 - 1: 
                        j = 0
                        k += 1
                        continue
                j += 1
                k += 1
            while j != min_len:
                # print(j, k)
                if list_1[k-1] > list_2[j]:
                    return 1
                elif list_1[k-1] < list_2[j]:
                    return -1
                else:
                    j += 1
        elif len_1 < len_2:
                 # print(j, len_1, list_1, list_2)
            while k < len_2:
                # print(k)
                if list_1[j] > list_2[k]:
                    return 1
                elif list_1[j] < list_2[k]:
                    return -1
                else:
                    if j == len_1 - 1: 
                        j = 0
                        k += 1
                        continue
                j += 1
                k += 1
            while j != min_len:
                # print(j, k)
                if list_1[j] > list_2[k-1]:
                    return 1
                elif list_1[j] < list_2[k-1]:
                    return -1
                else:
                    j += 1
        return 1 # order doesn't matter
            
    A.sort(key = cmp_to_key(order_A), reverse = True)
    A = [str(x) for x in A]
    # return "".join(A)
    return str(int("".join(A)))  # Corner case with a list of zero

A = [8, 89]
A = [ 170, 480, 735, 896, 634, 844, 
     1, 610, 446, 591, 935, 802, 383, 8, 443, 247, 124, 461, 317, 457, 48, 886, 420, 
     473, 973, 464, 203, 288, 785, 703, 935, 
     7, 987, 48, 692, 633, 597, 857, 139, 733, 692, 68, 434, 587, 489, 517,
     305, 432, 577, 335, 586, 34, 659, 491, 310, 857, 256, 856, 257, 877, 209, 979, 653, 646, 2, 65, 858, 
     779, 372, 
     116, 404, 268, 364, 351, 866, 824, 947, 960, 91, 691, 492, 312, 609, 915, 579, 476, 248, 192 ]
A = [ 12, 121 ]

len(largestNumber(A))
len("".join(map(str, A)))
largestNumber(A)

# The expected return value: 
B = '9879799739609479359359191589688868778668588578578568448248027857797735733703692692691686596565364663463361060959759158758657957751749249148948484804764734644614574464434344324204043833723643513433531731231030528826825725624824722092031921701391241161'
# Your function returned the following: 
C = '9879799739609479359359191589688868778668588578578568448248027857779735733703692692691686596565364663463361060959759158758657957751749249148948484804764734644614574464434344324204043833723643513433531731231030528826825725624824722092031921701391241116'
for i in range(len(B)):
    if B[i] != C[i]:
        print(i, B[i-6:i+1], C[i-6:i+1])
        
        # 65 2785 779 2785 777
        # 66 785 7797 785 7779
        # 248 9124 116 9124 111
        # 249 124 1161 124 1116
        
A = [ 931, 
     94, 209, 448, 716, 903, 124, 372, 462, 196, 715, 802, 103, 740, 389, 872, 615, 638, 771, 829, 899, 999, 29, 163, 342, 902, 
     922, 312, 326, 817, 288, 75, 37, 286, 708, 589, 975, 747, 743, 699, 743, 
     954, 523, 989, 114, 402, 236, 855, 323, 79, 
     949, 176, 663, 587, 322 ]
# The expected return value: 
    # The expected return value: 
B = '9999899759549499493192290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103'
C = largestNumber(A)
B == C
len(B)
len(C)
set([len(str(x)) for x in A])
for i in range(len(B)):
    if B[i] != C[i]:
        print(i, B[i-6:i+6], C[i-6:i+6])
# 15 954 949 94 9319 954 94 9499 319
# 16 54 94994 931 92 54 94949 931 92   949 94 vs 94 949

A = [ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 
     29, 337, 646, 868, 974, 675, 
     271, 791, 124, 363, 
     298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 ]
# The expected return value: 
B = '99197494093090589587787286882579979879178278077273570968668667867566465335024704093953663633573372982927126124019124113'
C = largestNumber(A)
B == C
len(B)
len(C)
for i in range(len(B)):
    if B[i] != C[i]:
        print(i, B[i-6:i+6], C[i-6:i+6])
set([len(str(x)) for x in A])
    
# 99 7337 298 29 271 7337 29 298 271 # 298 > 29
# 100 337298292712 337292982712
# 101 372 98292 7126 372 92982 7126

        # list_1 = '298'
        # list_2 = '29'
        # len_1 = len(list_1)
        # len_2 = len(list_2)
        # j = 0
        # k = 0 # min_len # 298 > 29
        # if len_1 > len_2: # Ex: 832 vs 83 83832>83283 8383 83832 8383 471 vs 4 4471 < 4714 c) 4343434371 4343
        #     while k <= len_1:
        #         print(k)
        #         if list_1[k] > list_2[j]:
        #             print(1)
        #         elif list_1[k] < list_2[j]:
        #             print(j, k)
        #             print(list_1[k] , list_2[j])
        #             print(-1)
        #         else:
        #             if j == len_2 - 1: 
        #                 j == 0
        #                 k += 1
        #                 print(j, k)
        #                 continue
        #         j += 1
        #         k += 1
        #         print(j,k)
        
        # list_1 = '949'
        # list_2 = '94'
        # min_len = min(len_1, len_2)
        # j = 0
        # k = 0 # min_len # 298 > 29 , 949 > 94 
        # if len_1 > len_2: # Ex: 832 vs 83 83832>83283 8383 83832 8383 471 vs 4 4471 < 4714 c) 4343434371 4343
        #     while k < len_1:
        #         print(j, k, list_1[k] , list_2[j])
        #         if list_1[k] > list_2[j]:
        #            print('here')
        #         elif list_1[k] < list_2[j]:
        #             print('there')
        #         else:
        #             if j == len_2 - 1: 
        #                 print('b4 reset', j, k)
        #                 j = 0
        #                 k += 1
        #                 print('after reset', j, k)
        #                 continue
        #         j += 1
        #         k += 1
        #     while j != min_len:
        #         print(j, k)
        #         if list_1[k-1] > list_2[j]:
        #            print('here')
        #            break
        #         elif list_1[k-1] < list_2[j]:
        #             print('there')
        #             break
        #         else:
        #             j += 1
        #         print('end', j, k-1)

# Editorial:
# from functools import cmp_to_key

# class Solution:
# 	# @param A : tuple of integers
# 	# @return a strings
# 	def largestNumber(self, A):
# 	    ''' When comparing numbers we must pick the one leading
# 	        to the best concatenated result:
# 	        787978 > 787879  so 7879 is 'bigger' than 78
# 	                    but     7879 is 'less' than 788
# 	    '''
# 	    
# 	    # Convert to string once, for proper comparison a+b vs b+a
# 	    A = map(str, A)
# 	    key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
# 	    res = ''.join(sorted(A, key= key, reverse=True))
# 	    # Must left trim 0, apparently
# 	    res = res.lstrip('0')
# 	    return res if res else '0'
# Scala:
# class Solution {
#     def largestNumber(A: Array[Int]): String  = {
#       if (A.forall(_ == 0)) "0"
#       else {
#         A.map(_.toString).sortWith {
#           case (l, r) => {
#             val ll = l + r
#             val rr = r + l
#             rr > ll
#           }
#         }.reverse.mkString("")
#       }
#     }
# }
# bool compareNum(string a, string b) {
#     return a + b > b + a;
# }
# string Solution::largestNumber(const vector < int > & A) {
#     string result;
#     vector < string > str;
#     for (int i = 0; i < A.size(); i++) {
#         str.push_back(to_string(A[i]));
#     }
#     sort(str.begin(), str.end(), compareNum);
#     for (int i = 0; i < str.size(); i++) {
#         result += str[i];
#     }

#     int pos = 0;
#     while (result[pos] == '0' && pos + 1 < result.size()) pos++;
#     return result.substr(pos);
# }

# /**
#  * @input A : Read only ( DON'T MODIFY ) Integer array
#  * @input n1 : Integer array's ( A ) length
#  * 
#  * @Output string.
#  */
 
# import "sort"
# import "strconv"
# //import "fmt"

# type dictInt []int

# func (s dictInt) Less(i, j int) bool {
#     s1 := strconv.Itoa(s[i])
#     s2 := strconv.Itoa(s[j])
#     return s1 + s2 < s2 + s1
# }

# func (s dictInt) Len() int {
#     return len(s)
# }

# func (s dictInt) Swap(i, j int) {
#     s[i], s[j] = s[j], s[i]
# }

# func largestNumber(A []int )  (string) {
    
#     b := A

# //    fmt.Println("Unsorted: ", b)

#     sort.Sort(sort.Reverse(dictInt(b)))
# //    fmt.Println("Sorted: ", b)

#     lNum := ""

#     if (b[len(b) - 1] == 0) {
#         return "0";
#     }
    
#     for _, v := range b {
#         lNum += strconv.Itoa(v)
#     }
    
#     return lNum
# }
