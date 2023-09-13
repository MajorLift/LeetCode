// https://leetcode.com/problems/regular-expression-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            if i < len(s) and p[j] in (s[i], "."):
                if j < len(p) - 1 and p[j + 1] == "*":
                    return dp(i, j + 2) or dp(i + 1, j)
                else:
                    return dp(i + 1, j + 1)
            return True
        return dp(0, 0)
