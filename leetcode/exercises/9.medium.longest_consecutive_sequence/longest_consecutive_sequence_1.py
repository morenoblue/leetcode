# -----------------------
# Created    : 08/11/2025
# Last Edited: 08/11/2025 
# Topics     : 
# Big O      :
# Problem Id : 238
# -----------------------

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        max_seq_size = 0
        for num in set(nums):
            if num-1 not in unique_nums:
                curr_seq_size = 1
                while num+curr_seq_size in unique_nums:
                    curr_seq_size += 1
                max_seq_size = max(curr_seq_size, max_seq_size)

        return max_seq_size

s = Solution()
l = [100,4,200,1,3,2]
print(s.longestConsecutive(l))
