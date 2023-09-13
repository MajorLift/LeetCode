// https://leetcode.com/problems/network-delay-time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        times = [(u - 1, v - 1, w) for u, v, w in times]
        k -= 1
        # deserialize input into graph
        adj_mat = [[0 for j in range(n)] for i in range(n)]
        for source, target, weight in times:
            adj_mat[source][target] = weight
        print(adj_mat)
        
        dist = [float('inf') if i != k else 0 for i in range(n)]
        visited = [False for i in range(n)]
        pq = [(0, k)]

        while pq:
            dist_u, u = heapq.heappop(pq)
            print(u)
            visited[u] = True
            for v, dist_v in enumerate(adj_mat[u]):
                if dist_v == 0:
                    continue
                alt_dist = dist_u + dist_v
                if alt_dist < dist[v]:
                    dist[v] = alt_dist
                    heapq.heappush(pq, (alt_dist, v))
        print(dist, pq)
        
        if max(dist) == float('inf'):
            return -1
        return max(dist)