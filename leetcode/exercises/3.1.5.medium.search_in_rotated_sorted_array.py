# -----------------------
# Created     : 03/12/2025
# Last Edited : 03/12/2025 
# Topics      : 
# Big O       :
# Problem Id  : 33. Search in Rotated Sorted Array
# References  : https://www.youtube.com/watch?v=U8XENwh8Oy8
# Notes       : Damn, got absolutely rekt by this one. No problem though, 
#               Neetcode for the rescue
# -----------------------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target < nums[l] or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0));


