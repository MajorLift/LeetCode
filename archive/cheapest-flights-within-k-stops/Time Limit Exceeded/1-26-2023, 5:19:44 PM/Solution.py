// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[0] * n for _ in range(n)]
        for u, v, w in flights:
            adj[u][v] = w

        dist = [+math.inf] * n
        dist[src] = 0
        pq = [(dist[src], 0, src)]
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
                # if stops < min_stops[v]:
                #     min_stops[v] = stops
                heappush(pq, (price + w, stops + 1, v))
                
        return dist[dst] if dist[dst] < +math.inf else -1