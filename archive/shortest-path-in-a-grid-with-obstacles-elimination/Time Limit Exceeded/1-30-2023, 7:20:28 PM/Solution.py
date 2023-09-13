// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        source, target = (0, 0), (m - 1, n - 1)

        dist = [[(+math.inf, +math.inf) for _ in range(n)] for _ in range(m)]
        dist[0][0] = (0, 0)
        pq = [(sum(target), 0, 0, source)]
        while pq:
            heuristic, steps, removals, (r, c) = heappop(pq)
            if k - removals >= heuristic - steps:
                return heuristic

            for i, j in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if not (0 <= i < m and 0 <= j < n):
                    continue

                min_steps_next, min_removals_next = dist[i][j]
                steps_next, removals_next = steps + 1, removals + grid[i][j]

                if steps_next < min_steps_next or (steps_next == min_steps_next and removals_next < min_removals_next):
                    dist[i][j] = (steps_next, removals_next)
                if (steps_next < min_steps_next or removals_next < min_removals_next) and removals_next <= k:
                    heappush(pq, (steps_next + sum(target) - sum((i, j)), steps_next, removals_next, (i, j)))

        min_steps_to_target = dist[-1][-1][0]
        return min_steps_to_target if min_steps_to_target < +math.inf else -1