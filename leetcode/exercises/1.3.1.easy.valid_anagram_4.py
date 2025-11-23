# -----------------------
# Created     : 20/10/2025
# Last Edited : 24/10/2025
# Topics      : 
# Big O       :
# Problem Id  : 242
# References  :
# Notes       :
# -----------------------

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		return Counter(s) == Counter(t)
