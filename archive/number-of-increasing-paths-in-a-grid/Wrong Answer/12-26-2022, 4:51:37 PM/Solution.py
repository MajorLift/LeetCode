// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid

from functools import cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(r, c):
            if dp[r][c] == 0:
                for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] > grid[r][c]:
                        dp[r][c] += dfs(i, j)
            return dp[r][c]
        return sum(dfs(i, j) for i in range(m) for j in range(n))