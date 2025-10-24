# -----------------------
# Created       : 20/10/2025
# Last Edited   : 24/10/2025
# Big O         :
# Topics        : 
# Problem Id    : 49
# -----------------------

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sets = defaultdict(list)
        for i in strs:

            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] += 1

            sets[tuple(count)].append(i)

        return list(sets.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
