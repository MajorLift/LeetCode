// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build adjacency list from flights
        graph = [[] for _ in range(n)]
        for source, target, cost in flights:
            graph[source].append((target, cost))
        
        # bellman-ford with optimization
        # relax edges v-1 times
        dist = [(math.inf, 0) if i != src else (0, 0) for i in range(n)]
        queue = deque([src])
        # if relaxed and not in queue, add to queue
        while queue:
            print(dist)
            v = queue.popleft()
            for u, cost_u in graph[v]:
                if dist[v][0] + cost_u < dist[u][0]:
                    dist[u] = (dist[v][0] + cost_u, dist[v][1] + 1)
                    if u not in queue and dist[u][1] <= k:
                        queue.append(u)
        
#         # negative cycle discovery
#         for _ in range(n - 1):      
        
        # return found shortest path if it has length leq k
        return dist[dst][0] if dist[dst][0] < math.inf else -1