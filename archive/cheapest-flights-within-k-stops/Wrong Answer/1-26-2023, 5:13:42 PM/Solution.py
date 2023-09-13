// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[-1 for _ in range(n)] for _ in range(n)]
        for u, v, w in flights:
            adj[u][v] = w
        dist, min_stops = [+math.inf] * n, [+math.inf] * n
        dist[src], min_stops[src] = 0, 0
        pq = [(0, 0, src)]
        while pq:
            price, stops, u = heappop(pq)
            if stops > k:
                continue
            if u == dst:
                break
            for v, w in enumerate(adj[u]):
                if w <= 0:
                    continue
                if price + w < dist[v]:
                    dist[v] = price + w
                    heappush(pq, (dist[v], stops + 1, v))
                    if stops < min_stops[v]:
                        min_stops[v] = stops
                # elif price + w >= dist[v] and stops < min_stops[v]:
                #     heappush(pq, (price + w, stops + 1, v))
                #     min_stops[v] = stops
        return dist[dst] if dist[dst] < +math.inf else -1