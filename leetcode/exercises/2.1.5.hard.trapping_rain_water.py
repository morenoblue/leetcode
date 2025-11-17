class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l_m = 0
        r_m = 0
        l = 0
        r = len(height) - 1
        while l <= r:
            if l_m <= r_m:
                res += max(l_m - height[l], 0)
                if height[l] > l_m:
                    l_m = height[l]
                l += 1
            else:
                res += max(r_m - height[r], 0)
                if height[r] > r_m:
                    r_m = height[r]
                r -= 1
        return res

s = Solution()
print(s.trap([4,2,0,3,2,5]))

#      o
# o    o
# o  o o
# oo ooo
# oo ooo
