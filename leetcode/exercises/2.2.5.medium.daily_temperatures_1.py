# -----------------------
# Created     : 23/11/2025
# Last Edited : 23/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 739
# References  : https://www.youtube.com/watch?v=cTBiBSnjO3c 
# Notes       : 
# -----------------------

class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = [0]
        res = [0]*len(temperatures)
        for i in range(1, len(temperatures)):

            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
                    
            else:
                stack.append(i)
        return res

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))


        
