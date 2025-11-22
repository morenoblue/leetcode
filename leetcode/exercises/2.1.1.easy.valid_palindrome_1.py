# -----------------------
# Created     : 12/11/2025
# Last Edited : 12/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 125
#  Source      :
#Notes       :
# -----------------------


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 and s.isalpha(): return True

        left = 0
        right = len(s) - 1
        
        while left < right:

            while not s[left].isalnum():
                left += 1 
                if left == len(s): return True

            while not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower(): 
                return False

            left += 1
            right -= 1

        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome(".,"))




        
