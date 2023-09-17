class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(i, 1 << i) for i in range(n)])
        visited = set(queue)

        steps = 0
        while queue:
            next_queue = deque()
            while queue:
                u, mask = queue.popleft()
                if mask == (1 << n) - 1:
                    return steps
                for v in graph[u]:
                    if (v, mask | (1 << v)) not in visited:
                        visited.add((v, mask | (1 << v)))
                        next_queue.append((v, mask | (1 << v)))
            queue = next_queue
            steps += 1