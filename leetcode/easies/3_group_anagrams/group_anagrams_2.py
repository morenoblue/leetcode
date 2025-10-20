# Self Solved: False

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
print()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
