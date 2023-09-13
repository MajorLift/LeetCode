// https://leetcode.com/problems/parallel-courses-iii

from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n)]
        indegrees = [0 for _ in range(n)]
        for src, dst in relations:
            adj[src - 1].append(dst - 1)
            indegrees[dst - 1] += 1
        completed = set()
        queue = deque([node for node in range(n) if indegrees[node] == 0])
        ans = 0
        while queue:
            ans += 1
            for curr in list(queue):
                queue.popleft()
                time[curr] -= 1
                if time[curr] > 0:
                    queue.append(curr)
                else:
                    completed.add(curr)
                    for node in adj[curr]:
                        if node not in completed:
                            indegrees[node] -= 1
                            if indegrees[node] == 0:
                                queue.append(node)
        return ans