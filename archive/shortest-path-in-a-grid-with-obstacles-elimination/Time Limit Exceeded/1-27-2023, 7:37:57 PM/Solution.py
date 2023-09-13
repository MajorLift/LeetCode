// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        source, target = (0, 0), (m - 1, n - 1)

        def dist_remaining(r, c):
            return sum(target) - sum((r, c))

        max_dist = dist_remaining(0, 0)
        if k >= max_dist:
            return max_dist
        
        dist = [[(+math.inf, +math.inf) for _ in range(n)] for _ in range(m)]
        dist[0][0] = (0, 0)
        pq = [(0, 0, source)]
        while pq:
            steps, removals, (r, c) = heappop(pq)
            if (r, c) == target:
                return steps
            if k - removals >= steps + dist_remaining(r, c):
                return steps + dist_remaining(r, c)

            for i, j in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                min_state_steps, min_state_removals = dist[i][j]
                if steps + 1 < min_state_steps:
                    dist[i][j] = (steps + 1, removals + grid[i][j])
                if removals + grid[i][j] <= k \
                    and (steps + 1 < min_state_steps \
                        or removals + grid[i][j] < min_state_removals):
                    heappush(pq, (steps + 1, removals + grid[i][j], (i, j)))
        return -1