# -----------------------
# Created     : 22/11/2025
# Last Edited : 22/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 150
# References  :
# Notes       : Man this backtracking stuff is tuff
# -----------------------

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
            
            res = []
            
            def backtrack(open_n, closed_n, path):
                
                if open_n == closed_n == n:
                    res.append(path)
                    return
                
                if open_n < n:
                    backtrack(open_n + 1, closed_n, path + "(")
                 
                if closed_n < open_n:
                    backtrack(open_n, closed_n + 1, path + ")")
                    
            backtrack(0, 0, "")
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
