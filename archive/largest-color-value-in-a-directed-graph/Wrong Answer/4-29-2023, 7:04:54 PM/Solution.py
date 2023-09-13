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
            @cache
            def dfs(node):
                if node in visited:
                    return -1
                cnt[colors[node]] += 1
                if not adj[node]:
                    return max(cnt.values())
                visited.add(node)
                return max([dfs(v) for v in adj[node]])
            return dfs(start)
        
        return max([dp(i) for i in range(n)])