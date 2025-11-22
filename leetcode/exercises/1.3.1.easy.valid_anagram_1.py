# -----------------------
# Created     : 20/10/2025
# Last Edited : 24/10/2025
# Topics      : 
# Big O       :
# Problem Id  : 242
# Source      :
# Notes       :
# -----------------------

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		map1, map2 = {}, {}
		for i,j in zip(s,t):
			map1[i] = map1.get(i, 0) + 1
			map2[j] = map2.get(j, 0) + 1

		return map1 == map2
