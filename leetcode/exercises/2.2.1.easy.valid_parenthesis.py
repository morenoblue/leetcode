# -----------------------
# Created     : 17/11/2025
# Last Edited : 17/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 20
# Source      :
# Notes       :
# -----------------------

class Solution:
    def isValid(self, s: str) -> bool:
        map = {
                "}": "{",
                ")": "(",
                "]": "[",
        }
        stack = []
        for i in s:
            if i in map:
                if len(stack) == 0 or stack[-1] != map.get(i, False):
                    return False
                stack.pop()
            else:
                stack.append(i)

        return True if len(stack) == 0 else False 
        

s = Solution()
print(s.isValid("(){}}{"))

  
