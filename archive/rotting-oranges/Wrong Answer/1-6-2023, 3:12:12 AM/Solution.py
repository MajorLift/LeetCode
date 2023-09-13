// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        m, n = len(grid), len(grid[0])
        fresh = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        rotten = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2]
        if not fresh: 
            return 0
        if not rotten:
            return -1
        
        def dfs(r, c, thread, clock = 0):
            print(thread, (r, c), clock)
            # print(grid)
            grid[r][c] = 2
            neighbors = [(i, j) for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)) \
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1]
            times = [dfs(i, j, thread, clock + 1) for i, j in neighbors]
            return max(times or [clock])

        times = [dfs(i, j, thread) for thread, (i, j) in enumerate(rotten)]
        # print(times)
        fresh = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        if len(fresh) == 0:
            return max(times)
        else:
            return -1
