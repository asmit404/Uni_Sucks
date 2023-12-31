"""
Title       : 9. Palindrome Number
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        res = str(x)
        return res == res[::-1]

# Time Complexity: O(n)
# Space Complexity: O(n)