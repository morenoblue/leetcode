# -----------------------
# Created    : 05/11/2025
# Last Edited: 07/11/2025 
# Topics     : 
# Big O      :
# Problem Id : 238
# -----------------------

class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]
        prefix = 1
        for i in range(len(nums)-1):
            res.append(prefix*nums[i]) 
            prefix *= nums[i] 

        postfix = 1
        for i in range(-1, -len(nums), -1):
            res[i-1] *= postfix*nums[i]
            postfix *= nums[i] 
        return res

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
