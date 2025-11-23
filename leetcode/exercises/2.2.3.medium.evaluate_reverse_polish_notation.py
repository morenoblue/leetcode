# -----------------------
# Created     : 19/11/2025
# Last Edited : 19/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 150
# References  :
# Notes       :
# -----------------------

import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []
        for i in tokens:

            if i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            elif i == "+":
                stack.append(stack.pop() + stack.pop())

            elif i == "*":
                stack.append(stack.pop() * stack.pop())

            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(i))

        return stack[0]

s = Solution()
print(s.evalRPN(["4","13","5","/","+"]))


                
                


