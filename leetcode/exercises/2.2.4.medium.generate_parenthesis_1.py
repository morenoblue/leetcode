# -----------------------
# Created     : 22/11/2025
# Last Edited : 22/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 150
# Source      :
# Notes       : Man this backtracking stuff is tuff
# -----------------------

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
            
            stack = []
            res = []
            def backtrack(open_n, closed_n):
                
                if open_n == closed_n == n:
                    res.append("".join(stack))
                    return
                
                if open_n < n:
                    stack.append("(")
                    backtrack(open_n + 1, closed_n)
                    stack.pop()
                 
                if closed_n < open_n:
                    stack.append(")")
                    backtrack(open_n, closed_n + 1)
                    stack.pop()
                    
            backtrack(0, 0)
            return res

s = Solution()
print(s.generateParenthesis(3))

# n = 3
#
# 
#                                                                                 
#                                               ""                                    
#                                                                                    
#                                           "("                                       
#
#                                    "(("                                           
#                                                                                    
#                        "((("                   "(()"                                
#
#                                                                                    
#                            "((()"        "(()("         "(())"                         
#
#                                                                                            
#                               "((())"          "(()()"       "(())("                          
#
#                                                                                    
#                                  "((()))"           "(()())"      "(())()"                                    
#                                                                                    
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
