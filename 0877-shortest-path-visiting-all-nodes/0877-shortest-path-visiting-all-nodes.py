class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(0, i, 1 << i) for i in range(n)])
        visited = set(queue)
        while queue:
            steps, u, mask = queue.popleft()
            if mask == (1 << n) - 1:
                return steps
            for v in graph[u]:
                if (v, mask | (1 << v)) not in visited:
                    visited.add((v, mask | (1 << v)))
                    queue.append((steps + 1, v, mask | (1 << v)))