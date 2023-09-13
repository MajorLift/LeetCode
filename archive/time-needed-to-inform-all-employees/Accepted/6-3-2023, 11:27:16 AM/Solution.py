// https://leetcode.com/problems/time-needed-to-inform-all-employees

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ans = 0
        adj = defaultdict(list)
        for employee, superior in enumerate(manager):
            if employee == headID: continue
            adj[superior].append(employee)
        dist = defaultdict(lambda: +inf)
        dist[headID] = informTime[headID]
        pq = [(dist[headID], headID)]
        while pq:
            dist_u, u = heappop(pq)
            for v in adj[u]:
                if dist_u + informTime[v] < dist[v]:
                    dist[v] = dist_u + informTime[v]
                    heappush(pq, (dist_u + informTime[v], v))
        return max(dist.values())