// https://leetcode.com/problems/path-with-maximum-probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[0.0] * n for _ in range(n)]
        for (u, v), w in zip(edges, succProb):
            adj[u][v] = w
            adj[v][u] = w
        dist = [0.0] * n
        pq = [(-1.0, start)]
        while pq:
            dist_u, u = heappop(pq)
            dist_u *= -1
            if u == end:
                break
            for v, dist_v in enumerate(adj[u]):
                if dist_v == 0.0: continue
                if dist_u * dist_v > dist[v]:
                    dist[v] = dist_u * dist_v
                    heappush(pq, (-dist[v], v))
        return dist[end] if dist[end] < 1.0 else 0.0