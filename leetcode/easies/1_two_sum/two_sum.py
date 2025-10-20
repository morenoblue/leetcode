class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		map = {}
		for index,value in enumerate(nums):
			complement = target - value
			if complement in map:
				return [index, map[complement]]
			map[value] = index
