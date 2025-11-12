# -----------------------
# Created       : 22/10/2025
# Last Edited   : 22/10/2025
# Big O         :
# Topics        : 
# Problem Id    : 217
# -----------------------

class Solution:
	def containsDuplicate(self, nums: list[int]) -> bool:
		a = set()
		for i in nums:
			if i not in a:
				a.add(i)
			else:
				return True
		return False

sol = Solution()
print()
print(sol.containsDuplicate([2, 1, 10, 12, 1]))
