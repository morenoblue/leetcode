# -----------------------
# Created     : 21/10/2025
# Last Edited : 24/10/2025
# Topics      : 
# Big O       :
# Problem Id  : 347
# References  :
# Notes       :
# -----------------------

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1

        result = []
        map = sorted(map.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(map[i][0])

        return result


sol = Solution()
print()
print(sol.topkfrequent([1,1,1,2,2,3], 2))
