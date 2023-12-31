"""
Title       : 4. Median of Two Sorted Arrays
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        pool = sorted(nums1 + nums2)
        total = len(pool)
        if total & 1 == 1:
            return float(pool[total // 2])
        else:
            mid1, mid2 = pool[total // 2 - 1], pool[total // 2]
            return (float(mid1) + float(mid2)) / 2.0

# Time Complexity: O(n + m log(n + m))
# Space Complexity: O(n + m)