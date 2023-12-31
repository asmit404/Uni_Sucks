"""
Title       : 3. Longest Substring Without Repeating Characters
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = res = 0
        vis = [-1] * 128
        for i, char in enumerate(s):
            start = max(start, vis[ord(char)] + 1)
            res = max(res, i - start + 1)
            vis[ord(char)] = i
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)