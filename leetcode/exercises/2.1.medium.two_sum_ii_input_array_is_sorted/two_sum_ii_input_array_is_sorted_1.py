# -----------------------
# Created    : 13/11/2025
# Last Edited: 13/11/2025 
# Topics     : 
# Big O      :
# Problem Id : 167
# -----------------------

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target: return [l+1,r+1]
            if sum < target:
                l += 1
            else:
                r -= 1

        return [0,0]

s = Solution()
print(s.twoSum([2,7,11,15],13))
    
        
