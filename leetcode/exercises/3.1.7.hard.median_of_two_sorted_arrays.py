# -----------------------
# Created     : 06/12/2025
# Last Edited : 10/12/2025 
# Topics      : 
# Big O       :
# Problem Id  : 4. Median of Two Sorted Arrays
# References  : https://youtu.be/q6IEA26hvXc?si=_FV_HNLEili4HEvg
# Notes       : This solution broke my spirit
# -----------------------

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        half = (len(nums1) + len(nums2)) // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            m_A = l + (r - l) // 2
            m_B = half - m_A - 2

            A_left  = A[m_A]     if m_A >= 0 else float("-inf")
            A_right = A[m_A + 1] if (m_A + 1) < len(A) else float("inf")
            B_left  = B[m_B]     if m_B >= 0 else float("-inf")
            B_right = B[m_B + 1] if (m_B + 1) < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if (len(nums1) + len(nums2)) % 2 != 0:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = m_A - 1
            else:
                l = m_A + 1

s = Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))

