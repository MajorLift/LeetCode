// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        source, target = (0, 0), (m - 1, n - 1)

        def dist_remaining(r, c):
            return sum(target) - sum((r, c))
      
        dist = [[(+math.inf, +math.inf) for _ in range(n)] for _ in range(m)]
        dist[0][0] = (0, 0)
        pq = [(0, 0, source)]
        while pq:
            steps, removals, (r, c) = heappop(pq)
            if (r, c) == target:
                break
            if k - removals >= steps + dist_remaining(r, c):
                return steps + dist_remaining(r, c)

            for i, j in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                min_state_steps, min_state_removals = dist[i][j]
                if steps + 1 < min_state_steps and removals + grid[i][j] <= k:
                    dist[i][j] = (steps + 1, removals + grid[i][j])
                    heappush(pq, (steps + 1, removals + grid[i][j], (i, j)))

        return dist[-1][-1][0] if dist[-1][-1][0] < +math.inf else -1