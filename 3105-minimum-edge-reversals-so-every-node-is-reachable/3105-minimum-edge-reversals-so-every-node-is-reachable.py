class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_forward, adj_backward = [[] for _ in range(n)], [[] for _ in range(n)]
        for u, v in edges:
            adj_forward[u].append((v, 0))
            adj_backward[v].append((u, 1))
        
        @cache
        def dfs(node, parent):
            return sum(w + dfs(v, node) 
                       for v, w in adj_forward[node] + adj_backward[node] 
                       if v != parent)
        
        return [dfs(i, -1) for i in range(n)]
    