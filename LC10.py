"""
Title       : 10. Regular Expression Matching
Difficulty  : Hard
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.backtrack(s, p, len(s) - 1, len(p) - 1, {})

    def backtrack(self, s, p, i, j, cache):
        key = (i, j)
        if key in cache:
            return cache[key]

        if i == -1 and j == -1:
            return cache.setdefault(key, True)

        if i != -1 and j == -1 or i == -1 and p[j] != '*':
            return cache.setdefault(key, False)

        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            return cache.setdefault(key, k == -1)

        if p[j] == '*':
            if any([self.backtrack(s, p, i, j - 2, cache), 
                    (p[j - 1] == s[i] or p[j - 1] == '.') and self.backtrack(s, p, i - 1, j, cache)]):
                return cache.setdefault(key, True)

        if p[j] == '.' or s[i] == p[j]:
            if self.backtrack(s, p, i - 1, j - 1, cache):
                return cache.setdefault(key, True)

        return cache.setdefault(key, False)

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)