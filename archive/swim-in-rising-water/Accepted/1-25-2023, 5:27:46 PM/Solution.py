// https://leetcode.com/problems/swim-in-rising-water

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([(0, 0)])
        pq = [(grid[0][0], 0, 0)]
        t = 0
        while pq:
            w, i, j = heappop(pq)
            t = w
            if i == j == n - 1:
                break
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    heappush(pq, (max(grid[x][y], t), x, y))
                    visited.add((x, y))
        return t