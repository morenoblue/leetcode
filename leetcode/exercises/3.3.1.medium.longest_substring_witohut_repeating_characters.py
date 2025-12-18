# -----------------------
# Created     : 11/12/2025
# Last Edited : 11/12/2025 
# Topics      : 
# Big O       :
# Problem Id  : 3. Longest Substring Without Repeating Characters
# References  :
# Notes       : Believe it or not, I solve this one entirely on my own!!!! I'm so proud rn
# -----------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        hashset = {s[0]}
        l = 0
        r = 1
        longest = s[l:r]
        while r < len(s):
                
            while l < r and s[r] in hashset:
                hashset.remove(s[l])
                l += 1

            if l == r:
                hashset.add(s[l])
                r += 1
                continue

            hashset.add(s[r])
            r += 1

            if len(s[l:r]) > len(longest):
                longest = s[l:r]

        return len(longest)

s = Solution()
print(s.lengthOfLongestSubstring("abcabcdbb"))

