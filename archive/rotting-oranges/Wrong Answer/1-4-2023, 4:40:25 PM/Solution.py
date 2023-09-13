// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        fresh_cnt = len([grid[i][j] for i in range(m) for j in range(n) if grid[i][j] == 1])
        if fresh_cnt == 0:
            return 0
        minutes = 0
        
        def dfs(r, c):
            nonlocal fresh_cnt, minutes
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if fresh_cnt == 0:
                    return
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    fresh_cnt -= 1
                    grid[i][j] = 2
                    dfs(i, j)
            minutes += 1
        
        [dfs(i, j) for i, j in [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2]]
        return minutes if fresh_cnt == 0 else -1