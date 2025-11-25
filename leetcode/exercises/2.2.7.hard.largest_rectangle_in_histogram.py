# -----------------------
# Created     : 25/11/2025
# Last Edited : 25/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 84
# References  : https://www.youtube.com/watch?v=zx5Sw9130L0
# Notes       : 
# -----------------------

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []
        max_area = 0
        for r in range(len(heights)+1):
            i = r
            h = heights[r] if r < len(heights) else 0

            if not stack:
               stack.append((i, h))
               continue
            
            if h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while stack and stack[-1][1] > h:
                    area = (i - stack[-1][0]) * stack[-1][1]
                    max_area = max(max_area, area)
                    start = stack[-1][0]
                    stack.pop()
                stack.append((start, h))
        return max_area

s = Solution()
print(s.largestRectangleArea([2,4]))



