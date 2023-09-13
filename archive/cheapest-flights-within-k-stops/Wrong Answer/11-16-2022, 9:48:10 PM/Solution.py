// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[0 for _ in range(n)] for _ in range(n)]
        for u, v, w in flights:
            adj[u][v] = w
        print(adj)
        
        dist = [+math.inf for _ in range(n)]
        curr_stops = [+math.inf for _ in range(n)]
        dist[src], curr_stops[src] = 0, 0
        pq = [(0, 0, src)]
        while pq:
            print(dist)
            price, stops, curr = heapq.heappop(pq)
            if stops > k:
                continue
            if curr == dst:
                break
            for node, cost in enumerate(adj[curr]):
                if cost == 0:
                    continue
                if dist[node] > dist[curr] + cost:
                    dist[node] = dist[curr] + cost
                    heapq.heappush(pq, (dist[node], stops + 1, node))
                    curr_stops[node] = stops
                elif stops < curr_stops[node]:
                    heapq.heappush(pq, (dist[curr] + cost, stops + 1, node))
        print(curr_stops)
        return -1 if dist[dst] == +math.inf else dist[dst]