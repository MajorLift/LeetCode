// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid = grid
        cnt = len([1 for i in range(m) for j in range(n) if grid[i][j] == 1])
        if cnt == 0:
            return 0

        def dfs(r, c, minutes = 0):
            nonlocal cnt
            if cnt == 0:
                return minutes
            max_time = 0
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = 2
                    cnt -= 1
                    max_time = max(max_time, dfs(i, j, minutes + 1))
            return max_time

        rotten = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2]
        time = 0
        for i, j in rotten:
            time = max(time, dfs(i, j))
        if cnt == 0 and time > 0:
            return time
        else:
            return -1

    