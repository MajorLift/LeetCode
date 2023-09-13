// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid

from functools import cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(r, c):
            ans = 1
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] > grid[r][c]:
                    ans += dfs(i, j)
            return ans
        return sum(dfs(i, j) for i in range(m) for j in range(n))