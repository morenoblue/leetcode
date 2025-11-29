# -----------------------
# Created     : 28/11/2025
# Last Edited : 29/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 875. koko eating bananas
# References  : https://www.youtube.com/watch?v=U2SozAs9RzA
# Notes       :
# -----------------------

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (r + l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
