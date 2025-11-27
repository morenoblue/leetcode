# -----------------------
# Created     : 27/11/2025
# Last Edited : 27/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 704
# References  : 
# Notes       : 
# -----------------------

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = int(l + (r - l)/2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return -1
