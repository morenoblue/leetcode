# -----------------------
# Created     : 18/10/2025
# Last Edited : 24/10/2025
# Topics      : 
# Big O       :
# Problem Id  : 1
# References  :
# Notes       :
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

