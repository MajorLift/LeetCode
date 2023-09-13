// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_sum = +math.inf
        stack = [(1, 0, 0)]
        visited = set()
        while stack:
            curr_sum, x, y = stack.pop()
            if x == m - 1 and y == n - 1:
                min_sum = min(min_sum, curr_sum)
                visited = set()
            for i, j in (x + 1, y), (x, y + 1):
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                    stack.append((curr_sum + grid[i][j], i, j))
                    visited.add((i, j))
        return min_sum