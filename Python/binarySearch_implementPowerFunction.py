# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:06:38 2022

@author: USER
# """


# There are two major things to note here:

# 1) Overflow situation: Note that if x is large enough, multiplying x to the answer might overflow in integer.

# 2) Multiplying x one by one to the answer is O(n). We are looking for something better than O(n).

# If n is even, note the following:

# x ^ n = (x * x) ^ n/2

# For modulus of negative integers, try to put the divisor in the range of dividend, i.e. if a % b, where a is a negative integer,
# you can perform, (a % b + b) % b

# Can you use the above observation to come up with a solution better than O(n)?


# Implement pow(x, n) % d.
# In other words, given x, n and d,
# Find (xn % d)
# Note that remainders on division cannot be negative. In other words, make sure the answer you return is non-negative integer.


# Problem Constraints
# -109 <= x <= 109
# 0 <= n <= 109
# 1 <= d <= 109


# Example Input
# Input 1:
x = 2
n = 3
d = 3
# Input 2:
x = 5
n = 2
d = 6

# Example Output
# Output 1:2
# Output 2:1


# Example Explanation
# Explanation 1:
# 2^3 % 3 = 8 % 3 = 2.
# Explanation 2:
# 5^2 % 6 = 25 % 6 = 1.

# class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    # def pow(self, x, n, d):
# temp = 11
# temp //= 2
# temp

def pow(x, n, d):
    result = 1
    base = x % d
    while (n > 0):
        if n % 2 == 1:
            # print(n, result, base)
            result *= base 
            result = result % d
        n //= 2
        # print('here', n, base, result)
        base *= base
        base = base % d
        # print(base)
    result = result % d
    # print(result)
    
    if (result < 0):
        result += d
        
    return result 

pow(x,n,d)      
t1 = 71045970
t2 = 41535484
t3 = 64735492   
pow(t1,t2,t3)   


# C++:
#     int Solution::pow(int x, int n, int p) {
#     assert(x >= -1e9 && x <= 1e9);
#     assert(n >= 0 && n <= 1e9);
#     assert(p >= 1 && p <= 1e9);
#     if (n == 0) return 1 % p;

# 			long long ans = 1, base = x;
# 			while (n > 0) {
# 				// We need (base ** n) % p. 
# 				// Now there are 2 cases. 
# 				// 1) n is even. Then we can make base = base^2 and n = n / 2.
# 				// 2) n is odd. So we need base * base^(n-1) 
# 				if (n % 2 == 1) {
# 					ans = (ans * base) % p;
# 					n--;
# 				} else {
# 					base = (base * base) % p;
# 					n /= 2;
# 				}
# 			}
# 			if (ans < 0) ans = (ans + p) % p;
# 			return ans;
# }
# java:
#     public class Solution {
# 	public int pow(int x, int n, int d) {
# 	    
# 	    long a = x;
# 	    long res = 1L;
# 	    
# 	    while (n > 0) {
# 	        
# 	        if (n % 2 == 1) {
# 	            res *= a;
# 	            res %= d;
# 	        }
# 	        
# 	        a *= a;
# 	        a %= d;
# 	        n = n >> 1;
# 	        
# 	    }
# 	    
# 	    res = (res + d) % d;
# 	    
# 	    return (int) res;
# 	    
# 	}
# }