# -----------------------
# Created     : 27/11/2025
# Last Edited : 27/11/2025 
# Topics      : 
# Big O       :
# Problem Id  : 
# References  : 
# Notes       : Self Solved
# -----------------------

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)

        target_row = 0
        while l < r:
            m = int(l + (r - l)/2)

            if matrix[m][0] <= target <= matrix[m][-1]:
                target_row = m
                break

            elif target < matrix[m][0]:
                r = m

            else:
                l = m + 1

        l = 0
        r = len(matrix[target_row])

        while l < r:
            m = int(l + (r - l)/2)

            if target == matrix[target_row][m]:
                return True

            elif target < matrix[target_row][m]:
                r = m

            else:
                l = m + 1
        return False

            





