# -----------------------
# Date       : 21/10/2025
# Self Solved: False
# Topics     : Bucket Sort
# -----------------------

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 0:
            return []

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, -1) + 1

        freq = [[] for i in range(len(nums))]
        for num, count in counts.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq)-1, -1, -1):
            if len(freq[i]) == 0:
                continue

            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result

sol = Solution()
print()
print(sol.topKFrequent([11, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6], 3))
