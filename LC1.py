"""
Title       : 1. Two Sum 
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hmap:
                return [hmap[comp], i]
            hmap[num] = i
        return []

# Time Complexity: O(n)
# Space Complexity: O(n)