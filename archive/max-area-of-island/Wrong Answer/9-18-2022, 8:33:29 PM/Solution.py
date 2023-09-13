// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr_area = 0
                    queue = deque([[i, j]])
                    while queue:
                        row, col = queue.popleft()
                        curr_area += 1
                        grid[row][col] = 0
                        if row > 0 and grid[row - 1][col] == 1:
                            queue.append([row - 1, col])
                        if row < m - 1 and grid[row + 1][col] == 1:
                            queue.append([row + 1, col])
                        if col > 0 and grid[row][col - 1] == 1:
                            queue.append([row, col - 1])
                        if col < n - 1 and grid[row][col + 1] == 1:
                            queue.append([row, col + 1])
                    max_area = max(max_area, curr_area)
        return max_area