// https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @cache
        def dp(i, j):
            if i == n or j == m:
                return int(j == m)
            elif s[i] == t[j]:
                return dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                return dp(i + 1, j)
        return dp(0, 0)