// https://leetcode.com/problems/regular-expression-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        @cache
        def dp(i, j):
            if j == n:
                return i == m
            is_curr_match = i < m and p[j] in (s[i], ".")
            if j < n - 1 and p[j + 1] == "*":
                return dp(i, j + 2) or (is_curr_match and dp(i + 1, j))
            return is_curr_match and dp(i + 1, j + 1)
        return dp(0, 0)