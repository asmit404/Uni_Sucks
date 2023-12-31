"""
Title       : 17. Letter Combinations of a Phone Number
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        hmap = {"2": "abc", "3": "def", "4": "ghi",
                "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        chars = [hmap[digit] for digit in digits]
        return [''.join(combination) for combination in product(*chars)]

# Time Complexity  : O(n * 4 ^ n)
# Space Complexity : O(n * 4 ^ n)