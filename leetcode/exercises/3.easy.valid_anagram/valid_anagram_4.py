# -----------------------
# Created       : 20/10/2025
# Last Edited   : 24/10/2025
# Big O         :
# Topics        : 
# Problem Id    : 242
# -----------------------

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		return Counter(s) == Counter(t)
