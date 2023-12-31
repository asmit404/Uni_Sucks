"""
Title       : 11. Container With Most Water
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = maxArea = 0
        right = len(height) - 1
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            left, right = (left + 1, right) if height[left] < height[right] else (left, right - 1)
        return maxArea

# Time Complexity  : O(n)
# Space Complexity : O(1)