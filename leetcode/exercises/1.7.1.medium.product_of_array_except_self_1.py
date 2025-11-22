# -----------------------
# Created     : 05/11/2025
# Last Edited : 05/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 238
# Source      :
# Notes       :
# -----------------------

class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        current = 1
        for i in range(len(nums)-1):
            prefix.append(current*nums[i]) 
            current = current*nums[i]

        postfix = [1]
        current = 1
        for i in range(-1, -len(nums), -1):
            postfix.append(current*nums[i]) 
            current = current*nums[i]
        postfix = postfix[::-1]

        res = []
        for i in range(len(prefix)):
            res.append(prefix[i]*postfix[i])

        return res

s = Solution()
print(s.productExceptSelf([2, 1, 3, 4]))
