# -----------------------
# Created     : 24/11/2025
# Last Edited : 24/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 853
# References  : https://www.youtube.com/watch?v=Pr6T-3yB9RM
# Notes       : 
# -----------------------

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in pairs:
            rs = (target - p) / s

            if not stack:
                stack.append(rs)
                continue

            if rs > stack[-1] :
                stack.append(rs)

        return len(stack)

s = Solution()
print(s.carFleet(10, [6, 8], [3, 2]))
        
