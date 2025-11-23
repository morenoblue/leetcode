# -----------------------
# Created     : 05/11/2025
# Last Edited : 05/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 36
# References  :
# Notes       :
# -----------------------

from collections import defaultdict
fr Source      :

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols    = defaultdict(set)
        rows    = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if board[r][c] in rows[r]: return False
                if board[r][c] in cols[c]: return False
                if board[r][c] in squares[(r // 3, c // 3)]: return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

s = Solution()
print(s.isValidSudoku([
                        ["8","3",".",   ".","7",".",   ".",".","."],
                        ["6",".",".",   "1","9","5",   ".",".","."],
                        [".","9",".",   ".",".",".",   ".","6","."],


                        [".",".",".",   ".","6",".",   ".",".","3"],
                        ["4",".",".",   "8",".","3",   ".",".","1"],
                        ["7",".",".",   ".","2",".",   ".",".","6"],


                        [".","6",".",   ".",".",".",   "2","8","."],
                        [".",".",".",   "4","1","9",   ".",".","5"],
                        [".",".",".",   ".","8",".",   ".","7","9"],
      ]))




        
        

