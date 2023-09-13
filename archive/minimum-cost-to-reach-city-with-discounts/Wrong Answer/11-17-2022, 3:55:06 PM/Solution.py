// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adj = [[-1 for _ in range(n)] for _ in range(n)]
        for u,v,w in highways:
            adj[u][v] = w
            adj[v][u] = w
        dist = [0] + [+math.inf for _ in range(n - 1)]
        cost, used_discounts, city = 0, 0, 0
        pq = [(cost, used_discounts, city)]
        while pq:
            cost, used_discounts, city = heapq.heappop(pq)
            for v, w in enumerate(adj[city]):
                if w < 0:
                    continue
                if dist[v] > cost + w:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], used_discounts, v))
                if dist[v] > cost + w // 2 and used_discounts < discounts:
                    dist[v] = cost + w // 2
                    heapq.heappush(pq, (dist[v], used_discounts + 1, v))
        return dist[-1] if dist[-1] < +math.inf else -1