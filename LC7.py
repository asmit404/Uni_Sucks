"""
Title       : 7. Reverse Integer
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT32 = 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > MAX_INT32:
                return 0
        return sign * rev

# Time Complexity: O(log(n))
# Space Complexity: O(1)