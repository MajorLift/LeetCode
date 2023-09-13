// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid = [[not bool(grid[i][j]) for j in range(n)] for i in range(m)]
        memo = [[int(i * j == 0) for j in range(n)] for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            memo[i][j] = ((memo[i - 1][j] if grid[i - 1][j] else 0) 
                + (memo[i][j - 1] if grid[i][j - 1] else 0))
        return memo[-1][-1]