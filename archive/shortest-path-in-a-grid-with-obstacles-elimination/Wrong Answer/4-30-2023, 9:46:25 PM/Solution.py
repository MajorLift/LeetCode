// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = map(len, (grid, grid[0]))
        self.m, self.n = m, n
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        SRC, DST = (0, 0), (m - 1, n - 1)
        dist = [[+inf] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(self.manhattan(*SRC), k, SRC)]
        while pq:
            heuristic, quota, (r, c) = heappop(pq)
            if heuristic <= quota:
                return dist[r][c] + heuristic
            if (r, c) == DST:
                break
            for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                if dist[r][c] + 1 < dist[i][j] and quota - grid[i][j] >= 0:
                    dist[i][j] = dist[r][c] + 1
                    heappush(pq, (self.manhattan(i, j), quota - grid[i][j], (i, j)))

        return dist[-1][-1] if dist[-1][-1] < +inf else -1            

    def manhattan(self, x, y):
        return abs(self.m - 1 - x) + abs(self.n - 1 - y)