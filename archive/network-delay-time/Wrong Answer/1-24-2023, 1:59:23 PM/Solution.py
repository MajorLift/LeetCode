// https://leetcode.com/problems/network-delay-time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u][v] = w
        
        mst = set()
        dist = [-math.inf] + [0 if i == k else +math.inf for i in range(1, n + 1)]
        pq = [(dist[k], k)]
        while pq:
            _, u = heappop(pq)
            mst.add(u)
            for v, w in enumerate(adj[u]):
                if w < 0:
                    continue
                if dist[u] + w < dist[v] and v not in mst:
                    dist[v] = dist[u] + w
                    heappush(pq, (w, v))

        if all(x < +math.inf for x in dist):
            return max(dist)
        return  -1
