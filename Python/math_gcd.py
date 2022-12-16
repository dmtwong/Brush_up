# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 23:15:17 2022

@author: USER
"""


class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
		min_AB = min(A, B)
		
		if min_AB == 0:
			return max(A, B)
		elif min_AB == 1:
			return 1
		
		for i in range(min_AB, 0, -1):
			if (A % i == 0) and (B % i == 0):
				return i
			
		return i