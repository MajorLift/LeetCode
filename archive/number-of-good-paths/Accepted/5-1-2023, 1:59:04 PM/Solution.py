// https://leetcode.com/problems/number-of-good-paths

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        count = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([(max(vals[u], vals[v]), u, v) for u,v in edges])
        ans = n
        uf = UnionFind(n)
        for val, u, v in edges:
            root_u, root_v = map(uf.find, (u, v))
            if root_u == root_v:
                continue
            ans += count[root_u][val] * count[root_v][val]
            uf.union(u, v)
            count[root_u] = Counter({val: count[root_u][val] + count[root_v][val]})
        return ans

class UnionFind:
    def __init__(self, size):
        self.roots = list(range(size + 1))
        self.cnt = [1] * (size + 1)

    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        rootX, rootY = map(self.find, (x, y))
        if rootX == rootY:
            return
        self.roots[rootY] = rootX
        self.cnt[rootX] += self.cnt[rootY]
        self.cnt[rootY] = 0
