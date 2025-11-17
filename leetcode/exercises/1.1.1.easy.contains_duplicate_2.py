# -----------------------
# Created       : 23/10/2025
# Last Edited   : 23/10/2025
# Big O         : 
# Topics        : 
# -----------------------

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

sol = Solution()
print()
print(sol.containsDuplicate([2, 1, 10, 12, 1]))
