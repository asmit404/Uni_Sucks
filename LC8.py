"""
Title       : 8. String to Integer (atoi)
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        sign = -1 if s and s[0] == '-' else 1
        if s and (s[0] in ['-', '+']): s = s[1:]
        res = 0
        for char in s:
            if not char.isdigit(): break
            res = res * 10 + int(char)
        res *= sign
        return max(-2**31, min(res, 2**31 - 1))

# Time Complexity: O(n)
# Space Complexity: O(1)