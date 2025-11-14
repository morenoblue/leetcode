# -----------------------
# Created    : 05/11/2025
# Last Edited: 05/11/2025 
# Topics     : 
# Big O      :
# Problem Id : 36
# -----------------------

# note(@morenoblue): I'm kinda super proud of myself rn, this solution is 100% 
#                    from my own brain, didn't check anywhere else to solve this
#                    one <3. Thought I'm already getting ready to be absolutely 
#                    reckt once I check for the other solutions just to find out
#                    that mine is absolutely trash.
#
#                    **A few moments later** ...yep, it happened exactly how I 
#                    predicted... I overcomplicated this thing... f*******ck!

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # rule 3

        blocks = [
            [i[0:3] for i in board[:3]],
            [i[3:6] for i in board[:3]],
            [i[6:9] for i in board[:3]],

            [i[0:3] for i in board[3:6]],
            [i[3:6] for i in board[3:6]],
            [i[6:9] for i in board[3:6]],

            [i[0:3] for i in board[6:9]],
            [i[3:6] for i in board[6:9]],
            [i[6:9] for i in board[6:9]],
        ]

        line_counts = defaultdict(dict)
        column_counts = defaultdict(dict)
        line_block = 0
        column_block = 0
        for idx, block in enumerate(blocks):
            block_counts = {}

            for i,v in enumerate(block):
                current_line = i + line_block

                for k, j in enumerate(v):
                    current_column = k + column_block 

                    if j == ".": continue
                    line_counts[current_line][j] = line_counts[current_line].get(j, 0) + 1
                    column_counts[current_column][j] = column_counts[current_column].get(j, 0) + 1
                    block_counts[j] = block_counts.get(j, 0) + 1
                    if block_counts[j] > 1: return False
            
            if idx < 2: 
                column_block += 3
            elif idx == 2:
                column_block = 0
                line_block += 3
            elif 2 < idx < 5:
                column_block += 3
            elif idx == 5:
                column_block = 0
                line_block += 3
            else:
                column_block += 3

        # rule 1
        for counts in line_counts.values():
            for c in counts.values():
                if c != 1: return False

        # rule 2
        for counts in column_counts.values():
            for c in counts.values():
                if c != 1: return False

        return True

s = Solution()
print(s.isValidSudoku([
                        ["8","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"],
      ]))
