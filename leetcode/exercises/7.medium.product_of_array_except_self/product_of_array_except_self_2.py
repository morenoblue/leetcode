# -----------------------
# Created    : 05/11/2025
# Last Edited: 05/11/2025 
# Topics     : 
# Big O      :
# Problem Id : 238
# -----------------------

class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]
        current = 1
        for i in range(len(nums)-1):
            res.append(current*nums[i]) 
            current = current*nums[i] 

        current = 1
        for i in range(-1, -len(nums), -1):
            res[i-1] = res[i-1]*current*nums[i]
            current = current*nums[i] 
        return res

s = Solution()
print(s.productExceptSelf([2, 1, 3, 4]))
