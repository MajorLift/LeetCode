// https://leetcode.com/problems/largest-color-value-in-a-directed-graph

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj, indegree = [[] for _ in range(n)], [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        queue = deque([i for i,e in enumerate(indegree) if e == 0])
        def dfs(node, cnt = defaultdict(int), visited = set()):
            cnt[colors[node]] += 1
            if node in visited:
                return -1
            visited.add(node)
            if not adj[node]:
                return sorted(cnt.items(), key=lambda p: p[1], reverse=True)[0][1]
            ans = -1
            for child in adj[node]:
                res = dfs(child, cnt, visited)
                if res == -1:
                    return -1
                ans = max(ans, res)
            return ans
        return max(list(map(dfs, queue))) if queue else -1