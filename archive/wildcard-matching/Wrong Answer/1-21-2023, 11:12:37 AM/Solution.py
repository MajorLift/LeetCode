// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def backtrack(i = 0, j = 0):
            if i == len(s):
                return True
            if j == len(p):
                return False
            if s[i] == p[j] or p[j] == "?":
                return backtrack(i + 1, j + 1)
            if p[j] == "*":
                return backtrack(i + 1, j) or backtrack(i + 1, j + 1)
        return backtrack()