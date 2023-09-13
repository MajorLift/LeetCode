// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_cnt = len([1 for i in range(m) for j in range(n) if grid[i][j] == 1])
        def dfs(r, c, minutes = 0):
            nonlocal fresh_cnt
            grid[r][c] = 2
            fresh_cnt -= 1
            print(fresh_cnt)
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    dfs(i, j, minutes + 1)
            return minutes

        rotten = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2]
        print(fresh_cnt)
        if fresh_cnt == 0:
            return max([dfs(i, j) for i, j in rotten])
        else:
            return -1
