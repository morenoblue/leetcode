# -----------------------
# Created     : 28/11/2025
# Last Edited : 28/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 875. koko eating bananas
# References  : 
# Notes       : Self Solved
# -----------------------

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            k = l + (r - l) // 2
            c = 0
            for i, v in enumerate(piles):
                c += math.ceil(v/k)

                if i != len(piles) - 1:
                    if c >= h:
                        l = k + 1
                        break
                else:
                    if c > h:
                        l = k + 1
                    else:
                        r = k - 1
                        res = k
        return res

s = Solution()
print(s.minEatingSpeed([4,11,20,23,30], 5))



        
