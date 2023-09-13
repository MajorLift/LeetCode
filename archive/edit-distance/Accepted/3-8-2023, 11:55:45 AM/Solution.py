// https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        @cache
        def dp(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if s[i] == t[j]:
                return dp(i + 1, j + 1)
            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
        return dp(0, 0)