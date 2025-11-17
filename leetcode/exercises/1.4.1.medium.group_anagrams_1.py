# -----------------------
# Created       : 20/10/2025
# Last Edited   : 24/10/2025
# Big O         :
# Topics        : 
# Problem Id    : 49
# -----------------------

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sets = {}
        for i in strs:

            key = {}
            for j in i:
                key[j] = key.get(j, 0) + 1
            key = frozenset(key.items())

            if key in sets:
                sets[key].append(i)
            else:
                sets[key] = [i]
        return list(sets.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
