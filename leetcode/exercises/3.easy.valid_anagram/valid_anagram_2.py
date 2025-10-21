# Self Solved: False

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		return Counter(s) == Counter(t)
