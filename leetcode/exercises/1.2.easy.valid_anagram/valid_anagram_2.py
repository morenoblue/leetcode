# -----------------------
# Created       : 24/10/2025
# Last Edited   : 24/10/2025
# Big O         :
# Topics        : 
# Problem Id    : 242
# -----------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for i,j in zip(s,t):
            counter[i] = counter.get(i, 0) + 1
            counter[j] = counter.get(j, 0) - 1

        for v in counter.values():
            if v != 0:
                return False
        return True
