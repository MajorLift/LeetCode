// https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in product(range(m), range(n)):
            if i * j == 0:
                memo[i][j] = i + j
            elif s[i] == t[j]:
                memo[i][j] = memo[i - 1][j - 1]
            else:
                memo[i][j] = 1 + min(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1])
        return memo[-1][-1] + 1