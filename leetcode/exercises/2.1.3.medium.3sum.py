# -----------------------
# Created     : 13/11/2025
# Last Edited : 27/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 15  
# References  :
# Notes       : 👀
# -----------------------

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        
        for c in range(len(nums)):

            if c > 0 and nums[c] == nums[c-1]:
                continue

            l = c + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r] + nums[c]

                if sum == 0:
                    triplets.append([nums[l], nums[r], nums[c]])

                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1] :
                        l += 1

                    # note(@morenoblue): we could comment this code paragraph 
                    #                    and it would still work.
                    r -= 1
                    while r > 0 and nums[r] == nums[r+1] :
                        r -= 1

                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return triplets

s = Solution()
print(s.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))

                



        
