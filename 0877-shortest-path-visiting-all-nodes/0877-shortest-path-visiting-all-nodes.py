class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        cache = dict()
        def dfs(node: int, mask: int) -> int:
            if (node, mask) in cache:
                return cache[(node, mask)]
            if mask ^ (1 << node) == (1 << n) - 1:
                return 0
            cache[(node, mask)] = +inf
            cache[(node, mask)] = reduce(
                lambda acc, v: min(
                    acc, 
                    1 + dfs(v, mask ^ (1 << node)), 
                    1 + dfs(v, mask)), 
                [v for v in graph[node] if not mask & (1 << v)],
                +inf)
            return cache[(node, mask)]

        return min(dfs(i, 0) for i in range(n))