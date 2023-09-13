// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        source, target = (0, 0), (m - 1, n - 1)

        def manhattan_dist_to_target(r, c):
            return sum(target) - sum((r, c))
      
        dist = [[(+math.inf, +math.inf) for _ in range(n)] for _ in range(m)]
        dist[0][0] = (0, 0)
        pq = [(0, 0, source)]
        while pq:
            steps, removals, (r, c) = heappop(pq)
            if (r, c) == target:
                break
            if k - removals >= steps + manhattan_dist_to_target(r, c):
                return steps + manhattan_dist_to_target(r, c)

            for i, j in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                min_steps_next, min_removals_next = dist[i][j]
                if removals + grid[i][j] <= k and \
                    (steps + 1 < min_steps_next or \
                    (min_steps_next <= steps + 1 < +math.inf and removals + grid[i][j] < min_removals_next)):
                    dist[i][j] = (steps + 1, removals + grid[i][j])
                    heappush(pq, (steps + 1, removals + grid[i][j], (i, j)))

        return dist[-1][-1][0] if dist[-1][-1][0] < +math.inf else -1