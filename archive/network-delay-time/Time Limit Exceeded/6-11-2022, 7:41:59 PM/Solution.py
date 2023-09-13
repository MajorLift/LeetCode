// https://leetcode.com/problems/network-delay-time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # convert vertex labels to zero-index
        times = [(u - 1, v - 1, w) for u, v, w in times]
        k -= 1
        
        # deserialize input into graph
        adj_mat = [[-1 for j in range(n)] for i in range(n)]
        for source, target, weight in times:
            adj_mat[source][target] = weight
        
        dist = [math.inf if i != k else 0 for i in range(n)]
        visited = [False for _ in range(n)]
        pq = [(0, k)]

        while pq:
            dist_v, v = heapq.heappop(pq)
            visited[v] = True
            for u, weight_u in enumerate(adj_mat[v]):
                if weight_u == -1:
                    continue
                dist[u] = min(dist[u], dist_v + weight_u)
                if not visited[u]:
                    heapq.heappush(pq, (dist[u], u))

        return max(dist) if math.inf not in dist else -1