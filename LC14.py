"""
Title       : 14. Longest Common Prefix
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for group in zip(*strs):
            if all(c == group[0] for c in group):
                prefix += group[0]
            else:
                break
        return prefix

# Time Complexity  : O(nm)
# Space Complexity : O(1)