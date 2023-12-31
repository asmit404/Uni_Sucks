"""
Title       : 6. ZigZag Conversion
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        rows = [""] * numRows
        index, step = 0, 1
        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(rows)

# Time Complexity: O(n)
# Space Complexity: O(n)