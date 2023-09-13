// https://leetcode.com/problems/number-of-good-paths

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n, self.vals = len(vals), vals
        if n == 1: return 1

        self.adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

        cnt = defaultdict(list)
        for i,e in enumerate(vals):
            cnt[e].append(i)
        ans = 0
        for matches in cnt.values():
            if len(matches) == 1:
                ans += 1
                continue
            for a, b in combinations(matches, 2):
                ans += self.findPath(a, b)
        return ans
        
    def findPath(self, a, b) -> int:
        def dfs(s, t, path):
            if s == t:
                return len(path)
            ans = 0
            for v in self.adj[s]:
                if v in path \
                    or self.vals[v] > self.vals[a]:
                    continue
                path.add(v)
                ans += dfs(v, t, path)
            return ans
        return dfs(a, b, set([a]))