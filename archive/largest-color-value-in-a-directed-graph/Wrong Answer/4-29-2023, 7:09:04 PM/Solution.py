// https://leetcode.com/problems/largest-color-value-in-a-directed-graph

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, m = map(len, (colors, edges))
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        
        @cache
        def dp(start):
            visited, cnt = set(), defaultdict(int)
            def dfs(node):
                if node in visited:
                    return -1
                cnt[colors[node]] += 1
                if not adj[node]:
                    return max(cnt.values())
                visited.add(node)
                res = [dfs(v) for v in adj[node]]
                if any(e == -1 for e in res):
                    return -1
                return max(res)
            return dfs(start)
        
        return max([dp(i) for i in range(n)])