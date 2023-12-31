"""
Title       : 12. Integer to Roman
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        pool = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], [
            "L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        res = ""
        for sym, val in pool:
            count, num = divmod(num, val)
            res += sym * count
        return res

# Time Complexity  : O(1)
# Space Complexity : O(1)