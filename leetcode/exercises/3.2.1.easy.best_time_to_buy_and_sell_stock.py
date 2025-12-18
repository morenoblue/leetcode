# -----------------------
# Created     : 11/12/2025
# Last Edited : 11/12/2025 
# Topics      : 
# Big O       :
# Problem Id  : 121. Best Time to Buy and Sell Stock
# References  : https://www.youtube.com/watch?v=1pkOgXD63yU
# Notes       :
# -----------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        cmax = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit >= 0:
                if profit > cmax:
                    cmax = profit
                r += 1
            else:
                l = r
                r = l + 1
        return cmax
            
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
