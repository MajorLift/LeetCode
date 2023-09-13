// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid

from functools import cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(r, c):
            return sum(1 + dfs(i, j) if 0 <= i < m and 0 <= j < n and grid[i][j] > grid[r][c] else 0 \
                for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))) or 1
        return sum(dfs(i, j) for i in range(m) for j in range(n))