# -----------------------
# Created       : 20/10/2025
# Last Edited   : 20/10/2025
# Self Solved   : False
# Big O         : O(n)
# Topics        : 
# -----------------------

class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		map = {}
		for index,value in enumerate(nums):
			complement = target - value
			if complement in map:
				return [index, map[complement]]
			map[value] = index

sol = Solution()
print(sol.twoSum([1,5,6,2,2,8], 11))

