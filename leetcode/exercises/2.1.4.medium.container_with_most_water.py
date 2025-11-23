# -----------------------
# Created     : 13/11/2025
# Last Edited : 13/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 11
# References  :
# Notes       :
# -----------------------

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2: return 0

        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            base = abs(r - l)
            min_height = min(height[l], height[r])
            max_area = max(max_area, base*min_height)

            if height[l] < height[r]:
                 l += 1
            elif height[l] > height[r]:
                 r -= 1
            else:
                 r -= 1
                 l += 1
        return max_area

s = Solution()
print(s.maxArea([1,2,1]))

            

        
