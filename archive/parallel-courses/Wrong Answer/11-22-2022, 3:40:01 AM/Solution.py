// https://leetcode.com/problems/parallel-courses

from collections import deque

class Solution:
    # Kahn's algorithm BFS
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in relations:
            adj[u - 1].append(v - 1)
            indegree[v - 1] += 1
        ans = 1
        queue = deque([node for node in range(n) if indegree[node] == 0])
        while queue:
            ans += 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
        return ans if ans > 1 else -1