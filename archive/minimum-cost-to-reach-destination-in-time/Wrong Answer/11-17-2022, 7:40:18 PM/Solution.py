// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], fees: List[int]) -> int:
        n = len(fees)
        adj = [[-1 for _ in range(n)] for _ in range(n)]
        for u, v, w in edges:
            adj[u][v] = w
            adj[v][u] = w
        min_times = [+math.inf for _ in range(n)]
        cost, time, city = fees[0], 0, 0
        pq = [(cost, time, city)]
        while pq:
            cost, time, city = heapq.heappop(pq)
            if city == n - 1:
                return cost
            if min_times[city] > time:
                min_times[city] = time
                for node, add_time in enumerate(adj[city]):
                    if add_time < 0 or time + add_time > maxTime:
                        continue
                    heapq.heappush(pq, (cost + fees[node], time + add_time, node))
        return -1