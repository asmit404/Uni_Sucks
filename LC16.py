"""
Title       : 16 . 3Sum Closest
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr = num + nums[left] + nums[right]
                if abs(curr - target) < abs(res - target):
                    res = curr
                left, right = (left + 1, right) if curr < target else (left, right - 1)
        return res

# Time Complexity  : O(n^2)
# Space Complexity : O(1)