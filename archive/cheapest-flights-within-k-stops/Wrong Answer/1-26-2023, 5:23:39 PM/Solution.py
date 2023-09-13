// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[0] * n for _ in range(n)]
        for u, v, w in flights:
            adj[u][v] = w

        min_cost, min_stops = [+math.inf] * n, [+math.inf] * n
        min_cost[src], min_stops[src] = 0, 0
        pq = [(0, 0, src)]
        while pq:
            cost, stops, u = heappop(pq)
            if stops > k:
                continue
            if u == dst:
                break
            for v, w in enumerate(adj[u]):
                if w <= 0:
                    continue
                if cost + w < min_cost[v]:
                    min_cost[v] = cost + w
                    heappush(pq, (cost + w, stops + 1, v))
                if stops < min_stops[v]:
                    min_stops[v] = stops
                    heappush(pq, (cost + w, stops + 1, v))
                
        return min_cost[dst] if min_cost[dst] < +math.inf else -1