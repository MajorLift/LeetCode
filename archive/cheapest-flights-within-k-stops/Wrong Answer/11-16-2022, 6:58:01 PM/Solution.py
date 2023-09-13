// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[-1 for _ in range(n)] for _ in range(n)]
        for u, v, w in flights:
            adj[u][v] = w
        print(adj)
        
        dist = [+math.inf for _ in range(n)]
        dist[src] = 0
        prev = [None for _ in range(n)]
        pq = [(0, 0, src)]
        while pq:
            print(dist)
            price, steps, curr = heapq.heappop(pq)
            if curr == dst:
                return dist[dst]
            for node, cost in enumerate(adj[curr]):
                if cost >= 0 and dist[node] > dist[curr] + cost and steps <= k:
                    dist[node] = dist[curr] + cost
                    prev[node] = curr
                    heapq.heappush(pq, (dist[node], steps + 1, node))
        return -1