"""
Title       : 13. Roman to Integer
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum(hmap[c] if hmap[c] >= hmap[n] else -hmap[c] for c, n in zip(s, s[1:]+'I'))

# Time Complexity  : O(n)
# Space Complexity : O(1)