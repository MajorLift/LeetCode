// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for u, v, w in flights:
            adj[u][v] = w
        dist = [-math.inf] + [+math.inf for _ in range(n)]
        dist[src] = 0
        pq = [(0, k + 1, src)]
        while pq:
            cost, rem, curr = heappop(pq)
            if rem < 0:
                continue
            if curr == dst:
                return cost
            for v, w in enumerate(adj[curr]):
                if w <= 0:
                    continue
                if cost + w < dist[v]:
                    dist[v] = cost + w
                    heappush(pq, (dist[v], rem - 1, v))
        return -1