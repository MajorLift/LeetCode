// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = map(len, (grid, grid[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        SRC, DST = (0, 0), (m - 1, n - 1)
        self.total = sum(DST)
        
        dist = [[(+inf, +inf)] * n for _ in range(m)]
        dist[0][0] = (0, 0)
        pq = [(self.manhattan(*SRC), 0, SRC)]
        while pq:
            heuristic, removals, (r, c) = heappop(pq)
            if removals + self.manhattan(r, c) <= k:
                return heuristic
            if (r, c) == DST:
                break
            for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                removals_uv = removals + grid[i][j]
                if removals_uv > k:
                    continue
                dist_uv = dist[r][c][0] + 1
                dist_v, removals_v = dist[i][j]
                if dist_uv < dist_v:
                    dist[i][j] = (dist_uv, removals_uv)
                if dist_uv < dist_v or (dist_uv == dist_v and removals_uv < removals_v):
                    heappush(pq, (self.manhattan(i, j) + dist_uv, removals_uv, (i, j)))

        return dist[-1][-1][0] if dist[-1][-1][0] < +inf else -1            

    def manhattan(self, x, y):
        return self.total - sum((x, y))